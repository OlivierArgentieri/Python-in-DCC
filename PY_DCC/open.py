import sys, os
#import hou 
sys.path.append(os.path.abspath(os.getcwd()))
sys.path.append(r'D:\\Projet\\PullGithub\\Artfx_Courses\\Haussman\\PythonInDCC\\PY_DCC')

from pipeline.ui import my_window as mw

mw.launchWindow()

#import clear
#clear.do()#
# hou.session(mw)