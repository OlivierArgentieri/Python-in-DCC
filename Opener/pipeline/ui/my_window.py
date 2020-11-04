import sys

from Qt import QtWidgets, QtCompat
from Qt.QtWidgets import QApplication
from pipeline.engine import engine  # get our Engine

# reload(engine)
from .abc.abc_export import AbcExport  # get AbcEnginePart
import conf  # app conf


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
        QtCompat.loadUi(conf.ui_path, self)

        # Set AbcExport
        self.AbcExportObject = AbcExport(self)

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