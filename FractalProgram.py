# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 17:57:05 2018

@author: Muhammad Rifky Y
"""

import tkinter as tk
import sys
sys.path.insert(0,'FractalProgram')
from MainWindow import MainWindow

root=tk.Tk()
root.geometry("400x300")
root.resizable(False,False)
app=MainWindow(root)
app.mainloop()