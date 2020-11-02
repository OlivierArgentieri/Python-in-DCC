import sys
import hou 

path_env = 'D:\Projet\Pull_github\Artfx_Courses\Haussman\PythonInDCC\PY_DCC' #Qt.py and libs path
if path_env not in sys.path:
    sys.path.append(path_env)
    # sys.path.insert(0, path_env) to add in top of paths
    
    
print("Starting up pipeline")
    
   