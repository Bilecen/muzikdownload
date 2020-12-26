# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uyari.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_musicwarning(object):

    def __init__(self, tittle, uyari , func1):
        self.tittle = tittle
        self.uyari = uyari
        self.func1 = func1


    def setupUi(self, musicwarning):
        musicwarning.setObjectName("musicwarning")
        musicwarning.resize(439, 295)

        self.btn_islemler = QtWidgets.QDialogButtonBox(musicwarning)
        self.btn_islemler.setGeometry(QtCore.QRect(60, 200, 341, 32))
        self.btn_islemler.setOrientation(QtCore.Qt.Horizontal)
        self.btn_islemler.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.btn_islemler.setObjectName("btn_islemler")
        self.txt_uyari = QtWidgets.QLabel(musicwarning)
        self.txt_uyari.setGeometry(QtCore.QRect(40, 70, 341, 81))
        self.txt_uyari.setStyleSheet("font: 18pt \"Arial\";")
        self.txt_uyari.setObjectName("txt_uyari")
        self.txt_uyari.setTextFormat(QtCore.Qt.PlainText)
        self.txt_uyari.setWordWrap(True)

        self.retranslateUi(musicwarning)
        self.btn_islemler.accepted.connect(self.islem)
        self.btn_islemler.rejected.connect(self.islem)
        QtCore.QMetaObject.connectSlotsByName(musicwarning)
    def islem(self):
        print("asdasd")

    def retranslateUi(self, musicwarning):
        _translate = QtCore.QCoreApplication.translate
        musicwarning.setWindowTitle(_translate("musicwarning", self.tittle))
        self.txt_uyari.setText(_translate("musicwarning", self.uyari))
