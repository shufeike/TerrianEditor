import sys
import numpy as np
terrain = open('terrain.data', 'w')
xl = 150; yl = 80; cellSize = 0.5;
count = 0;
step = 5
for px in np.arange(0, xl, step):
    for py in np.arange(0, yl, step):
        terrain.write(str(++count) + ' ' + str(px) + ' ' + str(py) + ' 0 1 \n')
terrain.flush()
terrain.close()
import TerrainScene
import CellItem
from PyQt4 import QtCore, QtGui
class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.terrainScene = TerrainScene.TerrainScene(xl // cellSize, yl // cellSize)
        self.cells = []
        for px in np.arange(0, xl // cellSize, 1):
            for py in np.arange(0, yl // cellSize, 1):
                cell = CellItem.CellItem();
                cell.setPos(px * cell.rect().width(), py * cell.rect().height())
                self.terrainScene.addItem(cell)
                #self.cells.append(CellItem.CellItem())
                #self.cells[-1].setPos(px * 10, py * 10)
                #self.terrainScene.addItem(self.cells[-1])
        self.view = QtGui.QGraphicsView(self.terrainScene)
        self.view.centerOn(self.terrainScene.width() / 2, self.terrainScene.height() / 2)
        self.view.scale(30, 30)
        #self.view.setupViewport()
        self.setCentralWidget(self.view)


app = QtGui.QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
app.exec_()


