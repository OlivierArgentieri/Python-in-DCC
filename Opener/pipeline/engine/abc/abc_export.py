import sys
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

    currentWindow = ''

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

    def __init__(self, currentWindow):
        pass


def get_current(myWindow):
    abcExport = AbcExport(myWindow)

    if ('maya' in sys.executable):
        from .abc_export_maya import AbcExportMaya

        abcExport = AbcExportMaya(myWindow)

    if ('houdini' in sys.executable):
        pass

    if ('Nuke' in sys.executable):
        pass
    else:
        from .abc_export_standalone import AbcExportStandalone
        abcExport = AbcExportStandalone(myWindow)
    return abcExport