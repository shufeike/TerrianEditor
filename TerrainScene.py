__author__ = 'aaron'
import sys
import CellItem
from PyQt4 import QtCore, QtGui
class TerrainScene(QtGui.QGraphicsScene):
    def __init__(self, width=150, height=80):
        QtGui.QGraphicsScene.__init__(self)
        self.setSceneRect(0, 0, width, height)
        self.cellType = CellItem.CellItemType.CIT_DC
        self.seletecRect = QtCore.QRectF(0, 0, 0, 0)

    def mouseMoveEvent(self, event):
        if self.LeftButtonPressed:
            tmpPos = event.scenePos()
            rectPath = QtGui.QPainterPath()
            rectPath.addRect(self.pos.x(), self.pos.y(), tmpPos.x()-self.pos.x(), tmpPos.y() - self.pos.y())
            self.setSelectionArea(rectPath)
            for item in self.selectedItems():
                item.update()

    def mousePressEvent(self, event):
        self.pos =event.scenePos()
        #self.seletecRect.setRect(self.itemAt(self.pos).rect().x())
        #QtGui.QGraphicsScene.mousePressEvent(self, event)
        self.LeftButtonPressed = True;

    def mouseReleaseEvent(self, event):
        self.clearSelection()
        begItem = self.itemAt(self.pos)
        endItem = self.itemAt(event.scenePos())
        rectPath = QtGui.QPainterPath(self.pos)
        self.seletecRect.setRect(begItem.pos().x(), begItem.pos().y(), endItem.pos().x() + endItem.rect().width() - begItem.pos().x() , endItem.pos().y() + endItem.rect().height() - begItem.pos().y())
        #else:
            #self.seletecRect.setRect(self.pos.x(), self.pos.y(), releasePos.x()-self.pos.x(), releasePos.y() - self.pos.y())
        rectPath.addRect(self.seletecRect)
        self.setSelectionArea(rectPath)
        self.LeftButtonPressed = False;
        for cell in self.selectedItems():
                cell.SetType(self.cellType)
                cell.update()
        #self.update()


