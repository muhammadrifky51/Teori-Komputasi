# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 00:26:42 2018

@author: Muhammad Rifky Y
"""

import tkinter as tk
from turtle import RawTurtle,TurtleScreen,ScrolledCanvas

class Lindenmayer:
    
    def __init__(self,x):
        self.it=x
        S="D+D+D+D"
        for i in range(self.it):
            pesan=""
            for j in range(len(S)):
                if S[j]=="D":
                    pesan+="D+D-D-DD+D+D-D"
                else:
                    pesan+=S[j]
            S=pesan
        root3=tk.Tk()
        if self.it!=1:
            root3.title('Lindenmayer Fractal with '+str(self.it)+' iterations')
        else:
            root3.title('Lindenmayer Fractal with an iteration')
        self.canvas=ScrolledCanvas(master=root3,width=1000,height=1000)
        self.canvas.pack(fill=tk.BOTH,expand=tk.YES)
        screen=TurtleScreen(self.canvas)
        screen.screensize(10000,10000)
        self.turtle=RawTurtle(screen)
        self.turtle.ht()
        self.turtle.speed(0)
        for i in range(len(S)):    
            if S[i]=="D":
                self.turtle.forward(10)
            elif S[i]=="+":
                self.turtle.right(90)
            else:
                self.turtle.left(90)
        self.canvas.bind('<MouseWheel>',self.zoom)
        screen.mainloop()
    
    def zoom(self,event):
        amount=0.9 if event.delta<0 else 1.1
        self.canvas.scale(tk.ALL,0,0,amount,amount)