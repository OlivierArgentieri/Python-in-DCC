import sys
import maya.cmds as cmds



# from parameters
mayaSceneFile = sys.argv[3]
exportFileName = sys.argv[4]
frameStart = sys.argv[5]
frameEnd = sys.argv[6]
rootObjects = sys.argv[7:]


# open file
cmds.file(mayaSceneFile, open = True, force=True)

# test object exist

for rootObject in rootObjects:

    # motion blur :  fram range -frameRange -0.25 -frameRelativeSample 0 -frameRelativeSample 0.5
    command = "-frameRange " + frameStart + " " + frameEnd +" -uvWrite -dataFormat ogawa -root " + rootObject + " -file " + exportFileName +"/"+rootObject+".abc "
    cmds.AbcExport ( j = command )

print('----- Export Alembic Complete ! -----')