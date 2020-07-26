# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ocrOriginalPreview.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
import os
import sys
import psutil
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import filedialog
from PIL import Image,ImageTk
from textblob import TextBlob
import numpy as np

from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = "Tesseract-OCR\\tesseract.exe"#env variable
from textblob import TextBlob
import cv2

class Ui_PIC2TEXT(object):
    langOcr="English"
    d1={'English':'eng','Hindi':'hin','Tamil':'tam','Telugu':'tel','Urdu':'urd'}
    d2={'English':'en','Hindi':'hi','Tamil':'ta','Telugu':'te','Urdu':'ur'}
    def setupUi(self, PIC2TEXT):

        PIC2TEXT.setObjectName("PIC2TEXT")
        PIC2TEXT.setWindowModality(QtCore.Qt.ApplicationModal)
        PIC2TEXT.resize(1471, 694)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ICONS/LOGO.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        PIC2TEXT.setWindowIcon(icon)
        PIC2TEXT.setWindowOpacity(9.0)
        PIC2TEXT.setToolTip("")
        self.centralwidget = QtWidgets.QWidget(PIC2TEXT)
        self.centralwidget.setObjectName("centralwidget")
        self.conv = QtWidgets.QPushButton(self.centralwidget)
        self.conv.setGeometry(QtCore.QRect(890, 630, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Demi")
        font.setPointSize(26)
        self.conv.setFont(font)
        self.conv.setObjectName("conv")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(610, 630, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(22)
        self.comboBox.setFont(font)
        self.comboBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(240, 640, 351, 31))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Demi")
        font.setPointSize(26)
        self.label_2.setFont(font)
        self.label_2.setToolTipDuration(-2)
        self.label_2.setObjectName("label_2")
        self.originalpreview = QtWidgets.QLabel(self.centralwidget)
        self.originalpreview.setGeometry(QtCore.QRect(10, 10, 1341, 601))
        self.originalpreview.setAutoFillBackground(True)
        self.originalpreview.setFrameShape(QtWidgets.QFrame.Box)
        self.originalpreview.setFrameShadow(QtWidgets.QFrame.Raised)
        self.originalpreview.setText("")
        self.originalpreview.setObjectName("originalpreview")
        PIC2TEXT.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(PIC2TEXT)
        self.statusbar.setObjectName("statusbar")
        PIC2TEXT.setStatusBar(self.statusbar)

        self.retranslateUi(PIC2TEXT)
        QtCore.QMetaObject.connectSlotsByName(PIC2TEXT)

    def retranslateUi(self, PIC2TEXT):
        _translate = QtCore.QCoreApplication.translate
        PIC2TEXT.setWindowTitle(_translate("PIC2TEXT", "PIC2TEXT"))
        self.conv.setToolTip(_translate("PIC2TEXT", "Click to run "))
        self.conv.setText(_translate("PIC2TEXT", "CONVERT"))
        #self.conv.
        self.comboBox.setToolTip(_translate("PIC2TEXT", "Select language of the image file"))
        self.comboBox.setItemText(0, _translate("PIC2TEXT", "English"))
        self.comboBox.setItemText(1, _translate("PIC2TEXT", "Hindi"))
        self.comboBox.setItemText(2, _translate("PIC2TEXT", "Tamil"))
        self.comboBox.setItemText(3, _translate("PIC2TEXT", "Telugu"))
        self.comboBox.setItemText(4, _translate("PIC2TEXT", "Urdu"))

        self.comboBox.currentIndexChanged.connect(self.selectionchange)
        #a.lang=self.comboBox.setText(self.dialog.comboBox.currentText())

        self.label_2.setToolTip(_translate("PIC2TEXT", "Select document langauge type"))
        self.label_2.setText(_translate("PIC2TEXT", "SELECT LANGUAGE"))
         
        self.conv.clicked.connect(self.ocrCall)
    
        pixmap = QPixmap('cropped.jpeg')
        self.originalpreview.setPixmap(pixmap)
       
        self.originalpreview.resize(pixmap.width(),pixmap.height())
        
    def selectionchange(self):
        Ui_PIC2TEXT.langOcr=self.comboBox.itemText(self.comboBox.currentIndex())
        print(Ui_PIC2TEXT.langOcr)


    def ocrCall(self):
        self.performOcr()

        os.system("python ocrOutput.py")

        #os.wait()
       # dirpath = "["+'os.getcwd()+"\\ocrOutput.py"'+"]"
        #app1 = QtWidgets.QApplication("['C:\\Users\\sanke\\Desktop\\ourcode\\Main\\ocrOutput.py']")
        #PIC2TEXT = QtWidgets.QMainWindow()
        #ui = Ui_PIC2TEXT()
        #ui.setupUi(PIC2TEXT)
        #PIC2TEXT.show()
        #sys.exit(app.exec_())
        #print("reac")
        #wait

        #self.close()
        
        #for pid in (process.pid for process in psutil.process_iter() if process.name()=="ocrOriginalPrev.py"):
          #  os.kill(pid)



        #sys.exit(0)


    def performOcr(self):
        originalImage = cv2.imread("cropped.jpeg")
        #grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
        #blackAndWhiteImage=cv2.adaptiveThreshold(grayImage, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 10)

        #preprocessing
        os.system("python preprocess.py")



        #cv2.imwrite("cropped.jpeg",blackAndWhiteImage)
        
       
        #here upto
        #grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
  
        #(thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)
        #originalImage = cv2.imread('original.jpeg')
        grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
  
#(thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)
        

#cv2.imshow('Output', out)
        
        #cv2.imwrite('spotless.jpeg', out)
        #cv2.imwrite("cropped.jpeg",out)#changed
        self.img=cv2.imread("cropped.jpeg")
        print(Ui_PIC2TEXT.langOcr)
        self.d1={'English':'eng','Hindi':'hin','Tamil':'tam','Telugu':'tel','Urdu':'urd'}
        self.d2={'English':'en','Hindi':'hi','Tamil':'ta','Telugu':'te','Urdu':'ur'}
        ocrln=self.d1[Ui_PIC2TEXT.langOcr]
        self.text=""
        if ocrln!='e':
            self.text=pytesseract.image_to_string(Image.open("cropped.jpeg"),lang=ocrln)
            file1 = open("textCon.txt","w",encoding='utf-16')
            file1.write(self.text)
        #bytes(theWord.encode('utf-8'))
        #file1.write(bytes((self.text).encode('utf-8'))) 
       # theWord=self.text
      #  theWord = theWord.decode('utf-8').encode('utf-8')
        else:
            self.text=pytesseract.image_to_string(Image.open("cropped.jpeg"),lang=ocrln)
            root = tk.Tk()
            T = tk.Text(root, height=100, width=100)
            T.pack()
            T.insert(tk.END, self.text)
            tk.mainloop()
            #sys.exit()
            





      


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PIC2TEXT = QtWidgets.QMainWindow()
    ui = Ui_PIC2TEXT()
    ui.setupUi(PIC2TEXT)
    PIC2TEXT.show()
    sys.exit(app.exec_())
