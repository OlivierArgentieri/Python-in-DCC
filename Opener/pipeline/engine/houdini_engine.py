from pipeline.engine import engine
import hou
from lib.Qt import QtWidgets

class HoudiniEngine(engine.Engine):

    def open(self):
        #path = hou.ui.selectFile()
        path = QtWidgets.QFileDialog.getOpenFileName(self.currentWindow, "Open Houdini File", "/home", "Houdini Files (*.hip *. *.hipnc)")
        hou.hipFile.load(path[0])
        
    def save(self):
        path = QtWidgets.QFileDialog.getSaveFileName(self.currentWindow, "save Houdini File", "", "All Files (*)")
        #path = hou.ui.selectFile()


        hou.hipFile.save(file_name = path[0] + ".hip", save_to_recent_files=False)

    def __str__(self):
        return 'houdini engine'