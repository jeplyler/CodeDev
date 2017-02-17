# pySpec.py

from matplotlib import mlab
import numpy as np

def pyASD(data_in,fs,nfft):
    pxx,freq=mlab.psd(data_in,NFFT=nfft,Fs=fs)
    return pxx,freq
 
def pyCSD(xin,yin,fs,nfft):
    pxy,freq=mlab.csd(xin,yin,NFFT=nfft,Fs=fs)
    
    return pxy,freq
     
def pyCOH(xin,yin,fs,nfft):
    coh,freq=mlab.cohere(xin,yin,NFFT=nfft,Fs=fs)
    return coh,freq

def pyTF(xin,yin,fs,nfft):
    pxx,f=pyASD(xin,fs,nfft)
    pxy,f=pyCSD(xin,yin,fs,nfft)    
    tfe=20*np.log10(abs(pxy/pxx))
    p1=np.angle(pxy/pxx)
    phase=np.unwrap(p1,discont=np.pi)
    return tfe,(180/np.pi)*(phase-phase[2]),f