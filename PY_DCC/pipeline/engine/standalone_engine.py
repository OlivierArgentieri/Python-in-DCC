from pipeline.engine import engine
import subprocess, os, platform

from Qt import QtWidgets
class StandaloneEngine(engine.Engine):

    def open(self):
      path = QtWidgets.QFileDialog.getOpenFileName(self.currentWindow, "Open Maya File", "D:\OlivierArgentieri\Project\Pull_github", "*.*")
      #print("test")

      if(platform.system() == 'Darwin'): # mac
         subprocess.call(('open', path[0]))
      elif (platform.system() == "Windows"): #windows
         os.startfile(path[0])
      else:
         subprocess.call(("xdg-open", path[0])) #linux

    def save(self):
         #path = cmds.fileDialog2(fileMode = 0, startingDirectory = "D:\OlivierArgentieri\Project\Pull_github\Artfx_Courses\Haussman\Micro_film\Maya\scenes\Layout", fileFilter="Maya Ascii (*.mb)")
         # todo error
         pass