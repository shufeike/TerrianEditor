__author__ = 'aaron'
from PyQt4 import QtGui, QtCore
import Ui_OpenFloor
import TerrainScene
import CellItem
class OpenFloorDialog(QtGui.QFrame):
    def __init__(self):
        QtGui.QFrame.__init__(self)
        self.ui = Ui_OpenFloor.Ui_Form()
        self.ui.setupUi(self)
        self.show();

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
            self.ui.lbLength.setText(wh[0])
            self.ui.lbWidth.setText(wh[1])
            self.scene.setSceneRect(-1, -1, self.length + 2, self.width + 2)
            for line in sceneFile:
                attrs = line.strip('\n').split(' ')
                cell = CellItem.CellItem()
                cell.SetType(int(attrs[4]))
                cell.setPos(float(attrs[1]), float(attrs[2]))
                cell.setToolTip('( ' + attrs[1] + ' ' + attrs[2] + ' )')
                self.scene.addItem(cell)
        except IOError:
            exit(-2)
        finally:
            sceneFile.close()
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
        terrain.truncate()
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