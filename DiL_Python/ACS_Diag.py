from pyqtgraph.Qt import QtCore, QtGui
import numpy as np
import pyqtgraph as pg


app=QtGui.QApplication([])
w=pg.GraphicsWindow(size=(800,800),border=True)
v=w.addViewBox(colspan=2)


## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if sys.flags.interactive != 1 or not hasattr(pg.QtCore, 'PYQT_VERSION'):
        pg.QtGui.QApplication.exec_()
