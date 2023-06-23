from PySide2 import QtUiTools, QtWidgets
from PySide2.QtGui import QColor
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QMainWindow
import sys

import os

current_file_path = os.path.dirname(__file__)
drive = os.path.splitdrive(current_file_path)[0]

class PreferencesUI(QtWidgets.QWidget):

    window = None

    def __init__(self, parent=None):
        """
        Import UI and connect components
        """
        super(PreferencesUI, self).__init__(parent)

        # load the created UI widget
        self.widgetPath = current_file_path + "\\"
        self.widget = QtUiTools.QUiLoader().load(
            self.widgetPath + "ToolGUI.ui"
        )  # path to PyQt .ui file
        
        self.preferencesWidget = None

        # attach the widget to the instance of this class (aka self)
        self.widget.setParent(self)
        
def openMainWindow():
    """
    Create tool window.
    """
    if QtWidgets.QApplication.instance():
        # Id any current instances of tool and destroy
        for win in QtWidgets.QApplication.allWindows():
            if "toolWindow" in win.objectName():  # update this name to match name below
                win.destroy()
    else:
        QtWidgets.QApplication(sys.argv)

    # load UI into QApp instance
    PreferencesUI.window = PreferencesUI()
    PreferencesUI.window.show()
    # update this with something unique to your tool
    PreferencesUI.window.setObjectName("Preferences")
    PreferencesUI.window.setWindowTitle("Preferences")