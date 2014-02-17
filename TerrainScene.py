__author__ = 'aaron'
import sys
import CellItem
from PyQt4 import QtCore, QtGui
class TerrainScene(QtGui.QGraphicsScene):
    def __init__(self, width=150, height=80):
        QtGui.QGraphicsScene.__init__(self)
        self.setSceneRect(0, 0, width, height)
        #self.cell = CellItem.CellItem(100.0, 100.0)
        #self.addItem(self.cell)
    def mousePressEvent(self, event):
        i=0


