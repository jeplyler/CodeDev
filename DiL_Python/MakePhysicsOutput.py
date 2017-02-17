# -*- coding: utf-8 -*-
"""
Created on Fri Jan 06 10:30:21 2017

@author: jplyler
"""
import sys
from Tkinter import Tk
from tkFileDialog import askopenfilename
from PyQt5 import QtWidgets
from scipy import io
import numpy as np
from scipy.signal import chirp
from matplotlib import pyplot as plt
from collections import OrderedDict
import pandas as pd

class physout():
    def __init__(self,f0,f1,t1):
        self.f0=30
        self.f1=.5
        self.t1=180
        self.Fs=1000
        self.time=np.round(np.linspace(0,self.t1,self.t1*self.Fs),3)
        
    def setF0(self,f0):
        self.f0=f0
    	
    def setTime(self):
        self.time=np.round(np.linspace(0,self.t1,self.t1*self.Fs),3)
    	
    def sigGen(self):
        if (self.f0==self.f1):
            return 0.0*self.time
        else:
            return chirp(self.time,self.f0,self.f1,self.t1,method='linear')
    
    def writeOutput(dfout):
        with open('c:\phystest.csv','w+') as csvfile:
            csvfile.write("#1\n")
            csvfile.write("double tab1(" + str(len(dfout)+2)+ ", 12)\n")
            dfout.to_csv(csvfile,header=True, index=False)
            csvfile.write('1000.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0\n')
            csvfile.write('1000.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0')
    	print "Data File Wirtten Successfully..."
    		
    def runChirps(self):
        sigScales=OrderedDict()
        sigScales['m_vCar']=[0,0]
        sigScales['m_accVert']=[0,0]
        sigScales['m_accLat']=[.5,30]
        sigScales['m_accLong']=[0,0]
        sigScales['m_rateYaw']=[0,0]
        sigScales['m_ratePitch']=[0,0]
        sigScales['m_rateRoll']=[0,0]
        sigScales['m_accYaw']=[0,0]
        sigScales['m_accPitch']=[0,0]
        sigScales['m_accRoll']=[0,0]
        sigScales['physicsOutput_mSteering']=[0,0]
            
        sigData=pd.DataFrame()
    
        for s,v in reversed(sigScales.items()):
            sigData.insert(0,s,self.sigGen(v[0],v[1]))
        
        sigData.insert(0,'#Time',self.time)
        self.writeOutput(sigData)    
    
    def ramp_hold(self,rate,currval,nextval):
        if abs(nextval-currval)==0:
            steptime=self.Fs
        if abs(nextval-currval)>0:
            steptime=(nextval-currval)*self.Fs    
        return np.linspace(currval,nextval,steptime)
    
    def runStepHold(self):
        
        sigScales=OrderedDict()
        sigScales['m_vCar']=1
        sigScales['m_accVert']=0
        sigScales['m_accLat']=0
        sigScales['m_accLong']=0
        sigScales['m_rateYaw']=0
        sigScales['m_ratePitch']=0
        sigScales['m_rateRoll']=0
        sigScales['m_accYaw']=0
        sigScales['m_accPitch']=0
        sigScales['m_accRoll']=0
        sigScales['physicsOutput_mSteering']=0
    
        sigData=pd.DataFrame()
        
        dt=5
        vals=[0,0,1,1,2,2,3,3,4,4,5,5,0,0]
        time=np.arange(0,dt*len(vals),5)
        nosig=np.linspace(0,0,len(vals))
    
        for s,v in reversed(sigScales.items()):
            dat=nosig
            if v==1:
                dat=vals
            sigData.insert(0,s,dat)
        sigData.insert(0,'#Time',time)       
     #   plt.plot(time,vals)
      #  plt.show()
        self.writeOutput(sigData)
        
        return sigData