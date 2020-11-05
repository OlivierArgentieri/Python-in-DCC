import hou
import os
import sys #for argv

hou.hipFile.load('D:/Projet/PullGithub/Python-in-DCC/Alembic/houdini/houdiniSample/BaseTemplateHoudini.hip')

hou.hipFile.save('D:/Projet/PullGithub/Python-in-DCC/Alembic/houdini/out/ImportAlembicTest.hip')
hou.hipFile.load('D:/Projet/PullGithub/Python-in-DCC/Alembic/houdini/out/ImportAlembicTest.hip')

# create base node

obj = hou.node("/obj")

obj.createNode("geo")

obj = hou.node("/obj/geo1")
obj.createNode("alembic")

# create Alembic node
obj = hou.node("/obj/geo1/alembic1")
obj.parm('fileName').set('D:/Projet/PullGithub/Python-in-DCC/Test/Maya/pCube1.abc')

# final save
hou.hipFile.save('D:/Projet/PullGithub/Python-in-DCC/Alembic/houdini/out/ImportAlembicTest.hip')

