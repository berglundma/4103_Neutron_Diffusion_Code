#!/usr/bin/python

import sys
import math
import scipy
import numpy
import mapotlotlib

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

range_bottom = -100.0
range_top    =  100.0
mesh_divisons = 200

range_spacing = (abs(range_bottom) + range_top)/mesh_divisons

for mesh in np.arange(-100.0, 100.0, range_spacing :problem_space.append(mesh_element.copy))
 

