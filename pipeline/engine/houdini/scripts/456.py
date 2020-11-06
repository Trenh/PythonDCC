import sys
import hou
import os
print('Starting up the Pipeline')

here = hou.getenv('HOUDINI_SCRIPT_PATH').split(';') [-1]
deployment_root =here.split('/pipeline/')[0]


sys.path.append(deployment_root) #import path to project
#sys.path.append(os.path.join(deployment_root, 'pipeline')
sys.path.append(r'D:/Artfx/GarciaTD4/PythonDCC/QtLib')  #import QT lib

#from pipeline.ui import my_window as mw

#win = mw.MyWindow()
#win.show()


print('Done Pipeline config')