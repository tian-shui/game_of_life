# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 12:30:46 2019

@author: Administrator
"""

from random import choice
from copy import deepcopy
from time import sleep
import tkinter as tk

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
        for pos_x in range(cell_number):
            column=[]
            for pos_y in range(cell_number):
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
                ((point_x < 0) or (point_x >= cell_number)) or \
                ((point_y < 0) or (point_y >= cell_number)):
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
                if alive_num == alive_number:
                    current_point.setAlive()
                elif alive_num != keep_number:
                    current_point.setDead()                    
                if current_point.isAlive:
                    row.append(1)
                else:
                    row.append(0)
            displist.append(row)
        self.world = new_world
        return displist

def cellDisplay(displist):
    width = cell_width
    for i in range(0,cell_number):
        pos_x = i*width
        for j in range(0,cell_number):
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
    cell_number = int(input('Please input the number of cell:'))
    cell_width = int(input('Please input the width of cell:'))
    alive_number = int(input('Please input the number of alive:'))
    keep_number = int(input('Please input the number of keep:'))
    speed = float(input('Please input the speed:'))
    times = int(input('Please input the times:'))

    current_world = World()
    window = tk.Tk()
    window.title('game of life')
    l = tk.Label(window, text='Welcome to the game of life!', bg='white', font=('Arial', 12), width=30, height=2)
    l.pack()
    canvas = tk.Canvas(window, height=cell_number*cell_width,
                       width=cell_number*cell_width)
    canvas.pack()

    for time in range(times):
        displist = current_world.gameProcess()
        cellDisplay(displist)
        window.update()
        sleep(speed)

tk.mainloop()



