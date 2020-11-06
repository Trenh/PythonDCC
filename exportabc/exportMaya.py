import maya.cmds as cmds
from pipeline.engine import engine
import sys

cmds.loadPlugin( 'AbcExport.mll' )

cmds.file(sys.argv[3], o=True )

command = "-frameRange 1 25 -uvWrite -dataFormat ogawa -root " + engine.exportObjectName + " -file D:/Artfx/GarciaTD4/PythonDCC/exportabc/exportedABC/" + engine.exportObjectName + ".abc"
cmds.AbcExport( j =command)