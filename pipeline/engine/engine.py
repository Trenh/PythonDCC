import sys

class Engine(object) :
    def open(self,path) :
        pass
        
    def save(self) :
        pass

def get_current():
    engine = Engine()

    if 'maya' in sys.executable:
        from pipeline.engine import maya_engine
        engine = maya_engine.MayaEngine()

    if 'houdini' in sys.executable:
        from pipeline.engine import houdini_engine
        engine = houdini_engine.HoudiniEngine()
    
    return engine