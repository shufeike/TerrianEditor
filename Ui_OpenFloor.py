# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OpenFloor.ui'
#
# Created: Wed Feb 19 21:15:51 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(670, 399)
        self.horizontalLayout_2 = QtGui.QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.graphicsView = QtGui.QGraphicsView(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.horizontalLayout_2.addWidget(self.graphicsView)
        self.frame = QtGui.QFrame(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(self.frame)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.rbNone = QtGui.QRadioButton(self.groupBox)
        self.rbNone.setObjectName(_fromUtf8("rbNone"))
        self.verticalLayout_3.addWidget(self.rbNone)
        self.rbFloor = QtGui.QRadioButton(self.groupBox)
        self.rbFloor.setObjectName(_fromUtf8("rbFloor"))
        self.verticalLayout_3.addWidget(self.rbFloor)
        self.rbWall = QtGui.QRadioButton(self.groupBox)
        self.rbWall.setObjectName(_fromUtf8("rbWall"))
        self.verticalLayout_3.addWidget(self.rbWall)
        self.rbExit = QtGui.QRadioButton(self.groupBox)
        self.rbExit.setObjectName(_fromUtf8("rbExit"))
        self.verticalLayout_3.addWidget(self.rbExit)
        self.rbDeskChair = QtGui.QRadioButton(self.groupBox)
        self.rbDeskChair.setObjectName(_fromUtf8("rbDeskChair"))
        self.verticalLayout_3.addWidget(self.rbDeskChair)
        self.rbIntersection = QtGui.QRadioButton(self.groupBox)
        self.rbIntersection.setObjectName(_fromUtf8("rbIntersection"))
        self.verticalLayout_3.addWidget(self.rbIntersection)
        self.rbParapet = QtGui.QRadioButton(self.groupBox)
        self.rbParapet.setObjectName(_fromUtf8("rbParapet"))
        self.verticalLayout_3.addWidget(self.rbParapet)
        self.rbStair = QtGui.QRadioButton(self.groupBox)
        self.rbStair.setObjectName(_fromUtf8("rbStair"))
        self.verticalLayout_3.addWidget(self.rbStair)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(self.frame)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lbLength = QtGui.QLabel(self.groupBox_2)
        self.lbLength.setObjectName(_fromUtf8("lbLength"))
        self.horizontalLayout.addWidget(self.lbLength)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        self.lbWidth = QtGui.QLabel(self.groupBox_2)
        self.lbWidth.setObjectName(_fromUtf8("lbWidth"))
        self.horizontalLayout_3.addWidget(self.lbWidth)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.commit = QtGui.QDialogButtonBox(self.frame)
        self.commit.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.commit.setObjectName(_fromUtf8("commit"))
        self.verticalLayout.addWidget(self.commit)
        self.horizontalLayout_2.addWidget(self.frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.groupBox.setTitle(_translate("Form", "Create", None))
        self.rbNone.setText(_translate("Form", "None", None))
        self.rbFloor.setText(_translate("Form", "Floor", None))
        self.rbWall.setText(_translate("Form", "Wall", None))
        self.rbExit.setText(_translate("Form", "Exit", None))
        self.rbDeskChair.setText(_translate("Form", "DeskChair", None))
        self.rbIntersection.setText(_translate("Form", "Intersection", None))
        self.rbParapet.setText(_translate("Form", "Parapet", None))
        self.rbStair.setText(_translate("Form", "Stair", None))
        self.groupBox_2.setTitle(_translate("Form", "Size", None))
        self.label.setText(_translate("Form", "Length:", None))
        self.lbLength.setText(_translate("Form", "0", None))
        self.label_2.setText(_translate("Form", "Width:", None))
        self.lbWidth.setText(_translate("Form", "0", None))

