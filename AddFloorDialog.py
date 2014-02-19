__author__ = 'aaron'
from PyQt4 import QtGui, QtCore
import Ui_AddFloor
import TerrainScene
import CellItem
class AddFloorDialog(QtGui.QFrame):
    def __init__(self):
        QtGui.QFrame.__init__(self)
        self.ui = Ui_AddFloor.Ui_Form()
        self.ui.setupUi(self)
        self.show();
        self.ui.spinBox.valueChanged.connect(self.drawScene)
        self.ui.spinBox_2.valueChanged.connect(self.drawScene)

        self.ui.rbDeskChair.toggled.connect(self.checkedDC)
        self.ui.rbNone.toggled.connect(self.checkedNone)
        self.ui.rbWall.toggled.connect(self.checkedWall)
        self.ui.rbFloor.toggled.connect(self.checkedFloor)
        self.ui.rbExit.toggled.connect(self.checkedExit)
        self.ui.rbParapet.toggled.connect(self.checkedParapet)
        self.ui.rbStair.toggled.connect(self.checkedStair)
        self.ui.rbIntersection.toggled.connect(self.checkedIntersection)

        self.ui.commit.accepted.connect(self.commit)
        self.ui.commit.rejected.connect(self.abort)
        self.scene = TerrainScene.TerrainScene(100, 100)
        self.ui.graphicsView.setScene(self.scene)

    def drawSceneFromFile(self, fileName):
        self.scene.clear()
        try:
            sceneFile = open(fileName, 'r')
            wh = sceneFile.readline().strip('\n').split(' ')
            self.length = float(wh[0])
            self.width = float(wh[1])
            self.ui.spinBox.setValue(self.length)
            self.ui.spinBox_2.setValue(self.width)
            self.scene.setSceneRect(-1, -1, self.length + 2, self.width + 2)
            for line in sceneFile:
                attrs = line.strip('\n').split(' ')
                cell = CellItem.CellItem()
                cell.SetType(int(attrs[4]))
                cell.setPos(float(attrs[1]), float(attrs[2]))
                cell.setToolTip('( ' + attrs[1] + ' ' + attrs[2] + ' )')
                self.scene.addItem(cell)
        finally:
            sceneFile.close()
        self.ui.graphicsView.centerOn(self.length / 2, self.width / 2)
        self.scene.update()
    def drawScene(self):
        self.length = self.ui.spinBox.value()
        self.width = self.ui.spinBox_2.value()
        self.scene.clear()
        self.scene.setSceneRect(-1, -1, self.length + 2, self.width + 2)
        for i in range(self.length):
            for j in range(self.width):
                cell = CellItem.CellItem()
                if i == 0 or i == self.length - 1 or j == 0 or j == self.width - 1:
                    cell.SetType(CellItem.CellItemType.CIT_WALL)
                else:
                    cell.SetType(CellItem.CellItemType.CIT_FLOOR)
                cell.setPos(i, j)
                self.scene.addItem(cell)
        self.ui.graphicsView.centerOn(self.length / 2, self.width / 2)
        self.scene.update()
    def checkedDC(self, checked):
        if checked:
            self.scene.cellType = CellItem.CellItemType.CIT_DC
    def checkedNone(self, checked):
        if checked:
            self.scene.cellType = CellItem.CellItemType.CIT_BLANK
    def checkedWall(self, checked):
        if checked:
            self.scene.cellType = CellItem.CellItemType.CIT_WALL
    def checkedFloor(self, checked):
        if checked:
            self.scene.cellType = CellItem.CellItemType.CIT_FLOOR
    def checkedIntersection(self, checked):
        if checked:
            self.scene.cellType = CellItem.CellItemType.CIT_INTERSECTION
    def checkedExit(self, checked):
        if checked:
            self.scene.cellType = CellItem.CellItemType.CIT_EXIT
    def checkedStair(self, checked):
        if checked:
            self.scene.cellType = CellItem.CellItemType.CIT_STAIR
    def checkedParapet(self, checked):
        if checked:
            self.scene.cellType = CellItem.CellItemType.CIT_PARAPET

    def commit(self):
        cells = self.scene.items();
        terrain = open('terrain.data', 'w')
        terrain.write(str(self.length) + ' ' + str(self.width) + '\n')
        count = 0
        for cell in cells:
            count += 1
            terrain.write(str(count) + ' ' + str(cell.pos().x()) + ' ' + str(cell.pos().y()) + ' 0 ' + str(cell.cellType) +  '\n')
        terrain.flush()
        terrain.close()
        self.close()
    def abort(self):
        self.close()
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Equal:
            self.ui.graphicsView.scale(1.5, 1.5)
        elif event.key() == QtCore.Qt.Key_Minus:
            self.ui.graphicsView.scale(0.75, 0.75)