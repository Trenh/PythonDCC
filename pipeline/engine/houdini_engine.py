from pipeline.engine import engine
import hou as hou

class HoudiniEngine(engine.Engine):
    def open(self, path):
        hou.hipFile.load(path)

    def save(self):
        hou.hipfile.save("D:/Artfx/GarciaTD4/testfile.hip")

    def __str__ (self) :
        return 'Houdini Engine'