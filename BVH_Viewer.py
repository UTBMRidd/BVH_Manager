from vpython import *
import sys
import os
import numpy as np
import scipy.interpolate as interpolate
import scipy.ndimage.filters as filters
import BVH as BVH
import Animation as Animation
from Quaternions import Quaternions

anims,names,_ = BVH.load('test.bvh')
global_xforms = Animation.transforms_global(anims)
global_positions = global_xforms[:,:,:3,3] / global_xforms[:,:,3:,3]
global_rotations = Quaternions.from_transforms(global_xforms)
for i in range(0,anims.parents.shape[0]):
    joint_vec = vec(global_positions[0,i,0],global_positions[0,i,1],global_positions[0,i,2])
    sphere(pos=joint_vec, radius=0.5)
    parent_id = anims.parents[i]
    if(parent_id != -1):
        xdir = global_positions[0,parent_id,0] - global_positions[0,i,0]
        ydir = global_positions[0,parent_id,1] - global_positions[0,i,1]
        zdir = global_positions[0,parent_id,2] - global_positions[0,i,2]
        rod = cylinder(pos=joint_vec,axis=vec(xdir,ydir,zdir), radius=0.2)
#sphere(pos=vec(1,2,1), radius=0.5)
#rod = cylinder(pos=vec(0,2,1),axis=vec(5,0,0), radius=1)