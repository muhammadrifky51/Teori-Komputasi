# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 23:22:28 2018

@author: Muhammad Rifky Y
"""
import tkinter as tk
from turtle import RawTurtle,TurtleScreen,ScrolledCanvas

class Sierpinski:
    
    def __init__(self,x):
        self.it=x
        S="E+D+D"
        for i in range(self.it):
            pesan=""
            for j in range(len(S)):
                if S[j]=="E":
                    pesan+="E+D-E-D+E"
                elif S[j]=="D":
                    pesan+="DD"
                else:
                    pesan+=S[j]
            S=pesan
        root3=tk.Tk()
        if self.it!=1:
            root3.title('Sierpinski Fractal with '+str(self.it)+' iterations')
        else:
            root3.title('Sierpinski Fractal with an iteration')
        self.canvas=ScrolledCanvas(master=root3,width=1000,height=1000)
        self.canvas.pack(fill=tk.BOTH,expand=tk.YES)
        screen=TurtleScreen(self.canvas)
        screen.screensize(10000,10000)
        self.turtle=RawTurtle(screen)
        self.turtle.ht()
        self.turtle.speed(0)
        for i in range(len(S)):    
            if S[i]=="E" or S[i]=="D":
                self.turtle.forward(10)
            elif S[i]=="+":
                self.turtle.left(120)
            else:
                self.turtle.right(120)
        self.canvas.bind('<MouseWheel>',self.zoom)
        screen.mainloop()
    
    def zoom(self,event):
        amount=0.9 if event.delta<0 else 1.1
        self.canvas.scale(tk.ALL,0,0,amount,amount)