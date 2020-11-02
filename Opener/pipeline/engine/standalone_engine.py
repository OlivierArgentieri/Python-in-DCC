from pipeline.engine import engine
import subprocess, os, platform

from Qt import QtWidgets
class StandaloneEngine(engine.Engine):

    def open(self):
      path = QtWidgets.QFileDialog.getOpenFileName(self.currentWindow, "Open Maya File", "D:\OlivierArgentieri\Project\Pull_github", "*.*")

      if(platform.system() == 'Darwin'): # mac
         subprocess.call(('open', path[0]))
      elif (platform.system() == "Windows"): #windows
         os.startfile(path[0])
      else:
         subprocess.call(("xdg-open", path[0])) #linux

    def save(self):
         
         pass