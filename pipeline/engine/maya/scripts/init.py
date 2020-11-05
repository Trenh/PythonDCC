import sys
import maya.cmds as cmds
import os
print('Starting up pipeline')

if r"C:\Users\Asus\Desktop\WSPython2020" not in sys.path:
    sys.path.append(r'//multifct/tools/pipeline/global/packages')  # path to Qt package
    sys.path.append(r'D:/Artfx/GarciaTD4')  # path to Qt package
    sys.path.append(r'D:/Artfx/GarciaTD4/PythonDCC/pipeline/') #import path to project

from ui import my_window as mw

win = mw.MyWindow()
win.show()


print('Done Pipeline config')