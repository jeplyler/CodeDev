# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 14:32:22 2017

@author: jplyler
"""

import GrediUtils as g
import pandas as pd

def configChirps():
    raw_data=g.getGrediDF("D:/DiL/DiL_Performance/ChirpPerformanceData/20170113 IndyCar 6236 update/Heave.mat")
    dem=['axDem','ayDem','azDem','ratePitchDem','rateRollDem','rateYawDem']
    rsp=['IMU_gX','IMU_gY','IMU_gZ','IMU_wY','IMU_wX','IMU_wZ']
    chirps=raw_data[rsp]
    scaleChirps()
    
def scaleChirps():
    rgain=[9.81,9.81,9.81,1,1,1]
    ros=[0,0,-1,0,0,0]
    for r in range(len(rsp)):
        chirps[rsp[r]]=chirps[rsp[r]].apply(lambda x: rgain[r]*(x+ros[r]))

def findDemand():
    dchan=chirps.ix[:,0:6].describe().iloc[2].idxmax()
    ddat=chirps[dchan].values.flatten()

def calcChirps():
    mags=pd.DataFrame()
    ph=pd.DataFrame()
    for r in reversed(rsp):
        rdat=chirps[r].values.flatten()
        tfe,p,f=g.spec.pyTF(ddat,rdat,1000,4000)
        mags.insert(0,r,tfe)
    mags.insert(0,'freq',f)
    return mags
        
def main():
    global m
    configChirps()
    findDemand()
    m=calcChirps()
    m.plot(y='IMU_gZ')
    
if __name__=='__main__':
    main()