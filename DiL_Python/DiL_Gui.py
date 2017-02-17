# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testGui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):

#added comment here
#added another comment for git test


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(349, 161)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(250, 10, 41, 61))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(80, 10, 91, 131))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout.addWidget(self.comboBox)
        self.edit_ChirpF0 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.edit_ChirpF0.setObjectName("edit_ChirpF0")
        self.verticalLayout.addWidget(self.edit_ChirpF0)
        self.edit_ChirpF1 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.edit_ChirpF1.setObjectName("edit_ChirpF1")
        self.verticalLayout.addWidget(self.edit_ChirpF1)
        self.edit_ChirpTime = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.edit_ChirpTime.setObjectName("edit_ChirpTime")
        self.verticalLayout.addWidget(self.edit_ChirpTime)
        self.edit_ChirpAmp = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.edit_ChirpAmp.setObjectName("edit_ChirpAmp")
        self.verticalLayout.addWidget(self.edit_ChirpAmp)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 9, 61, 131))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.lab_ChirpF0 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.lab_ChirpF0.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lab_ChirpF0.setObjectName("lab_ChirpF0")
        self.verticalLayout_2.addWidget(self.lab_ChirpF0)
        self.lab_ChirpF1 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.lab_ChirpF1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lab_ChirpF1.setObjectName("lab_ChirpF1")
        self.verticalLayout_2.addWidget(self.lab_ChirpF1)
        self.lab_ChirpTime = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.lab_ChirpTime.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lab_ChirpTime.setObjectName("lab_ChirpTime")
        self.verticalLayout_2.addWidget(self.lab_ChirpTime)
        self.lab_ChirpAmp = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.lab_ChirpAmp.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lab_ChirpAmp.setObjectName("lab_ChirpAmp")
        self.verticalLayout_2.addWidget(self.lab_ChirpAmp)
        self.bGenFile = QtWidgets.QPushButton(Dialog)
        self.bGenFile.setGeometry(QtCore.QRect(170, 10, 75, 23))
        self.bGenFile.setObjectName("bGenFile")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Cool DiL Stuff"))
        self.comboBox.setItemText(0, _translate("Dialog", "Surge"))
        self.comboBox.setItemText(1, _translate("Dialog", "Sway"))
        self.comboBox.setItemText(2, _translate("Dialog", "Heave"))
        self.comboBox.setItemText(3, _translate("Dialog", "Pitch"))
        self.comboBox.setItemText(4, _translate("Dialog", "Roll"))
        self.comboBox.setItemText(5, _translate("Dialog", "Yaw"))
        self.lab_ChirpF0.setText(_translate("Dialog", "Chirp F0"))
        self.lab_ChirpF1.setText(_translate("Dialog", "Chirp F1"))
        self.lab_ChirpTime.setText(_translate("Dialog", "Chirp Time"))
        self.lab_ChirpAmp.setText(_translate("Dialog", "Chirp Amp"))
        self.bGenFile.setText(_translate("Dialog", "Create Drive"))

