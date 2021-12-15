# PODS-DYNO
This repository is the combination of DYNO (Dynamically Normalized Objective Function) with PODS optimization algorithm. The use of DYNO on PODS need few code changes on the origianl PODS (https://github.com/louisXW/PODS): 1) The selection of the best solution; 2) The rebuilt of the surrogate value with the newly calcuated objecitve function value with DYNO at each iteration; 3) The defination of the success and failure search of each iteration. In orginal PODS, an iteration is defined as a success if the objective function vlaue of the best solution found in the iteration imporved at least 0.001 of that in the last iteration. Otherwise it is considered as a failure. In PODS-DYNO, an iteration is defined as a success if there is at least one variable (e.g., one compnenet objective function), whoes value imporved at least 0.001 of that in the last iteration.


# PODS-DYNO

## About

This repository including 1) a standalone PODS-DYNO algorithm code; 2) examples using PODS-DYNO with test function; 3) examples using PODS-DYNO with expensive simulaiton problems (e.g., Deflt3D-FLOW). 

## Install

Preparing your system to use PODS-DYNO
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


