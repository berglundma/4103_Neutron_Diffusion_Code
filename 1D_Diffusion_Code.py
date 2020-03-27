#!/usr/bin/python

#import sys
#import math
#import scipy
#import matplotlib
import numpy as np

problem_space = []
mesh_element = {}
mesh_element['x1'] = 0.0
mesh_element['x2'] = 0.0
mesh_element['flux'] = 0.0
mesh_element['flux_slope'] = 0.0
mesh_element['neutron_source'] = 0.0
mesh_element['absorption_cross_sections'] = [0.0, 0.0]
mesh_element['total_cross_sections'] = [0.0, 0.0]
# Assume no up-scatter
mesh_element['downscatter_cross_sections'] = [0.0, 0.0]
mesh_element['scatter_cross_sections'] = [0.0, 0.0]

convergance_factor = 0.0001

# Mesh range
mesh_range_bottom = -50.0
mesh_range_top    =  50.0
mesh_divisions = 100.0

# Core Region in cm
core_bottom = -100.0
core_top = 100.0

# Reflector region left in cm
ref_l_bottom = -110.0
ref_l_top = -100.0

# Reflector region right in cm
ref_l_bottom = 100.0
ref_l_top = 110.0

range_spacing = (abs(range_bottom) + range_top)/mesh_divisions

for mesh in np.arange(-100.0, 100.0, range_spacing):
    problem_space.append(mesh_element.copy())

print(len(problem_space))
print('stuffffff')
print(problem_space[11])
print(mesh_divisions)

# Define mesh boundary spacing
for i in range(0, len(problem_space)):
    problem_space[i]['x1'] = i * range_spacing
    problem_space[i]['x2'] = (i+1) * range_spacing

# Check stuff
for item in problem_space:
    print( item['x1'], item['x2'])

# Load Initial Values for each cell constant
for i in range(0, len(problem_space)):
    if (problem_space[i]['x1'] > -100
            and
        problem_space[i]['x1'] < 100):
        problem_space[i]['total_cross_sections'] = [0.2190,1.190]

## Load reflector region
for i in range(0, len(problem_space)):
    if (problem_space[i]['x1'] > -100 #This is a test
            and
        problem_space[i]['x1'] < 100):
        problem_space[i]['total_cross_sections'] = [0.2190,1.190]

# Iterate over mesh field
#for i in range(0, len(problem_space)):
#    print('left to right', i)

#for i in range(len(problem_space),0,-1):
#    print('right to left', i)

# Results
