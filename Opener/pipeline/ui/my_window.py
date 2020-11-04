import sys

from Qt import QtWidgets, QtCompat
from Qt.QtWidgets import QApplication
from pipeline.engine import engine  # get our Engine

# reload(engine)
from pipeline.engine.abc import abc_export  # get AbcEnginePart
import conf  # app conf


class MyWindow(QtWidgets.QMainWindow):
    
    # f/p
    AbcExportObject = ''

    def open(self):
        self.engine.open()
        
    def save(self):
        self.engine.save()

    def __init__(self):
        super(MyWindow, self).__init__()

        self.engine = engine.get_current(self)
        self.dataPath = ''
        
        # setup ui
        QtCompat.loadUi(conf.ui_path, self)

        # Set AbcExport
        self.AbcExportObject = abc_export.get_current(self)

        # ---- Opener part ---
        # openButton
        self.btn_openFile.clicked.connect(self.open)
        # saveButton
        self.btn_saveFile.clicked.connect(self.save)
        # ---- End opener part ---


       


def launchWindow():
  
    app = QApplication.instance()

    if app is None:
        app = QApplication(sys.argv)

    win = MyWindow()
    win.show()
    win.setFixedSize(win.size())
    app.exec_()