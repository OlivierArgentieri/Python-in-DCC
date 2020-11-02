import sys, os
#import hou 
sys.path.append(os.path.abspath(os.getcwd()))

from pipeline.ui import my_window as mw

mw.launchWindow()

#import clear
#clear.do()#
# hou.session(mw)