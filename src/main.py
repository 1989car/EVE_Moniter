#! /usr/bin/python

'''
   File      : screenCenter.pyw
   Author    : Mike
   E-Mail    : Mike_Zhang@live.com
'''
from Tkinter import *
 
rt = Tk()
rt.resizable(False,False)
rt.title("Screen center") 
 
rt.update() # update window ,must do
curWidth = rt.winfo_reqwidth() # get current width
curHeight = rt.winfo_height() # get current height
scnWidth,scnHeight = rt.maxsize() # get screen width and height
 
tmpcnf = '%dx%d+%d+%d'%(curWidth,curHeight,
(scnWidth-curWidth)/2,(scnHeight-curHeight)/2)
rt.geometry(tmpcnf)
rt.mainloop()
