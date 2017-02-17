# -*- coding: utf-8 -*-
"""
Created on Mon Jan 09 17:10:38 2017

@author: jplyler
"""

from PyQt5 import QtGui, QtWidgets
from DiL_Gui import Ui_Dialog
import sys
import os
import MakePhysicsOutput as physout

class win(Ui_Dialog):

    def __init__(self,dialog):
        Ui_Dialog.__init__(self)
        self.setupUi(dialog)
        self.bGenFile.clicked.connect(self.chirps)
        
    def chirps(self):
        physout.setF0(float(self.edit_ChirpF0.text()))
        physout.setF1(float(self.edit_ChirpF1.text()))
        physout.setT1(float(self.edit_ChirpTime.text()))
        physout.runChirps()
        
def main():        
    app=QtWidgets.QApplication(sys.argv)
    d=QtWidgets.QDialog()
    ui=Ui_Dialog()
    ui=win(d)
    d.show()
    sys.exit(app.exec_())
    
if __name__=='__main__':
    main()

    