# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 17:46:43 2018

@author: Muhammad Rifky Y
"""

import sys
import winsound
from tkinter import Frame,BOTH,Label,Button,CENTER,Menu,StringVar,Tk,OptionMenu,SW,NW,Entry
from AboutWindow import AboutWindow
from CautionWindow import CautionWindow
from Lindenmayer import Lindenmayer
from Batik import Batik
from Box import Box
from Koch import Koch
from Ring import Ring
from Sierpinski import Sierpinski
sys.path.insert(0,'..')

class MainWindow(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.master=master
        self.init_window()
        
    def init_window(self):
        self.master.title("Program Fraktal")
        self.pack(fill=BOTH,expand=1)
        
        Judul=Label(self,text="Program Fraktal by Muhammad Rifky Yusdiansyah")
        Judul.pack()
        
        AboutButton=Button(self,text="About",command=self.About)
        AboutButton.place(anchor=CENTER,x=200,y=250)
        
        MyMenu=Menu(self.master)
        self.master.config(menu=MyMenu)
        
        file=Menu(MyMenu,tearoff=False)
        MySave=Menu(MyMenu,tearoff=False)
        MySave.add_radiobutton(label="...as PNG",state='disabled',command=self.ASPNG)
        MySave.add_radiobutton(label="...as GIF",state='disabled',command=self.ASGIF)
        MySave.add_separator()
        MySave.add_radiobutton(label="Don't save",command=self.dontsave)
        file.add_cascade(label="Save...",menu=MySave)
        MySave.invoke(4)
        MyMenu.add_cascade(label="File",menu=file)
        
        self.tkvar=StringVar(self)
        self.pilihan=['Lindenmayer','Batik','Box','Koch','Ring','Sierpinski']
        self.tkvar.set('Lindenmayer')
        popupMenu=OptionMenu(self,self.tkvar,*self.pilihan)
        popupMenu.config(width=10)
        Label(self,text="Pilih Fraktal").place(anchor=CENTER,x=125,y=95)
        popupMenu.place(anchor=CENTER,x=125,y=120)
        self.tkvar.trace('w',self.pilihopsi)
        
        self.tkvar1=StringVar(self)
        jumlahiter=Entry(self,textvariable=self.tkvar1)
        self.tkvar1.set('0')
        jumlahiter.config(width=8)
        jumlahiter.place(anchor=CENTER,x=275,y=120)
        Label(self,text="Banyaknya iterasi:").place(anchor=CENTER,x=275,y=95)
        UpButton=Button(self,text="▴",command=self.UPNUM)
        UpButton.place(relheight=0.04,anchor=SW,x=310,y=120)
        DownButton=Button(self,text="▾",command=self.DOWNNUM)
        DownButton.place(relheight=0.04,anchor=NW,x=310,y=120)
        
        GOButton=Button(self,text="Go",command=self.GOFraktal)
        GOButton.place(anchor=CENTER,x=200,y=170)
        
        self.master.bind('<Return>',self.EnterGO)
        self.master.bind('<Up>',self.UPKEY)
        self.master.bind('<Down>',self.DOWNKEY)
        self.master.bind('<Right>',self.RIGHTKEY)
        self.master.bind('<Left>',self.LEFTKEY)
        
    def RIGHTKEY(self,event):
        if self.pilihan.index(self.tkvar.get())+1<len(self.pilihan):
            tmp=self.pilihan.index(self.tkvar.get())+1
            self.tkvar.set(self.pilihan[tmp])
            
    def LEFTKEY(self,event):
        if self.pilihan.index(self.tkvar.get())-1>=0:
            tmp=self.pilihan.index(self.tkvar.get())-1
            self.tkvar.set(self.pilihan[tmp])    

    def UPKEY(self,event):
        self.UPNUM()
        
    def DOWNKEY(self,event):
        self.DOWNNUM()
        
    def EnterGO(self,event):
        self.GOFraktal()
        
    def GOFraktal(self):
        self.tkvar1.set(str(int(eval(self.tkvar1.get()))))
        if eval(self.tkvar1.get())<0:
            self.tkvar1.set('0')
            root2=Tk()
            root2.geometry("300x50")
            root2.resizable(False,False)
            app2=CautionWindow(root2)
            winsound.PlaySound('SystemAsterisk',winsound.SND_ALIAS|winsound.SND_ASYNC)
            app2.mainloop()
        elif self.tkvar.get()==self.pilihan[0]:
            Lindenmayer(eval(self.tkvar1.get()))
        elif self.tkvar.get()==self.pilihan[1]:
            Batik(eval(self.tkvar1.get()))
        elif self.tkvar.get()==self.pilihan[2]:
            Box(eval(self.tkvar1.get()))
        elif self.tkvar.get()==self.pilihan[3]:
            Koch(eval(self.tkvar1.get()))
        elif self.tkvar.get()==self.pilihan[4]:
            Ring(eval(self.tkvar1.get()))
        else:
            Sierpinski(eval(self.tkvar1.get()))
    
    def UPNUM(self):
        self.tkvar1.set(str(eval(self.tkvar1.get())+1))
        
    def DOWNNUM(self):
        if eval(self.tkvar1.get())-1>=0:
            self.tkvar1.set(str(eval(self.tkvar1.get())-1))
        else:
            self.tkvar1.set('0')
        
    def pilihopsi(self,*args):
        self.tkvar.get()
            
    def About(self):
        root1=Tk()
        root1.geometry("300x50")
        root1.resizable(False,False)
        app1=AboutWindow(root1)
        app1.mainloop()
       
    def dontsave(self):
        self.opsisave=0
        
    def ASPNG(self):
        self.opsisave=1
        
    def ASGIF(self):
        self.opsisave=2