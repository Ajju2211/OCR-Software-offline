

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import  QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon
import os
import sys
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import cv2


class Ui_MainWindow(object):
    filename=""
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        font = QtGui.QFont()
        font.setPointSize(24)
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(True)
        MainWindow.setTabletTracking(True)
        MainWindow.setFocusPolicy(QtCore.Qt.ClickFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ICONS/LOGO.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(27.0)
        MainWindow.setToolTipDuration(-3)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.titleLab = QtWidgets.QLabel(self.centralwidget)
        self.titleLab.setGeometry(QtCore.QRect(120, 110, 411, 71))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(50)
        self.titleLab.setFont(font)
        self.titleLab.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.titleLab.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLab.setObjectName("titleLab")
        self.uploadB = QtWidgets.QPushButton(self.centralwidget)
        self.uploadB.setGeometry(QtCore.QRect(90, 270, 161, 81))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Demi")
        font.setPointSize(26)
        self.uploadB.setFont(font)
        self.uploadB.setAcceptDrops(False)
        self.uploadB.setAutoFillBackground(False)
        self.uploadB.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("ICONS/upload.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uploadB.setIcon(icon1)
        self.uploadB.setIconSize(QtCore.QSize(500, 62))
        self.uploadB.setObjectName("uploadB")
        self.cameraB = QtWidgets.QPushButton(self.centralwidget)
        self.cameraB.setGeometry(QtCore.QRect(360, 270, 171, 81))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Demi")
        font.setPointSize(26)
        self.cameraB.setFont(font)
        self.cameraB.setAcceptDrops(False)
        self.cameraB.setAutoFillBackground(False)
        self.cameraB.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("ICONS/iconfinder2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cameraB.setIcon(icon2)
        self.cameraB.setIconSize(QtCore.QSize(192, 192))
        self.cameraB.setAutoDefault(True)
        self.cameraB.setFlat(False)
        self.cameraB.setObjectName("cameraB")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PIC2TEXT"))
        MainWindow.setToolTip(_translate("MainWindow", "<html><head/><body><p>Upload Image File</p></body></html>"))
        self.titleLab.setToolTip(_translate("MainWindow", "<html><head/><body><p>Optical character Recogntion Application</p></body></html>"))
        self.titleLab.setText(_translate("MainWindow", "PIC2TEXT"))
        self.uploadB.setToolTip(_translate("MainWindow", "<html><head/><body><p>Upload an image file(*.jpeg /*.jpg)</p></body></html>"))
        self.uploadB.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>This is to upload a file</p></body></html>"))
        self.cameraB.setToolTip(_translate("MainWindow", "<html><head/><body><p>Upload an image file(*.jpeg /*.jpg)</p></body></html>"))
        self.cameraB.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>This is to upload a file</p></body></html>"))
        self.cameraB.clicked.connect(self.cameraCall)
        self.uploadB.clicked.connect(self.uploadCall)
    def cameraCall(self):
        os.system("python CamApp.py")
        sys.exit(0)
        #os.wait()

        #self.close()
    def uploadCall(self):
        Ui_MainWindow.filename=filedialog.askopenfilename(initialdir=".\\",title="Select An Image",filetype=(("jpeg",".jpeg"),("jpg",".jpg"),("png",".png"),("All Files","*.*")))

        
        img=cv2.imread(Ui_MainWindow.filename)
        
        cv2.imwrite("original.jpeg",img)
        os.system("python croppingmethodROI.py")
        #sys.exit(0)
      




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
