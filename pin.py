# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pin_command.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PinWindow(object):
    def __init__(self, pin_number):
        self.pin_number = pin_number
    def setupUi(self, PinWindow):
        PinWindow.setObjectName("PinWindow")
        PinWindow.resize(400, 189)
        self.centralwidget = QtWidgets.QWidget(PinWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pin_label = QtWidgets.QLabel(self.centralwidget)
        self.pin_label.setGeometry(QtCore.QRect(60, 20, 71, 31))
        self.pin_label.setObjectName("pin_label")
        self.command_label = QtWidgets.QLabel(self.centralwidget)
        self.command_label.setGeometry(QtCore.QRect(60, 70, 71, 31))
        self.command_label.setObjectName("command_label")
        self.pin_entry = QtWidgets.QSpinBox(self.centralwidget)
        self.pin_entry.setGeometry(QtCore.QRect(140, 20, 131, 31))
        self.pin_entry.setObjectName("pin_entry")
        self.command_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.command_entry.setGeometry(QtCore.QRect(140, 70, 211, 31))
        self.command_entry.setObjectName("command_entry")
        self.ok_btn = QtWidgets.QPushButton(self.centralwidget)
        self.ok_btn.setGeometry(QtCore.QRect(160, 110, 91, 31))
        self.ok_btn.setObjectName("ok_btn")
        PinWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PinWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 24))
        self.menubar.setObjectName("menubar")
        PinWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PinWindow)
        self.statusbar.setObjectName("statusbar")
        PinWindow.setStatusBar(self.statusbar)

        self.retranslateUi(PinWindow)
        QtCore.QMetaObject.connectSlotsByName(PinWindow)

    def retranslateUi(self, PinWindow):
        _translate = QtCore.QCoreApplication.translate
        PinWindow.setWindowTitle(_translate("PinWindow", "MainWindow"))
        self.pin_label.setText(_translate("PinWindow", "Pin"))
        self.command_label.setText(_translate("PinWindow", "command"))
        self.ok_btn.setText(_translate("PinWindow", "Ok"))
import main_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PinWindow = QtWidgets.QMainWindow()
    ui = Ui_PinWindow()
    ui.setupUi(PinWindow)
    PinWindow.show()
    sys.exit(app.exec_())