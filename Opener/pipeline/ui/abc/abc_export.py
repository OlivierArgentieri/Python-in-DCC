import sys, os, subprocess
from Qt import QtWidgets, QtCompat
from pipeline.conf import mayabatch, exec_py # app conf

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
        # open file browser only for maya mb|ma
        path = QtWidgets.QFileDialog.getOpenFileName(self.mainWindow, "Open Maya File", "D:\Projet\PullGithub\Python-in-DCC\Test\Maya", "*.ma *.mb")

        if path[0] == '':
            return

        self.tb_SceneFile.setText(path[0])
        self.tryParseRootElement(path[0])
        pass

    def browseOutFolder(self):
        dialog = QtWidgets.QFileDialog()
        dialog.setOption(QtWidgets.QFileDialog.ShowDirsOnly, True)
        dialog.setFileMode(QtWidgets.QFileDialog.DirectoryOnly)

        directory = QtWidgets.QFileDialog.getExistingDirectory(self.mainWindow, 'Out directory', "D:\Projet\PullGithub\Python-in-DCC\Test\Maya")
        if QtWidgets.QDialog.Accepted:
            self.tb_OutFolder.setText(directory)

    def onClick_runExport(self):
        # call custom commands
        command = [self.mayabatch, '-script', self.exec_py, self.tb_SceneFile.text(), self.tb_OutFolder.text(), str(self.sb_startFrame.value()), str(self.sb_endFrame.value())]
        subprocess.Popen(command + self.rootObjects, shell=True)

    def bindEvent(self):
        if not self.mainWindow:
            pass
        self.mainWindow.btn_abcBrowseSceneFile.clicked.connect(self.browseSceneFile)
        self.mainWindow.btn_abcOutFolder.clicked.connect(self.browseOutFolder)
        self.mainWindow.btn_abcRunExport.clicked.connect(self.onClick_runExport)

    def tryParseRootElement(self, pathFile):

        if pathFile == '' or os.path.splitext(pathFile)[1] != '.ma':
            self.tb_RootObjects.setText('')
            return
        file = open(pathFile, 'r')
        self.rootObjects = []
        for line in file.readlines():
            if "createNode transform -n" in line:
                self.rootObjects.append(
                    line.split('-n')[1].split(' ')[1].replace(';', '').replace('"', '').replace('\n', ''))

        self.tb_RootObjects.setText(' '.join(self.rootObjects))

    def isValid(self):
        return not self.tb_SceneFile.text() and not self.tb_OutFolder.text() and not self.tb_RootObjects.text()

    def __init__(self, mainWindow):
        self.tb_SceneFile = mainWindow.tb_abcSceneFile
        self.tb_OutFolder = mainWindow.tb_abcOutFolder
        self.tb_RootObjects = mainWindow.tb_abcRootObjects

        #conf
        self.mayabatch = mayabatch
        self.exec_py = exec_py

        # spin box
        self.sb_startFrame = mainWindow.sb_startFrame
        self.sb_endFrame = mainWindow.sb_endFrame

        # ref main window
        self.mainWindow = mainWindow

        # bind Action
        self.bindEvent()
