from PyQt5 import QtCore, QtGui, QtWidgets
from pynput import keyboard
import backend

class Ui_PinWindow(object):
    def __init__(self, switch_number):
        self.switch_number = switch_number     
        self.command_sequence = []  # Store the sequence of commands

    def setupUi(self, PinWindow):
        PinWindow.setObjectName("PinWindow")
        PinWindow.setFixedSize(400, 189)
        self.centralwidget = QtWidgets.QWidget(PinWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.command_label = QtWidgets.QLabel(self.centralwidget)
        self.command_label.setGeometry(QtCore.QRect(60, 50, 71, 31))
        self.command_label.setObjectName("command_label")
        self.command_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.command_entry.setGeometry(QtCore.QRect(140, 50, 211, 31))
        self.command_entry.setObjectName("command_entry")
        self.command_entry.setReadOnly(True)  # Make the entry read-only
        self.ok_btn = QtWidgets.QPushButton(self.centralwidget)
        self.ok_btn.setGeometry(QtCore.QRect(160, 110, 91, 31))
        self.ok_btn.setObjectName("ok_btn")
        self.ok_btn.clicked.connect(self.ok_btn_clicked)
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

        self.start_key_listener()

    def start_key_listener(self):
        self.listener = keyboard.Listener(on_release=self.on_release)
        self.listener.start()

    def on_release(self, key):
        try:
            key_char = key.char
        except AttributeError:
            key_char = str(key).replace("Key.", "")

        if key_char not in self.command_sequence:
            self.command_sequence.append(key_char)
            self.update_command_entry()

        if key == keyboard.Key.esc:
            return False

    def update_command_entry(self):
        try:
            command = "+".join(self.command_sequence)
            QtCore.QMetaObject.invokeMethod(
                self.command_entry, "setText", QtCore.Qt.QueuedConnection, QtCore.Q_ARG(str, command))
        except Exception as e:
            pass

    def ok_btn_clicked(self):
        command = self.command_entry.text()
        backend.update_command_to_json(self.switch_number, command)
        self.centralwidget.parentWidget().close()

    def retranslateUi(self, PinWindow):
        _translate = QtCore.QCoreApplication.translate
        PinWindow.setWindowTitle(_translate("PinWindow", "Pin Command"))
        self.command_label.setText(_translate("PinWindow", "Command"))
        self.ok_btn.setText(_translate("PinWindow", "Ok"))

class PinWindow(QtWidgets.QMainWindow, Ui_PinWindow):
    def __init__(self, switch_number):
        super().__init__()
        self.setupUi(self)
        self.switch_number = switch_number
