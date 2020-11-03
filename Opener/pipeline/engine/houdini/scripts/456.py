# -*- coding: utf-8 -*-
"""
ARTFX Pipeline Launch script for Houdini.

For this to work:
HOUDINI_SCRIPT_PATH must be set with ";" separator and the pipeline script location must be last.
Example: HOUDINI_SCRIPT_PATH = &;T:/PIPELINE/users/mhaussmann/workspace/alpha/packages/houdiniLib/launch/scripts

"""
import sys
print('Starting up Pipeline in Houdini')

here = hou.getenv('HOUDINI_SCRIPT_PATH').split(';')[-1]   # os.path.dirname(__file__) not working in 456.py

deployment_root = here.split('/pipeline/')[0]
print('Script root {}'.format(deployment_root))

sys.path.append(deployment_root)  # path to pipeline 
sys.path.append(r'//multifct/tools/pipeline/global/packages')  # path to Qt package

print('Done Pipeline config')
