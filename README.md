
# DYNO-pods

## About

Dynamically Normalized objective function (DYNO) is a novel objective function (used with optimization algorithms) for multi-variable (i.e., temperature and velocity) model calibration problems. DYNO combines the error metrics of multiple variables into a single objective function by dynamically normalizing each variable's error terms using information available during the search. DYNO is proposed to dynamically adjust the weight of the error of each variable hence balancing the calibration to each variable during optimization search.

This repository is the combination of DYNO (Dynamically Normalized Objective Function) with PODS optimization algorithm. The use of DYNO with PODS needs a few code changes on the origianl PODS (https://github.com/louisXW/PODS): 1) The selection of the best solution; 2) The rebuilt of the surrogate value with the newly calcuated objecitve function value with DYNO at each iteration; 3) The defination of the success and failure search of each iteration. In orginal PODS, an iteration is defined as a success if the objective function vlaue of the best solution found in the iteration imporved at least 0.001 of that in the last iteration. Otherwise it is considered as a failure. In DYNO-pods, an iteration is defined as a success if there is at least one variable (e.g., one component objective function), whoes component objective function value imporved at least 0.001 of that in the last iteration.

DYNO can also be easily utilized with other heuristic optimization methods for multi-variables calibration problems with some modifications on the orignal optimization method, which depend on the structure of an optimization method. 

This repository includes 1) a standalone DYNO-pods algorithm code; 2) examples using DYNO-pods with test function; 3) examples using DYNO-pods with a toy Deflt3D-FLOW model calibration problem where velocity data at two stations are included in model calibration (this toy example is only for the purpose of demonstrating how to run the DYNO-pods code; users should make changes on the real_function.py accordingly for their own problem). 

## Install

Preparing your system to use DYNO-pods
------------------------------------

1. **python** & **pySOT**

Before starting you will need to Python installed. Recommend python 2.7 since PODS was developed and tested based on this verison.
You will need to have pySOT (0.1.36) installed. Other python module like (scipy, numpy, pyDOE) needed will be installed automatically once the pySOT is installed.

To install the pySOT (0.1.36) package with conda run one of the following:

```

		conda install -c conda-forge pysot==0.1.36
		
```
or
```
		conda install -c conda-forge/label/gcc7 pysot
```

pySOT is a open source toolbox is for optimization of computationally expensive black-box objective functions. 
more information about pySOT refer to: https://pysot.readthedocs.io/en/latest/index.html


2. **Delft3D**

To work with Delft3D problem you may need to have Delft3D installed.

Delft3D is an open source software which simulates two-dimensional (in either the horizontal or a vertical plane) and three-dimensional flow, sediment transport and morphology, waves, water quality and ecology and is capable of handling the interactions between these processes.

The Delft3D installation manual on both windows and linux links to https://content.oss.deltares.nl/delft3d/manuals/Delft3D-Installation_Manual.pdf

You may also want to compile the open source on your platform. The instruction links to https://oss.deltares.nl/c/document_library/get_file?uuid=e3bf2d05-f59f-4d4a-8c13-97bcbaa84060&groupId=21119


## Citing US

If you use DYNO-pods, please cite the coming DYNO paper and the original PODS paper: Xia, W., Shoemaker, C., Akhtar, T., & Nguyen, M. T. (2021). Efficient parallel surrogate optimization algorithm and framework with application to parameter calibration of computationally expensive three-dimensional hydrodynamic lake PDE models. Environmental Modelling & Software, 135, 104910.https://doi.org/10.1016/j.envsoft.2020.104910

```	
@article{xia2021efficient,
  title={Efficient parallel surrogate optimization algorithm and framework with application to parameter calibration of computationally expensive three-dimensional hydrodynamic lake PDE models},
  author={Xia, Wei and Shoemaker, Christine and Akhtar, Taimoor and Nguyen, Manh-Tuan},
  journal={Environmental Modelling \& Software},
  volume={135},
  pages={104910},
  year={2021},
  publisher={Elsevier}
}	
```

