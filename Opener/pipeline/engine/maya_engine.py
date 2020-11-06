import maya.cmds as cmds
from pipeline.engine import engine
from lib.Qt import QtWidgets
class MayaEngine(engine.Engine):
    def open(self):
       path = QtWidgets.QFileDialog.getOpenFileName(self.currentWindow, "Open Maya File", "D:\OlivierArgentieri\Project\Pull_github\Artfx_Courses\Haussman\Micro_film\Maya\scenes\Layout", "*.ma *.mb")
       #path = cmds.fileDialog2(fileMode = 1, startingDirectory = "D:\OlivierArgentieri\Project\Pull_github\Artfx_Courses\Haussman\Micro_film\Maya\scenes\Layout", fileFilter="Maya Ascii (*.mb)")
       cmds.file(path[0], open = True, force=True)

    def save(self):
       #path = cmds.fileDialog2(fileMode = 0, startingDirectory = "D:\OlivierArgentieri\Project\Pull_github\Artfx_Courses\Haussman\Micro_film\Maya\scenes\Layout", fileFilter="Maya Ascii (*.mb)")
       path = QtWidgets.QFileDialog.getSaveFileName(self.currentWindow, "Open Houdini File", "", "All Files (*)")
       
       cmds.file(rename = path[0])
       cmds.file(save = True)

    def __str__(self):
        return 'maya engine'