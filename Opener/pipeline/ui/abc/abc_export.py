from Qt import QtWidgets, QtCompat


class AbcExport(object):
    # f/p
    rootObject = []

    # ui elements
    tb_SceneFile = ''
    tb_OutFolder = ''
    tb_RootObjects = ''

    btn_browseSceneFile = ''
    btn_OutFolder = ''

    mainWindow = ''

    def browseSceneFile(self):
        # open file browser only for maya mb|ma
        path = QtWidgets.QFileDialog.getOpenFileName(self.mainWindow, "Open Maya File", "D:\Projet\PullGithub\Python-in-DCC\Test\Maya", "*.ma *.mb")

        if path[0] == '':
            return

        self.tb_SceneFile.setText(path[0])
        pass

    def browseOutFolder(self):
        dialog = QtWidgets.QFileDialog()
        dialog.setOption(QtWidgets.QFileDialog.ShowDirsOnly, True)
        dialog.setFileMode(QtWidgets.QFileDialog.DirectoryOnly)

        directory = QtWidgets.QFileDialog.getExistingDirectory(self.mainWindow, 'Out directory', "D:\Projet\PullGithub\Python-in-DCC\Test\Maya")
        if QtWidgets.QDialog.Accepted:
            self.tb_OutFolder.setText(directory)


    def onClick_runExport(self):
        pass


    def bindEvent(self):
        if not self.mainWindow:
            pass
        self.mainWindow.btn_abcBrowseSceneFile.clicked.connect(self.browseSceneFile)
        self.mainWindow.btn_abcOutFolder.clicked.connect(self.browseOutFolder)

    def tryParseRootElement(self):
        pass

    def __init__(self, mainWindow):
        self.tb_SceneFile = mainWindow.tb_abcSceneFile
        self.tb_OutFolder = mainWindow.tb_abcOutFolder
        self.tb_RootObjects = mainWindow.tb_abcRootObjects

        self.mainWindow = mainWindow
        self.bindEvent()
