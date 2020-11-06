import sys

class Engine(object) :
    def open(self,path) :
        pass
        
    def save(self) :
        pass

    def export(self, path):
        mayabat = "C:/Program Files/Autodesk/Maya2020/bin/mayabatch.exe"
        
def get_current():
    engine = Engine()

    if 'maya' in sys.executable:
        from pipeline.engine import maya_engine
        engine = maya_engine.MayaEngine()

    if 'houdini' in sys.executable:
        from pipeline.engine import houdini_engine
        engine = houdini_engine.HoudiniEngine()
    
    return engine