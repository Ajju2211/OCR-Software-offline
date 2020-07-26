# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ocrOutput.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image,ImageTk
import cv2
from tkinter import *

import tkinter


from PIL import Image
import pytesseract

class Ui_PIC2TEXT(object):
   
   
    
    def setupUi(self, PIC2TEXT):
        PIC2TEXT.setObjectName("PIC2TEXT")
        PIC2TEXT.setWindowModality(QtCore.Qt.ApplicationModal)
        PIC2TEXT.resize(1471, 697)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(240, 19, 49))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 44, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 19, 49))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 44, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 19, 49))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 44, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        PIC2TEXT.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ICONS/LOGO.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        PIC2TEXT.setWindowIcon(icon)
        PIC2TEXT.setWindowOpacity(9.0)
        PIC2TEXT.setToolTip("")
        self.centralwidget = QtWidgets.QWidget(PIC2TEXT)
        self.centralwidget.setObjectName("centralwidget")
        self.downloadB = QtWidgets.QPushButton(self.centralwidget)
        self.downloadB.setGeometry(QtCore.QRect(1020, 590, 241, 91))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(22, 22, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        self.downloadB.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Demi")
        font.setPointSize(26)
        self.downloadB.setFont(font)
        self.downloadB.setInputMethodHints(QtCore.Qt.ImhNone)
        self.downloadB.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("ICONS/DOWNLOAD.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.downloadB.setIcon(icon1)
        self.downloadB.setIconSize(QtCore.QSize(201, 80))
        self.downloadB.setCheckable(False)
        self.downloadB.setDefault(False)
        self.downloadB.setFlat(False)
        self.downloadB.setObjectName("downloadB")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(20, 10, 1331, 561))
        self.plainTextEdit.setInputMethodHints(QtCore.Qt.ImhMultiLine)
        self.plainTextEdit.setObjectName("plainTextEdit")
        

        self.message = QtWidgets.QLabel(self.centralwidget)
        self.message.setGeometry(QtCore.QRect(180, 620, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Poor Richard")
        font.setPointSize(24)
        self.message.setFont(font)
        self.message.setObjectName("message")
        PIC2TEXT.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(PIC2TEXT)
        self.statusbar.setObjectName("statusbar")
        PIC2TEXT.setStatusBar(self.statusbar)

        self.retranslateUi(PIC2TEXT)
        QtCore.QMetaObject.connectSlotsByName(PIC2TEXT)

    def retranslateUi(self, PIC2TEXT):
        _translate = QtCore.QCoreApplication.translate
        PIC2TEXT.setWindowTitle(_translate("PIC2TEXT", "PIC2TEXT"))
        self.downloadB.setToolTip(_translate("PIC2TEXT", "<html><head/><body><p>click to convert </p><p>file to text</p></body></html>"))
        self.message.setText(_translate("PIC2TEXT", "Loading......"))
        file1=open("textCon.txt",'r',encoding='utf-16')
        data=""
        para=file1.readlines()
        for word in para:
        	data=data+word
        file1.close()

        self.plainTextEdit.setPlainText(data)
        self.message.setText(_translate("PIC2TEXT", "Ready to Download"))
        self.downloadB.clicked.connect(self.downloadFile)
    def downloadFile(self):
        filename =  filedialog.asksaveasfilename(initialdir = "Documents\\",title = "Download file",filetypes = (("text files","*.txt"),("all files","*.*")))
        file2=open(filename+".txt",'w')
        file1=open("textCon.txt",'r')
        data=""
        para=file1.readlines()
        for word in para:
            data=data+word

        file2.write(data)
        file2.close()
        file1.close()
        sys.exit(0)



 
    
       

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    print(sys.argv)
    PIC2TEXT = QtWidgets.QMainWindow()
    ui = Ui_PIC2TEXT()
    ui.setupUi(PIC2TEXT)
    PIC2TEXT.show()
    sys.exit(app.exec_())
