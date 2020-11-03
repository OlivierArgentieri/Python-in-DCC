import os
import sys

from Qt import QtWidgets, QtCompat
from Qt.QtWidgets import QApplication
from pipeline.engine import engine  # get our Engine

# reload(engine)
from .abc.abc_export import AbcExport  # get AbcEnginePart

#os.path.join
ui_path = os.path.abspath(os.getcwd())+'\\pipeline\\ui\\my_window_v2.ui'
mayabatch = "D:/Program_Files/Maya2019.2/bin/mayabatch.exe" # path to maya batch

class MyWindow(QtWidgets.QMainWindow):
    
    # f/p
    AbcExportObject = ''

    def openDialog(self):
        return QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', "D:\OlivierArgentieri\Project\Pull_github\Artfx_Courses\Haussman\Micro_film\Maya\scenes\Layout", '*.*')

    def open(self):
        self.engine.open()
        
    def save(self):
        self.engine.save()

    def __init__(self):
        super(MyWindow, self).__init__()
        self.engine = engine.get_current(self)
        self.dataPath = ''
        
        # setup ui
        QtCompat.loadUi(ui_path, self)

        # Set AbcExport
        self.AbcExportObject = AbcExport(self, mayabatch)

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