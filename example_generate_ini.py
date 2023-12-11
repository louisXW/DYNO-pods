"""
.. module:: test_simple
  :synopsis: Test Simple
.. moduleauthor:: XiaWei
"""
import os
from dyno_pods.experimental_design import SymmetricLatinHypercube
from dyno_pods.utils import *
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

    # -----------Initilizae ini_exp saving-----------------#
    """ ini_exp folder to
    save generated initial experiment design if you want to use the same initial experiment experiment
     design for multiple experiments"""
    if not os.path.exists("./ini_exp"):
        os.makedirs("ini_exp")


    # (1) Initilize the Optimization problem
    data = Ackley_2obj(dim=10)
    logging.info(data.info)

    # (2) Experimental design
    # Use a symmetric Latin hypercube with 2d + 1 samples; npts should be multiple of the number of parallel
    # processors you want to use
    exp_des = SymmetricLatinHypercube(dim=data.dim, npts=24)
    start_sample = exp_des.generate_points()
    start_sample = from_unit_box(start_sample, data)

    print ("generated %s samples for initial experiments design" %start_sample.shape[0])

    # (3) Evaluate Experimental design
    objfuns = []
    for j in range(start_sample.shape[0]):
        objfuns.append(obj_func([start_sample[j,:], 0, 0]))

    print ("finished the evaluation of %s samples for initial experiments design" % len(objfuns))
    print ("there are %s objectives" % len(objfuns[0]))

    np.savetxt("./ini_exp/ini_xs.txt", start_sample)
    np.savetxt("./ini_exp/ini_fxs.txt", np.asarray(objfuns))

if __name__ == "__main__":
   main()



