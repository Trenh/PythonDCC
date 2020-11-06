from pipeline.engine import engine
import maya.cmds as cmds
import subprocess


class MayaEngine(engine.Engine) :
    def open(self, path) :
        cmds.file(new = True, force = True)
        cmds.file(path, o = True)
        
    def save(self):
        cmds.file(rename="D:/Artfx/GarciaTD4/test.ma")
        cmds.file(save=True, type="mayaAscii")
        pass
    def __str__ (self) :
        return 'Maya Engine'