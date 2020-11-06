import sys, os, subprocess
from lib.Qt import QtWidgets, QtCompat
from pipeline.conf import mayabatch, exec_py, hython, abcsToSceneHoudini  # app conf


class AbcToHip(object):
    # ---  f/p ---

    # conf
    hython = ''
    abcsToSceneHoudini = ''

    # ui elements
    mainWindow = ''

    tb_SourceFolder = ''
    tb_OutFolder = ''

    # end f/p ----

    def isValid(self):
        return not self.tb_SourceFolder.text() and not self.tb_OutFolder.text()

    def browseSourceFolder(self):
        # open file browser only for maya mb|ma
        dialog = QtWidgets.QFileDialog()
        dialog.setOption(QtWidgets.QFileDialog.ShowDirsOnly, True)
        dialog.setFileMode(QtWidgets.QFileDialog.DirectoryOnly)

        directory = QtWidgets.QFileDialog.getExistingDirectory(self.mainWindow, 'source directory',
                                                               "D:\Projet\PullGithub\Python-in-DCC\Test\Maya")

        if QtWidgets.QDialog.Accepted:
            self.tb_SourceFolder.setText(directory)
        pass

    def browseOutFolder(self):
        dialog = QtWidgets.QFileDialog()
        dialog.setOption(QtWidgets.QFileDialog.ShowDirsOnly, True)
        dialog.setFileMode(QtWidgets.QFileDialog.DirectoryOnly)

        directory = QtWidgets.QFileDialog.getExistingDirectory(self.mainWindow, 'Out directory',
                                                               "D:\Projet\PullGithub\Python-in-DCC\Test\Maya")
        if QtWidgets.QDialog.Accepted:
            self.tb_OutFolder.setText(directory)

    def onClick_runExport(self):
        self.generateHoudiniScene()

    def generateHoudiniScene(self):
        command = [self.hython, self.abcsToSceneHoudini, self.tb_SourceFolder.text(), self.tb_OutFolder.text()]

        subprocess.call(command, shell=True)

    def bindEvent(self):
        if not self.mainWindow:
            pass
        self.mainWindow.btn_abctohou_sourceDir.clicked.connect(self.browseSourceFolder)
        self.mainWindow.btn_abctohou_destinationDir.clicked.connect(self.browseOutFolder)
        self.mainWindow.btn_abctohou_run.clicked.connect(self.onClick_runExport)

    def __init__(self, mainWindow):
        self.tb_SourceFolder = mainWindow.tb_abctohou_source
        self.tb_OutFolder = mainWindow.tb_abctohou_destination

        # conf
        self.hython = hython
        self.abcsToSceneHoudini = abcsToSceneHoudini

        # ref main window
        self.mainWindow = mainWindow

        # bind Action
        self.bindEvent()
