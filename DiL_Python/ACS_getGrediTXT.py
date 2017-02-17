# -*- coding: utf-8 -*-
"""
Created on Wed Jul 06 16:17:46 2016

@author: User
"""

import numpy as np
from scipy import io
import Tkinter as tk
from tkFileDialog import askopenfilenames
import ACS_Plots as aplots
import pySpec as spec

rt=tk.Tk()
rt.withdraw()

def getFname():
    name= askopenfilenames()
    return name
#fname=getFname()

#f=open(fname[0],'r')
#chans=f.readline().split('\t')
#f.readline()
#units=f.readline().split('\t')
#f.close()
#data=np.genfromtxt(fname[0],skip_header=3)

fig1=aplots.Config(2,2,0)
ax1=fig1.get_axes()   

pspec='r-'

aplots.UpdateLinePlots(ax1[p_no],f,txy,r,pspec,'off')
    
aplots.UpdateLinePlots(ax1[0],)
ax1[p_no].axis([0.5, 30,-25,25])
ax1[p_no].axhspan(-3,3,facecolor='.5',alpha=.5)
