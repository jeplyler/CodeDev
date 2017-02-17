# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 11:12:14 2016

@author: jplyler
"""

import matplotlib.pyplot as plt
from scipy.signal import *
import pyASD as sig
import numpy as np

ddata=data1['rateYawDem']
rdata=data1['IMU_wZ']
fs=1000

