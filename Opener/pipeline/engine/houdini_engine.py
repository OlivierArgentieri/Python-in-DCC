from pipeline.engine import engine
import hou
from Qt import QtWidgets

class HoudiniEngine(engine.Engine):

    def open(self):
        #path = hou.ui.selectFile()
        path = QtWidgets.QFileDialog.getOpenFileName(self.currentWindow, "Open Houdini File", "/home", "Houdini Files (*.hip *. *.hipnc)")
        #path = QtWidgets.QFileDialog.getOpenFileName(self, 'Open houdini file', "D:\OlivierArgentieri\Project\Pull_github\Artfx_Courses\Haussman\Micro_film\Maya\scenes\Layout", "*.*", options=options)
        hou.hipFile.load(path)
        
    def save(self):
        path = QtWidgets.QFileDialog.getSaveFileName(self.currentWindow, "Open Houdini File", "", "All Files (*)")
        #path = hou.ui.selectFile()
        hou.hipFile.save(file_name = path[0] + ".hip", save_to_recent_files=False)
        