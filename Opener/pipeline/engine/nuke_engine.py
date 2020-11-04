import sys, nuke
from pipeline.engine import engine

class NukeEngine(engine.Engine):
    def open(self):
       path = nuke.getFilename('Get File Contents', '*.nknc *.nk')
       nuke.load(path)
       
    def save(self):
       path = nuke.getFilename('To save', '*.nknc *.nk')
       nuke.nodeCopy(path)

    def __str__(self):
        return 'nuke engine'