"""
.. module:: test_simple
  :synopsis: Test Simple
.. moduleauthor:: XiaWei
"""
import os
from dyno_pods.experimental_design import SymmetricLatinHypercube
from dyno_pods.sot_sync_strategies import SyncStrategyNoConstraintsDYNOPODS
from dyno_pods.rbf import RBFInterpolant, CubicKernel, LinearTail
from dyno_pods.adaptive_sampling import CandidateDYCORS
from dyno_pods.controller import MultiproController

import numpy as np
import os
import logging
from test_functions import *
import shutil

def obj_func(paramters):
    """
    The function for objective function evaluation.
    :param paramters: A tuple (x, simid, iterid)
        x: the dim dimensional parameter vector
        simid: the index of simulation ID in each iteration
        iterid: the index of iteration ID
        simid and iterid is used control a batch of simulations running simultaneously in each iteration.
    :return: the objective function value [subobj1, subobj2] (a list of multiple sub objectives)
    """
    data = Ackley_2obj(dim=10) #Initializaiton for the problem class
    data.home_dir = './'
    x, simid, iterid = paramters
    simid = simid
    iterid = iterid
    data.file_save =True
    data.project_name ='up22'
    data.file_result='pysot_result.txt'
    result = data.objfunction(x, simid, iterid)
    return result

def main():
    # -----------Initilizae logging-----------------#
    if not os.path.exists("./logfiles"):
        os.makedirs("logfiles")
    if os.path.exists("./logfiles/test_simple.log"):
        os.remove("./logfiles/test_simple.log")
    logging.basicConfig(filename="./logfiles/test_simple.log",
                        level=logging.INFO)

    # -----------Initilizae result saving-----------------#
    if not os.path.exists("./result"):
        os.makedirs("result")

        """ histroy_data folder is needed when you need to
        save the simultion output of each evaluation"""
    if os.path.exists("./result/history_data"):
        shutil.rmtree("./result/history_data")
    if not os.path.exists("./result/history_data"):
        os.makedirs("./result/history_data")

        """ pysot_tesult.txt file is for saving the objective
        function value and parameter vector of each evaluations"""
    if os.path.exists("./result/pysot_result.txt"):
        os.remove("./result/pysot_result.txt")

    fp = open("./result/pysot_result.txt", "a")
    fp.write("Iteration\tSimID\tObj\tParmaters\n")
    fp.close()

    # -----------set the threads and budget-----------------#
    nthreads = 24
    maxeval = 192
    nsamples = nthreads

    # (1) Initilize the Optimization problem
    data = Ackley_2obj(dim=10)
    logging.info(data.info)
    data.home_dir = '/home/xiawei/tem_vs_vel/cal_both/exp1_2/'

    # (2) Experimental design
    # Use a symmetric Latin hypercube with 2d + 1 samples
    exp_des = SymmetricLatinHypercube(dim=data.dim, npts=24)

    # (3) Surrogate model
    # Use a cubic RBF interpolant with a linear tail
    surrogate = RBFInterpolant(kernel=CubicKernel, tail=LinearTail, maxp=maxeval)

    # (4) Adaptive sampling
    adapt_samp = CandidateDYCORS(data=data, numcand=1000 * data.dim)

    # (5) Use predefined initial experiment design
    #'./ini_exp/ini_fxs.txt' contains a list of decision variables in predefined experiments design
    # The number of samples should be multiples of nsamples (i.e., the number of parallel processors used)
    # (in this case 24 samples were used)
    # './ini_exp/ini_xs.txt' contains the list of objective functions for the predefined experiments design
    # In this case there are two objectives for each of the 24 samples
    ini_vals = np.loadtxt('./ini_exp/ini_fxs.txt') # shape of ini_xs should be (npt, number of objectives);
    # if there is one objective shape of ini should be (npt, 1) not (npt,)
    ini_xs = np.loadtxt('./ini_exp/ini_xs.txt') # shape of ini_vals should be (npt, dim)

    # (6) Use the multiprocessing-based sychronous strategy without non-bound constraints
    #if use predefined initial experiment design need to specify the ini_xs variable (list of decision
    # variables of the initial experiment design) as shown below;
    # ini_vals (list of objective function values) is not mandatory
    strategy = SyncStrategyNoConstraintsDYNOPODS(obj_func,
                                                worker_id=0, data=data, maxeval=maxeval, nsamples=nsamples,
                                                exp_design=exp_des, response_surface=surrogate,
                                                sampling_method=adapt_samp, ini_xs=ini_xs, ini_vals=ini_vals)

    # (6) Use the multiprocessing-based sychronous controller
    controller = MultiproController()
    controller.strategy = strategy

    # Run the optimization strategy
    result = controller.run()
    print "result", result



if __name__ == "__main__":
   main()



