from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog
from PIL import Image, ImageTk
from pyzbar.pyzbar import decode
import pyqrcode
import os
class qrcode_App(object):
    def setupUi(self, MainWindow):
        # create instance fot translate
        _translate = QtCore.QCoreApplication.translate
        # set properties for main window
        MainWindow.setWindowTitle(_translate("MainWindow", "QR Code app"))
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(413, 441)
        # create central widget area on main window
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # define font
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        # create tab widget
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 411, 441))
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")
        self.tabWidget.addTab(self.tab1, "")
        self.tabWidget.addTab(self.tab2, "")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("MainWindow", "Generate QR Code"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), _translate("MainWindow", "Read QR Code"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.tabWidget.setCurrentIndex(0)
        # create widgets for first tab
        self.label_1 = QtWidgets.QLabel(self.tab1)
        self.label_1.setGeometry(QtCore.QRect(130, 50, 181, 151))
        self.label_1.setObjectName("label_1")
        self.lineEdit_1 = QtWidgets.QLineEdit(self.tab1)
        self.lineEdit_1.setGeometry(QtCore.QRect(190, 250, 171, 31))        
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab1)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 310, 171, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.generate_pushButton = QtWidgets.QPushButton(self.tab1, clicked=lambda: self.generate())
        self.generate_pushButton.setGeometry(QtCore.QRect(50, 360, 121, 31))
        self.generate_pushButton.setObjectName("generate_pushButton")
        self.generate_pushButton.setText(_translate("MainWindow", "Generate"))
        self.exit_pushButton_1 = QtWidgets.QPushButton(self.tab1, clicked=lambda: self.close())        
        self.exit_pushButton_1.setGeometry(QtCore.QRect(200, 360, 121, 31))
        self.exit_pushButton_1.setObjectName("exit_pushButton_1")
        self.exit_pushButton_1.setText(_translate("MainWindow", "Exit"))
        self.label_3 = QtWidgets.QLabel(self.tab1)
        self.label_3.setGeometry(QtCore.QRect(60, 240, 121, 51))
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_3.setText(_translate("MainWindow", "Enter data:"))
        
        self.label_4 = QtWidgets.QLabel(self.tab1)
        self.label_4.setGeometry(QtCore.QRect(50, 290, 131, 61))
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><div>Enter Name </div><div>to save with:</div></body></html>"))
    
        self.label_2 = QtWidgets.QLabel(self.tab2)
        self.label_2.setGeometry(QtCore.QRect(120, 60, 171, 161))
        self.label_2.setObjectName("label_2")
        # widgets for second tab
        self.select_pushButton = QtWidgets.QPushButton(self.tab2, clicked=lambda: self.read())
        self.select_pushButton.setGeometry(QtCore.QRect(60, 360, 111, 31))
        self.select_pushButton.setObjectName("select_pushButton")
        self.select_pushButton.setText(_translate("MainWindow", "Select"))
        self.exit_pushButton_2 = QtWidgets.QPushButton(self.tab2, clicked=lambda: self.close())
        self.exit_pushButton_2.setGeometry(QtCore.QRect(210, 360, 111, 31))
        self.exit_pushButton_2.setObjectName("exit_pushButton_2")
        self.exit_pushButton_2.setText(_translate("MainWindow", "Exit"))
        self.label_5 = QtWidgets.QLabel(self.tab2)
        self.label_5.setGeometry(QtCore.QRect(120, 289, 321, 41))
        self.label_5.setObjectName("label_5")
    def generate(self):
        if self.lineEdit_1.text() != '' and self.lineEdit_2.text() != '':
            # create qr code
            qr = pyqrcode.create(self.lineEdit_1.text())
            # save image
            img = qr.png(self.lineEdit_2.text()+".png", scale = 5)
            # set image to the label
            self.label_1.setPixmap(QPixmap(f"{self.lineEdit_2.text()}.png"))
    def read(self):
        # file dialog to select image from folder
        img_file = QFileDialog.getOpenFileName()
        # read image path from selected image
        img_path = img_file[0]
        # decode qr code image
        d = decode(Image.open(img_path))
        data = d[0].data.decode()
        # set image to the label
        self.label_2.setPixmap(QPixmap(img_path))
        # set qr code data text to the label
        self.label_5.setText(data)
    def close(self):
        MainWindow.destroy()
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = qrcode_App()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
