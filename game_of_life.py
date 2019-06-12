# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 12:30:46 2019

@author: Administrator
"""

import numpy as np

#input_1 = np.zeros((5,5))
#input_1[2,2] = 1
#output_standard = np.zeros((5,5))

#for i in range(1,len(input_1)-1):
#    for j in range(1,len(input_1)-1):
#        number = 0
#        number += input_1[i-1,j-1]
#        number += input_1[i-1,j]
#        number += input_1[i-1,j+1]
#        number += input_1[i,j-1]
#        number += input_1[i,j+1]
#        number += input_1[i+1,j-1]
#        number += input_1[i+1,j]
#        number += input_1[i+1,j+1]
worldHigh=400
worldWidth=400
class Point:
    def __init__(self,position):
        self.pos = position
        self.isAlive = False
        self.x,self.y=self.pos
    def setAlive(self):
        self.isAlive=True
    def setDead(self):
        self.isAlive=False
        
class World:
    def __init__(self):
        world=[]
        self.world=self.initialWorld()
        for pos_x in range(worldHigh):
            column=[]
            for pos_y in range(worldWidth):
                column.append(Point((pos_x,pos_y)))
            world.append(column)
        return world
          
        
# def getNeighbours(self, input_1): 
#    alive_count = 0
#    for x_of in xrange(-1, 2): 
#      for y_of in xrange(-1, 2): 
#        c_x, c_y = input_1.x + x_of, input_1.y + y_of 
#        if ((c_x, c_y) == cell_obj.point) or \ 
#          (c_x < 0 or c_x >= WORLD_WIDE) or \ 
#          (c_y < 0 or c_y >= WORLD_HIGH): 
#          '''''排除自身和越界的点'''
#          continue
#        if self.world[c_x][c_y].is_alive: 
#          alive_count += 1
#    return alive_count 

        