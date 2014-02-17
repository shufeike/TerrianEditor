__author__ = 'aaron'
import sys
from PyQt4 import QtCore, QtGui, QtOpenGL
class CellItemType(object):
    CIT_BLANK = 0 #black
    CIT_DC = 1 #desk and chair
    CIT_WALL = 2 #wall
    CIT_FLOOR = 3 #floor
    CIT_TAIL = 4

class CellItem(QtGui.QGraphicsRectItem):
    def __init__(self, width=1, height=1):
        QtGui.QGraphicsRectItem.__init__(self, 0.0, 0.0, width, height)
        self.cellType = CellItemType.CIT_BLANK
    def paint(self, painter, option, widget):
        #painter.drawPixmap(QtCore.QRect(0, 0, self.rect().width(), self.rect().width()), self.pixmap)
        painter.setPen(QtGui.QColor(255, 0, 0))
        if(self.cellType == CellItemType.CIT_BLANK):
            painter.setBrush(QtGui.QColor(255, 255, 255))
            #painter.setBrush(QtGui.QColor(0, 0, 0))
            #painter.drawRoundedRect(0, 0, 1, 1, 0.1, 0.1)
        elif(self.cellType == CellItemType.CIT_WALL):
            painter.setBrush(QtGui.QColor(100, 100, 100))
        elif(self.cellType == CellItemType.CIT_DC):
            painter.setBrush(QtGui.QColor(0, 0, 255))
        elif(self.cellType == CellItemType.CIT_FLOOR):
            painter.setBrush(QtGui.QColor(0, 255, 0))
        painter.drawRoundedRect(0, 0, 1, 1, 0.1, 0.1)
    def mousePressEvent(self, event):
        self.cellType = self.cellType + 1
        self.cellType %=  CellItemType.CIT_TAIL
        self.update()

