import sys

class Engine():
    currentWindow = None
    def __init__(self, _currentWindow):
        currentWindow = _currentWindow

    def open(self):
        pass
    
    def save(self):
        pass
    
    def __str__(self):
        return 'abstract engine'
        

def get_current(myWindow):

    engine = Engine(myWindow)

    if ('maya' in sys.executable):
        from pipeline.engine import maya_engine
        
        
        engine = maya_engine.MayaEngine(myWindow)
        
    if ('houdini' in sys.executable):
        from pipeline.engine.houdini_engine import HoudiniEngine

        engine = HoudiniEngine(myWindow)
        
    if ('Nuke' in sys.executable):
        from pipeline.engine.nuke_engine import NukeEngine
        engine = NukeEngine(myWindow)
    
    else:
        from pipeline.engine.standalone_engine import StandaloneEngine
        engine = StandaloneEngine(myWindow)
    return engine