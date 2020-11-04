import sys


class Engine(object):
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
        return engine

    if ('houdini' in sys.executable):
        from pipeline.engine.houdini_engine import HoudiniEngine
        engine = HoudiniEngine(myWindow)
        return engine

    if ('Nuke' in sys.executable):
        from pipeline.engine.nuke_engine import NukeEngine
        engine = NukeEngine(myWindow)
        return engine

    # then default engine
    from pipeline.engine.standalone_engine import StandaloneEngine
    engine = StandaloneEngine(myWindow)
    return engine

