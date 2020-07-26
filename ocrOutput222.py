# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ocrOutput.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PIC2TEXT(object):
    def setupUi(self, PIC2TEXT):
        PIC2TEXT.setObjectName("PIC2TEXT")
        PIC2TEXT.setWindowModality(QtCore.Qt.ApplicationModal)
        PIC2TEXT.resize(1471, 697)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ICONS/LOGO.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        PIC2TEXT.setWindowIcon(icon)
        PIC2TEXT.setWindowOpacity(9.0)
        PIC2TEXT.setToolTip("")
        self.centralwidget = QtWidgets.QWidget(PIC2TEXT)
        self.centralwidget.setObjectName("centralwidget")
        self.downloadB = QtWidgets.QPushButton(self.centralwidget)
        self.downloadB.setGeometry(QtCore.QRect(1020, 590, 241, 91))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Demi")
        font.setPointSize(26)
        self.downloadB.setFont(font)
        self.downloadB.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("ICONS/DOWNLOAD.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.downloadB.setIcon(icon1)
        self.downloadB.setIconSize(QtCore.QSize(201, 80))
        self.downloadB.setObjectName("downloadB")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(15, 11, 1341, 561))
        self.textBrowser.setOverwriteMode(True)
        self.textBrowser.setTabStopDistance(80.0)
        self.textBrowser.setObjectName("textBrowser")
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
        self.textBrowser.setHtml(_translate("PIC2TEXT", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:26pt;\">Sample Text</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PIC2TEXT = QtWidgets.QMainWindow()
    ui = Ui_PIC2TEXT()
    ui.setupUi(PIC2TEXT)
    PIC2TEXT.show()
    sys.exit(app.exec_())
