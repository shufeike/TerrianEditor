__author__ = 'aaron'
import sys
from PyQt4 import QtCore, QtGui, QtOpenGL
class CellItemType(object):
    CIT_BLANK = 0 #black
    CIT_DC = 1 #desk and chair
    CIT_WALL = 2 #wall
    CIT_FLOOR = 3 #floor
    CIT_PARAPET = 4 #parapet
    CIT_STAIR = 5
    CIT_EXIT = 6
    CIT_INTERSECTION = 7
    CIT_TAIL = 8

class CellItem(QtGui.QGraphicsRectItem):
    def __init__(self, width=1, height=1):
        QtGui.QGraphicsRectItem.__init__(self, 0.0, 0.0, width, height)
        self.cellType = CellItemType.CIT_BLANK
        self.setFlag(QtGui.QGraphicsItem.ItemIsSelectable)
        self.hover = False
        self.brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
    def paint(self, painter, option, widget):
        if(self.cellType == CellItemType.CIT_BLANK):
            self.brush.setColor(QtGui.QColor(255, 255, 255))
        elif(self.cellType == CellItemType.CIT_WALL):
            self.brush.setColor(QtGui.QColor(0, 0, 0))
        elif(self.cellType == CellItemType.CIT_DC):
            self.brush.setColor(QtGui.QColor(0, 0, 255))
        elif(self.cellType == CellItemType.CIT_FLOOR):
            self.brush.setColor(QtGui.QColor(0, 255, 0))
        if self.isSelected():
            painter.setPen(QtGui.QColor(255, 0, 0))
        else:
            #self.brush.setColor(QtGui.QColor(255, 0, 0))
            painter.setPen(QtGui.QColor(0, 0, 0))
        painter.setBrush(self.brush)
        painter.drawRoundedRect(0, 0, 1, 1, 0.0, 0.0)

    def SetType(self, type):
        self.cellType = type
