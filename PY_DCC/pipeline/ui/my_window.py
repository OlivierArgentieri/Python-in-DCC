import sys, os
#sys.path.append(r'\\multifct\tools\pipeline\global\packages') #path to QT Package

from Qt import QtWidgets, QtCompat
from Qt.QtWidgets import QApplication
from pipeline.engine import engine # get our Engine
#reload(engine)



#os.path.join
ui_path = os.path.abspath(os.getcwd())+'\\pipeline\\ui\\my_window_new.ui'
#ui_path = r'D:\\Projet\\PullGithub\Artfx_Courses\\Haussman\\PythonInDCC\\PY_DCC\\pipeline\\ui\\my_window_new.ui'

class MyWindow(QtWidgets.QMainWindow):
    
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
        
        # openDialogButton
        #self.btn_openFile.clicked.connect()

        # openButton
        self.btn_openFile.clicked.connect(self.open)
        
        # saveButton
        self.btn_saveFile.clicked.connect(self.save)


def launchWindow():
  
    app = QApplication.instance()

    if app is None:
        app = QApplication(sys.argv)

    win = MyWindow()
    win.show()

    app.exec_()