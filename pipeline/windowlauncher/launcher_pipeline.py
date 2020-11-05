import sys

if r"D:/Artfx/GarciaTD4/PythonDCC" not in sys.path:
    sys.path.append(r'D:/Artfx/GarciaTD4/PythonDCC')
    sys.path.append(r'D:/Artfx/GarciaTD4/PythonDCC/QtLib')

from pipeline.engine import engine
from Qt import QtWidgets
from pipeline.ui import my_window as mw

app = QtWidgets.QApplication(sys.argv)
win = mw.MyWindow()
win.show()

app.exec_()