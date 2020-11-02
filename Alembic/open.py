import sys
import maya.cmds as cmds

print(sys.argv)


# from parameters
# frameStart = sys.argv[0]
# frameEnd = sys.argv[1]
# objectName = sys.argv[2]
# fileName = sys.argv[3]

# open file
cmds.file("D:\\Projet\\PullGithub\\Artfx_Courses\\Haussman\\Micro_film\\Maya\\scenes\\Layout\\s010_animation_v007_final.mb", open = True, force=True)

command = "-frameRange " + "0" + " " + "10" +" -uvWrite -dataFormat ogawa -root " + "car02:root" + " -file " + "C:\\Users\\olivi\\Desktop\\test.abc"
cmds.AbcExport ( j = command )
# mayabatch. exe
# maya-batch
#./mayabatch.exe -script D:\Projet\PullGithub\Python-in-DCC\Alembic\test.mel
#./mayabatch.exe -command 'python("execfile(\'D:/Projet/PullGithub/Python-in-DCC/Alembic/open.py\')");'
# ./mayabatch.exe -script D:\Projet\PullGithub\Python-in-DCC\Alembic\test.mel "D:\\Projet\\PullGithub\\Artfx_Courses\\Haussman\\Micro_film\\Maya\\scenes\\Layout\\s010_animation_v007.mb"
# #mayabatch.exe -batch -file someMayaFile.mb -command "file -save"