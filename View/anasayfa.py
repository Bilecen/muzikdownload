# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sayfatasarim.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!
import sys
from tkinter import messagebox

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QApplication, QMessageBox

from Entity.GenericEntity import MuzikEntity, MuzikListE
from Kural import Sorgular
from Controller.AnasayfaController import videoEkle
from View import uyari
from View.uyari import Ui_musicwarning


class Ui_anasayfa(object):

    def setupUi(self, anasayfa):
        anasayfa.setObjectName("anasayfa")
        anasayfa.resize(813, 505)
        anasayfa.setFixedSize(813, 505)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(anasayfa.sizePolicy().hasHeightForWidth())
        anasayfa.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            "D:/Yedekler/Yedek/PycharmProjects/ferganiorts/media/WhatsApp_Image_2018-09-25_at_00.40.27.jpeg"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        anasayfa.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(anasayfa)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 791, 451))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_listetemizle = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_listetemizle.setObjectName("btn_listetemizle")
        self.gridLayout.addWidget(self.btn_listetemizle, 6, 2, 1, 1)
        self.txt_videoismi = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txt_videoismi.setStyleSheet("font: 16pt \"Arial\";")
        self.txt_videoismi.setObjectName("txt_videoismi")
        self.gridLayout.addWidget(self.txt_videoismi, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setStyleSheet("font: 14pt \"Arial\";")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.btn_videogoster = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_videogoster.sizePolicy().hasHeightForWidth())
        self.btn_videogoster.setSizePolicy(sizePolicy)
        self.btn_videogoster.setMaximumSize(QtCore.QSize(16777215, 100))
        self.btn_videogoster.setObjectName("btn_videogoster")
        self.gridLayout.addWidget(self.btn_videogoster, 3, 0, 1, 3)
        self.txt_videourl = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txt_videourl.setSizeIncrement(QtCore.QSize(0, 0))
        self.txt_videourl.setStyleSheet("font: 16pt \"Arial\";\n"
                                        "")
        self.txt_videourl.setObjectName("txt_videourl")
        self.gridLayout.addWidget(self.txt_videourl, 1, 1, 1, 1)
        self.btn_videoekle = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_videoekle.sizePolicy().hasHeightForWidth())
        self.btn_videoekle.setSizePolicy(sizePolicy)
        self.btn_videoekle.setMaximumSize(QtCore.QSize(16777215, 150))
        self.btn_videoekle.setObjectName("btn_videoekle")
        self.gridLayout.addWidget(self.btn_videoekle, 0, 2, 2, 1)
        self.listView = QtWidgets.QListView(self.gridLayoutWidget)
        self.listView.setObjectName("listView")
        self.gridLayout.addWidget(self.listView, 6, 0, 4, 2)
        self.btn_listeyiindir = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(15)
        sizePolicy.setVerticalStretch(45)
        sizePolicy.setHeightForWidth(self.btn_listeyiindir.sizePolicy().hasHeightForWidth())
        self.btn_listeyiindir.setSizePolicy(sizePolicy)
        self.btn_listeyiindir.setMaximumSize(QtCore.QSize(150, 150))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_listeyiindir.setFont(font)
        self.btn_listeyiindir.setAutoFillBackground(True)
        self.btn_listeyiindir.setObjectName("btn_listeyiindir")
        self.gridLayout.addWidget(self.btn_listeyiindir, 8, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 14pt \"Arial\";")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 5, 0, 1, 3)
        self.btn_videompcevir = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_videompcevir.sizePolicy().hasHeightForWidth())
        self.btn_videompcevir.setSizePolicy(sizePolicy)
        self.btn_videompcevir.setMaximumSize(QtCore.QSize(16777215, 100))
        self.btn_videompcevir.setObjectName("btn_videompcevir")
        self.gridLayout.addWidget(self.btn_videompcevir, 2, 0, 1, 3)
        self.btn_gecmismpler = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_gecmismpler.sizePolicy().hasHeightForWidth())
        self.btn_gecmismpler.setSizePolicy(sizePolicy)
        self.btn_gecmismpler.setMaximumSize(QtCore.QSize(16777215, 100))
        self.btn_gecmismpler.setObjectName("btn_gecmismpler")
        self.gridLayout.addWidget(self.btn_gecmismpler, 4, 0, 1, 3)
        anasayfa.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(anasayfa)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 813, 26))
        self.menubar.setObjectName("menubar")
        anasayfa.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(anasayfa)
        self.statusbar.setObjectName("statusbar")
        anasayfa.setStatusBar(self.statusbar)
        self.retranslateUi(anasayfa)
        self.btn_videoekle.clicked.connect(self.bt_videoEkle)
        self.model = QStandardItemModel(self.listView)
        self.items = []

        QtCore.QMetaObject.connectSlotsByName(anasayfa)

        self.islem()

    def bt_videoEkle(self):
        try:
            videoEkle(self.txt_videoismi.text() , self.txt_videourl.text())
            # if not self.txt_videourl.text() is "" and not self.txt_videoismi.text() is "":
            #     print(self.txt_videourl.text() + " " + self.txt_videoismi.text())
            #     mz = MuzikListE(self.txt_videoismi.text(), self.txt_videourl.text())
            #     self.items.append(mz)
            #     item = QStandardItem(self.items)
            #     item.setCheckable(True)
            #     self.model.appendRow(item)
            # else:
            #     alert = QMessageBox()
            #     alert.setWindowTitle("Dikkat")
            #     alert.setText('Lütfen Url ve İsmi doldurunuz...')
            #     alert.setIcon(QMessageBox.Warning)
            #     alert.setDefaultButton(QMessageBox.Ok)
            #     alert.show()
            #     alert.exec_()
        except Exception as e:
            print(e)

    def sorgu(self, i):
        # print(i == QMessageBox.Ok)
        if i:
            self.btn_listeyiindir.setDisabled(True)
            self.txt_videoismi.setDisabled(True)
            self.txt_videourl.setDisabled(True)
            self.btn_listetemizle.setDisabled(True)
            self.btn_videoekle.setDisabled(True)
            self.listView.setDisabled(True)
        else:
            sys.exit(0)

    def islem(self):
        a = Sorgular.internetVar_mi()
        if not a:
            alert = QMessageBox()
            alert.setWindowTitle("Uyari")
            alert.setText('Lütfen İnternet Bağlantısını Kontrol Ediniz...')
            alert.setIcon(QMessageBox.Information)
            btncevrimdisi = alert.addButton("Çevrim Dışı Çalış", QMessageBox.ActionRole)
            btncikis = alert.addButton("Çıkış", QMessageBox.ActionRole)
            # alert.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            alert.show()
            btnclick = alert.exec_()
            if alert.clickedButton() == btncevrimdisi:
                self.sorgu(True)
            else:
                self.sorgu(False)

            # u = QtWidgets.QDialog()
            # alert = Ui_musicwarning("Uyari", "Lütfen İnternet Bağlantınızı Kontrol Ediniz...", None)
            # alert.setupUi(u)
            # u.exec_()
            # u.show()

        else:
            self.btn_listeyiindir.setDisabled(False)
            self.txt_videoismi.setDisabled(False)
            self.txt_videourl.setDisabled(False)
            self.btn_listetemizle.setDisabled(False)
            self.btn_videoekle.setDisabled(False)

    def retranslateUi(self, anasayfa):
        _translate = QtCore.QCoreApplication.translate
        anasayfa.setWindowTitle(_translate("anasayfa", "Müzik Arşivi"))
        self.btn_listetemizle.setText(_translate("anasayfa", "Listeyi Temizle"))
        self.label_2.setText(_translate("anasayfa", "Video Url: "))
        self.btn_videogoster.setText(_translate("anasayfa", "Geçmiş Videoları Göster"))
        self.btn_videoekle.setText(_translate("anasayfa", "Video Ekle"))
        self.btn_listeyiindir.setText(_translate("anasayfa", "Listeyi İndir"))
        self.label.setText(_translate("anasayfa", "Video İsmi: "))
        self.btn_videompcevir.setText(_translate("anasayfa", "Videoları MP3 Çevir"))
        self.btn_gecmismpler.setText(_translate("anasayfa", "Geçmiş Müzileri Göster"))


@Sorgular.anaIslem
# @Sorgular.internetVar_mi
def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    anasayfa = QtWidgets.QMainWindow()
    ui = Ui_anasayfa()
    ui.setupUi(anasayfa)
    anasayfa.show()
    sys.exit(app.exec_())
