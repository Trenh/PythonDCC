from engine import engine
import hou as hou

class HoudiniEngine(engine.Engine):
    def open(self, path):
        hou.hipFile.load(path)

    def save(self):
        pass

    def __str__ (self) :
        return 'Houdini Engine'