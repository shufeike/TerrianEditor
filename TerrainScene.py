__author__ = 'aaron'
import sys
import CellItem
from PyQt4 import QtCore, QtGui
class TerrainScene(QtGui.QGraphicsScene):
    def __init__(self, width=150, height=80):
        QtGui.QGraphicsScene.__init__(self)
        self.setSceneRect(-1, -1, width + 2, height + 2)
        self.cellType = CellItem.CellItemType.CIT_BLANK

    def mouseMoveEvent(self, event):
        if self.LeftButtonPressed:
            tmpPos = event.scenePos()
            rectPath = QtGui.QPainterPath()
            rectPath.addRect(self.begPos.x(), self.begPos.y(), tmpPos.x()-self.begPos.x(), tmpPos.y() - self.begPos.y())
            self.setSelectionArea(rectPath)
            for item in self.selectedItems():
                item.update()

    def mousePressEvent(self, event):
        self.begPos =event.scenePos()
        self.LeftButtonPressed = True;
        QtGui.QGraphicsScene.mousePressEvent(self, event)

    def mouseReleaseEvent(self, event):
        self.clearSelection()
        if self.begPos == event.scenePos():
            i = 1;
        else :
            rectPath = QtGui.QPainterPath()
            rectPath.addRect(self.begPos.x(), self.begPos.y(), event.scenePos().x() - self.begPos.x(), event.scenePos().y() - self.begPos.y())
            self.setSelectionArea(rectPath)
        self.LeftButtonPressed = False;
        for cell in self.selectedItems():
            if self.cellType != CellItem.CellItemType.CIT_BLANK:
                cell.SetType(self.cellType)
            cell.update()
        QtGui.QGraphicsScene.mouseReleaseEvent(self, event)


