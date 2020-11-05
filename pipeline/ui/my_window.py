import sys, os

sys.path.append(r'\\multifct\tools\pipeline\global\packages') # path to Qt package
sys.path.append(r'D:/Artfx/GarciaTD4')  # path to Qt package

sys.path.append(r'D:/Artfx/GarciaTD4/PythonDCC/pipeline')

from Qt import QtWidgets, QtCompat

ui_path = os.path.join(os.path.dirname(__file__), 'my_window.ui')

class MyWindow(QtWidgets.QMainWindow) :
    
    def __init__(self) :
        super(MyWindow, self).__init__()
        #self.engine = MayaEngine()
        path = ""
        
        from engine import engine
        self.engine = engine.get_current()
        
        # setup ui
        QtCompat.loadUi(ui_path, self) # replace self.setupUi(Self)
        self.open_button.clicked.connect(self.open)
        self.browse_button.clicked.connect(self.browse)
        
    def open(self) :
        print(self.path)
        self.engine.open(self.path)
        
    def browse(self) :
        self.path= QtWidgets.QFileDialog.getOpenFileName(self, "Open file")[0]
        print(self.path)