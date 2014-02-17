__author__ = 'aaron'
import sys
from PyQt4 import QtCore, QtGui, QtOpenGL
class CellItem(QtGui.QGraphicsRectItem):
    def __init__(self, width=1, height=1):
        QtGui.QGraphicsRectItem.__init__(self, 0.0, 0.0, width, height)
        self.pixmap = QtGui.QPixmap('terrain.bmp');
    def paint(self, painter, option, widget):
        painter.drawPixmap(QtCore.QRect(0, 0, self.rect().width(), self.rect().width()), self.pixmap)
        if()
