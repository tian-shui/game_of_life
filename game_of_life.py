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
import argparse

def argumentProcess():
    global arguments
    parser = argparse.ArgumentParser(description='Game of Life')
    parser.add_argument('-n','--cell_number',required=True,
    type=int,nargs=1,default=10,help='The cell number every row/col [required].')
    parser.add_argument('-w','--cell_width',required=True,
    type=int,nargs=1,default=50,help='The width of every cell [required]. ')
    parser.add_argument('-a','--alive_number',required=True,
    type=int,nargs=1,default=3,help='The cell can be alive when the number of surrounded cells is a. ')
    parser.add_argument('-k','--keep_number',required=True,
    type=int,nargs=1,default=2,help='The cell will not change when the number of surrounded cells is k. ')
    parser.add_argument('-s','--speed',required=True,
    type=int,nargs=1,default=1,help='The speed that canvas change is s. ')
    parser.add_argument('-t','--times',required=True,
    type=int,nargs=1,default=10,help='The times that canvas change is t. ')
    args=parser.parse_args()
    arguments={}
    arguments["cell number"]=args.cell_number[0]
    arguments["cell width"]=args.cell_width[0]
    arguments["alive number"]=args.alive_number[0]
    arguments["keep number"]=args.keep_number[0]
    arguments["speed"]=args.speed[0]
    arguments["times"]=args.times[0]
    
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
        for pos_x in range(arguments["cell number"]):
            column=[]
            for pos_y in range(arguments["cell number"]):
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
                ((point_x < 0) or (point_x >= arguments["cell number"])) or \
                ((point_y < 0) or (point_y >= arguments["cell number"])):
                    continue

                if self.world[point_x][point_y].isAlive:
                    number += 1
        return number
    
    def gameProcess(self):
        new_world = deepcopy(self.world)
        displist = []
        for x, widelist in enumerate(new_world):
            row = []
            for y, _ in enumerate(widelist):
                current_point = new_world[x][y]
                alive_num = self.count(current_point)
                if alive_num == arguments["alive number"]:
                    current_point.setAlive()
                elif alive_num != arguments["keep number"]:
                    current_point.setDead()                    
                if current_point.isAlive:
                    row.append(1)
                else:
                    row.append(0)
            displist.append(row)
        self.world = new_world
        return displist

def cellDisplay(displist):
    width = arguments["cell width"]
    for i in range(0,arguments["cell number"]):
        pos_x = i*width
        for j in range(0,arguments["cell number"]):
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
    if argumentProcess():
        current_world = World()
        window = tk.Tk()
        canvas = tk.Canvas(window, height=arguments["cell number"]*arguments["cell width"],
        width=arguments["cell number"]*arguments["cell width"])
        canvas.pack()
        looptimes=arguments["times"]
        aa=[]
        for times in range(looptimes):
            displist = current_world.gameProcess()
            aa.append(displist)
            cellDisplay(displist)
            window.update()
            sleep(arguments["speed"])
    
    btn = tk.Button(window,text='Start')
    btn.pack()
    tk.mainloop()          