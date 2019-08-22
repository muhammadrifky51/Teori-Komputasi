# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 23:03:22 2018

@author: Muhammad Rifky Y
"""

from tkinter import Frame,BOTH,CENTER,Label

class CautionWindow(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.master=master
        self.init_window()
        
    def init_window(self):
        self.master.title("Caution")
        self.pack(fill=BOTH,expand=1)
        
        Judul=Label(self,text="Iterasi harus lebih dari sama dengan 0",anchor=CENTER)
        Judul.pack()