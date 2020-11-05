import hou
import os
import sys  # for argv

def generateAlembicNode(abcPath):
    root = hou.node("/obj/geo1")
    obj = root.createNode("alembic")
    obj.parm('fileName').set(abcPath)

def initFileNodes():
    obj = hou.node("/obj")
    obj.createNode("geo")



# ==== args ====
sourceDirectory = sys.argv[1]
outDirectory = sys.argv[2]

outFileName = 'out.hip'
outDirectory = os.path.join(outDirectory, outFileName)

hou.hipFile.save(outDirectory)
hou.hipFile.load(outDirectory)

# prepare base file
initFileNodes()


for file in os.listdir(sourceDirectory):
    if file.endswith(".abc"):
        generateAlembicNode(os.path.join(sourceDirectory, file))

hou.hipFile.save(outDirectory)
print('----- Houdini Scene File Generated ! -----')