# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AboutGuide.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AboutGuide(object):
    def setupUi(self, AboutGuide):
        AboutGuide.setObjectName("AboutGuide")
        AboutGuide.resize(755, 581)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:/Abdullah/Mata Kuliah/Semester 7/TA - Tugas Akhir/Laporan/dataencryption_application_dedatos_3363.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AboutGuide.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(AboutGuide)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(2, 0, 751, 71))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 491, 101))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 60, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 197, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(26, 256, 361, 211))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(6, 226, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(400, 240, 361, 211))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(380, 226, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 470, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(25, 495, 701, 41))
        self.label_10.setObjectName("label_10")
        AboutGuide.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AboutGuide)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 755, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        AboutGuide.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AboutGuide)
        self.statusbar.setObjectName("statusbar")
        AboutGuide.setStatusBar(self.statusbar)
        self.actionAbout = QtWidgets.QAction(AboutGuide)
        self.actionAbout.setObjectName("actionAbout")
        self.actionGuide = QtWidgets.QAction(AboutGuide)
        self.actionGuide.setObjectName("actionGuide")
        self.actionHash_Function = QtWidgets.QAction(AboutGuide)
        self.actionHash_Function.setObjectName("actionHash_Function")
        self.actionMain_Menu = QtWidgets.QAction(AboutGuide)
        self.actionMain_Menu.setObjectName("actionMain_Menu")
        self.actionQuit = QtWidgets.QAction(AboutGuide)
        self.actionQuit.setObjectName("actionQuit")
        self.menuMenu.addAction(self.actionAbout)
        self.menuMenu.addAction(self.actionMain_Menu)
        self.menuMenu.addAction(self.actionQuit)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(AboutGuide)
        QtCore.QMetaObject.connectSlotsByName(AboutGuide)

    def retranslateUi(self, AboutGuide):
        _translate = QtCore.QCoreApplication.translate
        AboutGuide.setWindowTitle(_translate("AboutGuide", "StegoKrip"))
        self.label.setText(_translate("AboutGuide", "Implementation Program for Data Security"))
        self.label_2.setText(_translate("AboutGuide", "This program can secure information in the .txt format\n"
"\n"
"Security used is to use Cryptography and Steganography\n"
"\n"
"The .txt file is encrypted using the AES algorithm and hidden into image \n"
"files to hide, so it becomes a double security for accessing information in the .txt file"))
        self.label_3.setText(_translate("AboutGuide", "About   :"))
        self.label_4.setText(_translate("AboutGuide", "Guide  :"))
        self.label_5.setText(_translate("AboutGuide", "The .txt file is encrypted first using the encryption \n"
"function by entering the file name along with the file format, \n"
"then enter the password that will be the key in the \n"
"encryption process, then fill in the output file name along \n"
"with the file format (.txt) that will be the cipher file.\n"
"\n"
"Plaintext files that have been encrypted into Ciphertext \n"
"are entered into hide\'s function to insert messages into images.\n"
"enter the name of the CipherText File and its format into the \n"
"\"File can be hide\" textbox, then enter Image File that \n"
"will be inserted in the message along with the format, and \n"
"enter the file name that will Output File with the format \n"
"(.png) and Output file Hash for Digital Signature and Recovery."))
        self.label_6.setText(_translate("AboutGuide", "Encryption and Hide  :"))
        self.label_7.setText(_translate("AboutGuide", "\n"
"To return information that has been encrypted, the image \n"
"file (StegoImage) is entered into the recovery function and \n"
"check Code Hash for Digital Sigature, if match then file \n"
"can be recovery, after that enter the output file name \n"
"with the format (.txt) to restore the inserted file.\n"
"\n"
"Files that have been returned from images, decrypted using \n"
"the Decryption function by entering the file name to be \n"
"decrypted along with the format, entering the password \n"
"that is the key to encrypt the message, and entering \n"
"the output file name which will be the decrypted file \n"
"name."))
        self.label_8.setText(_translate("AboutGuide", "Decryption and Recovery  :"))
        self.label_9.setText(_translate("AboutGuide", "Hash Function :"))
        self.label_10.setText(_translate("AboutGuide", "Hash function becomes the identity of each message that will be sent to the recipient, that message is genuine from the sender. \n"
"Makes the hash function for Digital Signature."))
        self.menuMenu.setTitle(_translate("AboutGuide", "Menu"))
        self.actionAbout.setText(_translate("AboutGuide", "About and Guide"))
        self.actionGuide.setText(_translate("AboutGuide", "Guide"))
        self.actionHash_Function.setText(_translate("AboutGuide", "Hash Function"))
        self.actionMain_Menu.setText(_translate("AboutGuide", "Main Menu"))
        self.actionQuit.setText(_translate("AboutGuide", "Quit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AboutGuide = QtWidgets.QMainWindow()
    ui = Ui_AboutGuide()
    ui.setupUi(AboutGuide)
    AboutGuide.show()
    sys.exit(app.exec_())

