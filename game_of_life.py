# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 12:30:46 2019

@author: Administrator
"""

import numpy as np
from random import choice
from copy import deepcopy
from time import sleep
from tkinter import *
mygui = Tk()
mainloop()

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
worldHigh = 5
worldWidth= 5
aliveNumber = 3
deadNumber = 2
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
        self.world=self.initialWorld()
        self.initAlivePoint()
        
    def initialWorld(self):
        world = []
        for pos_x in range(worldHigh):
            column=[]
            for pos_y in range(worldWidth):
                column.append(Point((pos_x,pos_y)))
            world.append(column)
        return world
    
    def initAlivePoint(self):
        for high in self.world:
            for point in high:
                if choice((0,1)) == 0:
                    continue
                point.setAlive()

    def count(self, point_obj):
        number = 0
        for x in range(-1,2):
            for y in range(-1,2):
                point_x = point_obj.x + x
                point_y = point_obj.y + y
                if ((point_x,point_y) == point_obj.pos) or \
                ((point_x < 0) or (point_x >= worldHigh)) or \
                ((point_y < 0) or (point_y >= worldWidth)):
                    continue
                print(point_obj.x,point_x)
                print(point_obj.y,point_y)
                if self.world[point_x][point_y].isAlive:
                    number += 1
        return number
    
    def gameProcess(self):
        new_world = deepcopy(self.world)
        for x, widelist in enumerate(self.world):
            for y, _ in enumerate(widelist):
                current_point = self.world[x][y]
                alive_num = self.count(current_point)
                if alive_num == aliveNumber:
                    current_point.setAlive()
                elif alive_num != deadNumber:
                    current_point.setDead()
        self.world = new_world
        sleep(0.2)
            
if __name__ == '__main__':
    current_world = World()
    current_world.gameProcess()
      
        
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

        