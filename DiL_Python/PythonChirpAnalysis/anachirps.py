import pandas as pd
from scipy import io
from Tkinter import Tk
from tkFileDialog import askopenfilename
import pySpec as specs

class chirp:
    
    fname=''
    rawdata=pd.DataFrame()
    chirpdata=pd.DataFrame()
    mag=pd.DataFrame()
    ph=pd.DataFrame()
    rgain=[9.81,9.81,9.81,1,1,1]
    ros=[0,0,-1,0,0,0]
    dem=['axDem','ayDem','azDem','ratePitchDem','rateRollDem','rateYawDem']
    rsp=['IMU_gX','IMU_gY','IMU_gZ','IMU_wY','IMU_wX','IMU_wZ']
    dchan=''
    ddat=[]

    def __init__(self,name):
        self.name=name 
    
    def setFname(self):
        bw=Tk()
        bw.attributes("-topmost",True)
        bw.withdraw()
        self.fname=askopenfilename()
        bw.destroy()
    
    def setGrediDF(self):
        cnames=[]
        raw=io.loadmat(self.fname).items()[0][1]
        dchans=len(raw[1])
        cmap=open(self.fname.replace('.mat','.m')).read().split(';')
        for c in cmap:
            cnames.append(c.split('=')[0][1:-1])

        for c in range(3,dchans+3):
            try:
                self.rawdata.insert(0,cnames[c],raw[:,c-3])
            except:
                pass
                      
    def setChirpData(self):
        self.chirpdata=self.rawdata[self.dem+self.rsp]
                          
    def setDemChan(self):
        self.dchan=self.chirpdata.ix[:,0:6].describe().iloc[2].idxmax()
        self.ddat=self.chirpdata[self.dchan].values.flatten()
            
    def scaleChirps(self):
        for r in range(len(self.rsp)):
            self.chirpdata[self.rsp[r]]=self.chirpdata[self.rsp[r]].apply(lambda x: self.rgain[r]*(x+self.ros[r]))


    def calcChirps(self):
        for r in reversed(self.rsp):
            rdat=self.chirpdata[r].values.flatten()
            tfe,p,f=specs.pyTF(self.ddat,rdat,1000,4000)
            self.mag.insert(0,r,tfe)
        self.mag.insert(0,'freq',f)            