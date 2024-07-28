from PySide2 import QtUiTools, QtWidgets
from PySide2.QtGui import QColor
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QMainWindow

class SecondWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Load the UI file for this window
        self.ui = QtWidgets.QUiLoader().load("path_to_second_window_ui_file.ui")