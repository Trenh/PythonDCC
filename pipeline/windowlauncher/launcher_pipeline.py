import sys

sys.path.append(r'D:/Artfx/GarciaTD4/PythonDCC/pipeline')
sys.path.append(r'D:/Artfx/GarciaTD4/PythonDCC/QtLib')

from pipeline.engine import engine
from Qt import QtWidgets

app = QtWidgets.QApplication(sys.argv)

engine.get_current()

win = engine.MyWindow()
win.show()

app.exec_()