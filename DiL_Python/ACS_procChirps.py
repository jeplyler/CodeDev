# -*- coding: utf-8 -*-
"""
Created on Wed Nov 04 11:22:45 2015

@author: User
"""
import numpy as np
from scipy import io
#from Tkinter import *
import Tkinter as tk
from tkFileDialog import askopenfilenames
import ACS_Plots as aplots
import pySpec as spec


rt=tk.Tk()
rt.withdraw()

def getFname():
    name= askopenfilenames()
    return name

def getData(fn):

    
    dout={}    
    cnames=[]
    raw=io.loadmat(fn).items()[0][1]
    dchans=len(raw[1])
    cmap=open(fn.replace('.mat','.m')).read().split(';')

    for c in cmap:
        cnames.append(c.split('=')[0][1:-1])
    
    for c in range(3,dchans+3):
        dout[cnames[c]]=raw[:,c-3]
    return cnames ,dout

def findDemand(dem,dat_in):
    drv=[]
    for d in dem:
        drv.append(np.std(dat_in[d]))
    D=drv.index(max(drv))    
    return D

def getScaledChirpData(rsp_in):
    rgain=[9.81,9.81,9.81,1,1,1]
    ros=[0,0,-1,0,0,0]
    rdat=rgain[rsp.index(r)]*(rsp_in+ros[rsp.index(r)])
    return rdat

def anaChirp():

    fn=getFname()[0]
    
    dem=['axDem','ayDem','azDem','ratePitchDem','rateRollDem','rateYawDem']
    rsp=['IMU_gX','IMU_gY','IMU_gZ','IMU_wY','IMU_wX','IMU_wZ']
    
    chans,cdata=getData(fn)
    dChan=findDemand(dem,cdata)
    ddat=cdata[dem[dChan]]
    #ddat=cdata[dem[1]]
#    figs=[]
    fig1=aplots.Config(2,3,0)
    ax1=fig1.get_axes()   
    fig2=aplots.Config(2,3,1)
    ax2=fig2.get_axes()
    pspec='b-'
    
#    results={}
      
    for r in rsp:
        p_no=rsp.index(r)
        rdat=getScaledChirpData(cdata[r])
    
        txy,phase,f=spec.pyTF(ddat[:-15],rdat[15:],1000,4000)    
        
        
        aplots.UpdateLinePlots(ax1[p_no],f,txy,r,pspec,'off')
        ax1[p_no].axis([0.5, 30,-25,25])
        ax1[p_no].axhspan(-3,3,facecolor='.5',alpha=.5)
        aplots.UpdateLinePlots(ax2[p_no],f,phase,r,pspec,'off')
        ax2[p_no].axis([.5, 30,-200,100])    