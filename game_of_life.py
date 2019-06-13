# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 12:30:46 2019

@author: Administrator
"""

import numpy as np
from random import choice
from copy import deepcopy
from time import sleep
import tkinter as tk
from tkinter import *

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
worldHigh = 10
worldWidth= 10
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
    def display(self):
        if self.isAlive:
            return '*'
        else:
            return ' '
        
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

                if self.world[point_x][point_y].isAlive:
                    number += 1
        return number
    
    def display(self):
        if self.isAlive:
            return '*'
        else:
            return ' '
    
    def gameProcess(self):
        new_world = deepcopy(self.world)
        displist = []
        for x, widelist in enumerate(new_world):
            row = []
            for y, _ in enumerate(widelist):
                current_point = new_world[x][y]
                alive_num = self.count(current_point)
                if alive_num == aliveNumber:
                    current_point.setAlive()
                elif alive_num != deadNumber:
                    current_point.setDead()
                    
                if current_point.isAlive:
                    row.append(1)
                else:
                    row.append(0)
            displist.append(row)
        self.world = new_world
        return displist
       # sleep(0.2)

def cellDisplay(displist):
    width = 50
    for i in range(0,10):
        pos_x = i*width
        for j in range(0,10):
            pos_y = j*width
            canvas.create_rectangle(pos_x,pos_y,pos_x + width, pos_y + width, 
                                    fill='white')
    
    for row in range(len(displist)):
        row_x = row*width
        for col in range(len(displist)):
            col_y = col*width
            if displist[row][col] == 1:
                canvas.create_rectangle(col_y,row_x,col_y + width,row_x + width, 
                                         fill='black')    
                
if __name__ == '__main__':
    current_world = World()
    #displist = current_world.gameProcess()
    window = tk.Tk()
    canvas = tk.Canvas(window, height=500, width=500)
    canvas.pack()
    looptimes=10
    aa=[]
    for times in range(looptimes):
        displist = current_world.gameProcess()
        aa.append(displist)
        cellDisplay(displist)
        window.update()
        sleep(1)
    
    btn = tk.Button(window,text='Start')
    btn.pack()
    tk.mainloop() 
    
    
#    listb = tk.Listbox(window)          #  创建两个列表组件
#    for item in displist:               # 第一个小部件插入数据
#        listb.insert(0,item)
#     
#    listb.pack()                        # 将小部件放置到主窗口中
#    window.mainloop() 

      
        

        