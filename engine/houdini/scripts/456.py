import sys
import hou
import os
print('Starting up the Pipeline')

if '//multifct/tools/pipeline/global/packages' not in sys.path:

    sys.path.append(r'//multifct/tools/pipeline/global/packages')  # path to Qt package
    sys.path.append(r'D:/Artfx/GarciaTD4/PythonDCC/pipeline/engine/houdini/scripts')  # pipeline lib
    sys.path.append(r'D:/Artfx/GarciaTD4/PythonDCC/pipeline')  # ui lib

    from ui import my_window as mw

    win = mw.MyWindow()
    win.show()

print('Done with Pipeline config')