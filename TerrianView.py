__author__ = 'aaron'
from PyQt4 import QtGui, QtCore
class TerrianView(QtGui.QGraphicsView):
    def __init__(self, scene):
        QtGui.QGraphicsView.__init__(self, scene)
    def keyReleaseEvent(self, event):
        if event.key() == QtCore.Qt.Key_Equal:
            self.scale(1.1, 1.1)
        elif event.key() == QtCore.Qt.Key_Minus:
            self.scale(0.9, 0.9)
