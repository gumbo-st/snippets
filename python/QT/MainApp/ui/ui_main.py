import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.QtCore import QFile
from PySide6.QtCore import QCoreApplication
from ui.ui_mainwindow import Ui_MainWindow
from ui.ui_aboutdialog import Ui_aboutDialog
import version



class MainWindow(QMainWindow):
    """
    Main window for application
    """
    def __init__(self):
        super(MainWindow,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui_about = None
    
        self.ui.actionExit.triggered.connect(self.onActionExitClick)
        self.ui.actionAbout.triggered.connect(self.showAboutWindow)
    

    def closeEvent(self, event):
        """ Overiding this method to catch the application
            closing if the user doesn't use the exit menu item
        """
        # @TODO: make sure all files are closed properly
        #        and the json file is written out if applicable
        print("caught window close event")

    def onActionExitClick(self):
        QCoreApplication.quit()

    def showAboutWindow(self):
        if self.ui_about is None:
            self.ui_about = AboutWindow()
        ver_str = str(version.VER_MAJOR) + "." + str(version.VER_MINOR) + "." + str(version.VER_BETA)
        self.ui_about.ui.label_app_ver_val.setText(ver_str)
        self.ui_about.show()


class AboutWindow(QWidget):
    """
    Show the About information.
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self):
        super().__init__()
        self.ui = Ui_aboutDialog()
        self.ui.setupUi(self)