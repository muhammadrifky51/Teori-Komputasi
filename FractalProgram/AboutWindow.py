# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 18:06:52 2018

@author: Muhammad Rifky Y
"""

from tkinter import Frame,BOTH,Label,W,LEFT

class AboutWindow(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.master=master
        self.init_window()
        
    def init_window(self):
        self.master.title("About")
        self.pack(fill=BOTH,expand=1)
        
        Judul=Label(self,text="Name\t: Muhammad Rifky Yusdiansyah\nNPM\t: 1506671423",anchor=W,justify=LEFT)
        Judul.pack()