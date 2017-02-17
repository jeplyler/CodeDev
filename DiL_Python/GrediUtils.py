# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 14:33:00 2017

@author: jplyler
"""

import pandas as pd
from scipy import io
from Tkinter import Tk
from tkFileDialog import askopenfilename
import pySpec as spec
from matplotlib import mlab

def getFname():
    bw=Tk()
    bw.attributes("-topmost",True)
    bw.withdraw()
    fname=askopenfilename()
    bw.destroy()
    return fname    

def getGrediDF(fin):
    dfout=pd.DataFrame()    
    cnames=[]
    raw=io.loadmat(fin).items()[0][1]
    dchans=len(raw[1])
    cmap=open(fin.replace('.mat','.m')).read().split(';')
    for c in cmap:
        cnames.append(c.split('=')[0][1:-1])
        
    for c in range(3,dchans+3):
        
        dfout.insert(0,cnames[c],raw[:,c-3])
    
    return dfout.set_index(['\nTimestamp'],drop=True,)

def findDemand(dem,dat_in):
    drv=[]
    for d in dem:
        drv.append(np.std(dat_in[d]))
    D=drv.index(max(drv))    
    return D

def scale(dfin,c,g,o):   
    return dfin[c].apply(lambda x: g*(x+o))    

def getChirpData(gdat):
    return gdat[['axDem','ayDem','azDem','rateRollDem','ratePitchDem','rateYawDem','IMU_gX','IMU_gY','IMU_gZ','IMU_wX','IMU_wY','IMU_wZ']]

def PSD(dat,Fs,nfft):
    p,f=spec.pyASD(dat,Fs,nfft)
    return pd.DataFrame({"freq":f,"pxx":p},index=f)
    