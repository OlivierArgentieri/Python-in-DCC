import os
import subprocess
from Qt import QtWidgets, QtCompat
import conf  # app conf
import maya.cmds as cmds
# mother
from .abc_export import AbcExport


class AbcExportMaya(AbcExport):
    # f/p
    rootObjects = []

    # ui elements
    tb_SceneFile = ''
    tb_OutFolder = ''
    tb_RootObjects = ''

    sb_startFrame = ''
    sb_endFrame = ''

    currentWindow = ''

    def browseSceneFile(self):
        # open file browser only for maya mb|ma
        path = QtWidgets.QFileDialog.getOpenFileName(self.currentWindow, "Open Maya File",
                                                     "D:\Projet\PullGithub\Python-in-DCC\Test\Maya", "*.ma *.mb")

        if path[0] == '':
            return

        self.tb_SceneFile.setText(path[0])
        self.tryParseRootElement(path[0])
        pass

    def browseOutFolder(self):
        dialog = QtWidgets.QFileDialog()
        dialog.setOption(QtWidgets.QFileDialog.ShowDirsOnly, True)
        dialog.setFileMode(QtWidgets.QFileDialog.DirectoryOnly)

        directory = QtWidgets.QFileDialog.getExistingDirectory(self.currentWindow, 'Out directory',
                                                               "D:\Projet\PullGithub\Python-in-DCC\Test\Maya")
        if QtWidgets.QDialog.Accepted:
            self.tb_OutFolder.setText(directory)

    def onClick_runExport(self):
        # call custom commands
        for rootObject in self.rootObjects:
            command = ['-frameRange ', str(self.sb_startFrame.value()), str(self.sb_endFrame.value()), ' -uvWrite -dataFormat ogawa -root ', rootObject, ' -file', self.tb_OutFolder.text(), '/', rootObject, '.abc']
            cmds.AbcExport(j=''.join(command))

    def bindEvent(self):
        if not self.currentWindow:
            pass
        self.currentWindow.btn_abcBrowseSceneFile.clicked.connect(self.browseSceneFile)
        self.currentWindow.btn_abcOutFolder.clicked.connect(self.browseOutFolder)
        self.currentWindow.btn_abcRunExport.clicked.connect(self.onClick_runExport)

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

    def __init__(self, currentWindow):
        super().__init__(currentWindow)
        self.tb_SceneFile = currentWindow.tb_abcSceneFile
        self.tb_OutFolder = currentWindow.tb_abcOutFolder
        self.tb_RootObjects = currentWindow.tb_abcRootObjects

        # spin box
        self.sb_startFrame = currentWindow.sb_startFrame
        self.sb_endFrame = currentWindow.sb_endFrame

        # ref main window
        self.currentWindow = currentWindow

        # bind Action
        self.bindEvent()
