import sys
from PyQt4 import QtGui
import Ui_MainWindow
import AddFloorDialog
import  OpenFloorDialog
class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow.Ui_MainWindow();
        self.ui.setupUi(self);
        self.ui.actionNew.triggered.connect(self.newTriggered)
        self.ui.actionOpen.triggered.connect(self.openFile)
        self.ui.actionAddFloor.triggered.connect(self.addFloor)

    def newTriggered(self):
        i=0
    def openFile(self):
        self.addThing = OpenFloorDialog.OpenFloorDialog()
        self.addThing.drawSceneFromFile("terrain.data")
    def addFloor(self):
        self.addThing = AddFloorDialog.AddFloorDialog()

app = QtGui.QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
app.exec_()


