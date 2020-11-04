class AbcExport(object):
    # f/p
    rootObjects = []
    mayabatch = ''
    exec_py = ''

    # ui elements
    tb_SceneFile = ''
    tb_OutFolder = ''
    tb_RootObjects = ''

    sb_startFrame = ''
    sb_endFrame = ''

    mainWindow = ''

    def browseSceneFile(self):
        pass

    def browseOutFolder(self):
        pass

    def onClick_runExport(self):
        pass

    def bindEvent(self):
        pass

    def tryParseRootElement(self, pathFile):
        pass

    def isValid(self):
        pass

    def __init__(self, mainWindow):
        pass