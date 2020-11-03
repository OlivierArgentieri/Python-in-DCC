import sys, time
import maya.cmds as cmds


print(sys.argv)


# from parameters
fileName = sys.argv[4]
frameStart = sys.argv[5]
frameEnd = sys.argv[6]
objectName = sys.argv[7]


# open file
cmds.file("D:\\Projet\\PullGithub\\Python-in-DCC\\Test\\Maya\\animation_sample.mb", open = True, force=True)
print cmds.ls('pCube1')

#command = "-frameRange " + "0" + " " + "20" +" -uvWrite -dataFormat ogawa -root " + "pCube1" + " -file " + "C:\\Users\\olivi\\Desktop\\test2.abc"
# fram range -frameRange -0.25 -frameRelativeSample 0 -frameRelativeSample 0.5
command = "-frameRange " + frameStart + " " + frameEnd +" -uvWrite -dataFormat ogawa -root " + objectName + " -file " + "C:\\Users\\olivi\\Desktop\\test2.abc"
cmds.AbcExport ( j = command )
# mayabatch. exe
# maya-batch
#./mayabatch.exe -script D:\Projet\PullGithub\Python-in-DCC\Alembic\test.mel
#./mayabatch.exe -command 'python("execfile(\'D:/Projet/PullGithub/Python-in-DCC/Alembic/open.py\')");'
#./mayabatch.exe -script D:\Projet\PullGithub\Python-in-DCC\Alembic\test.mel "D:\\Projet\\PullGithub\\Python-in-DCC\\Test\\Maya\\animation_sample.mb"
# #mayabatch.exe -batch -file someMayaFile.mb -command "file -save"