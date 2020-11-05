import sys,os
import maya.cmds as cmds
print('Starting up pipeline')


here = os.path.dirname(__file__)

deployment_root = here.split('/pipeline/')[0]
sys.path.append(deployment_root)  # path to pipeline 

#if r"D:/Artfx/GarciaTD4/PyhtonDCC" not in sys.path:
#    sys.path.append(r'//multifct/tools/pipeline/global/packages')  # path to Qt package
sys.path.append(r'D:/Artfx/GarciaTD4/PyhtonDCC/QtLib')  # path to Qt package
#   sys.path.append(r'D:/Artfx/GarciaTD4/PythonDCC') #import path to project

from pipeline.ui import my_window as mw

win = mw.MyWindow()
win.show()


print('Done Pipeline config')