# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AttractModeMameListMgrWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(906, 525)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.dupBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dupBtn.sizePolicy().hasHeightForWidth())
        self.dupBtn.setSizePolicy(sizePolicy)
        self.dupBtn.setObjectName("dupBtn")
        self.gridLayout.addWidget(self.dupBtn, 2, 6, 1, 1)
        self.clearSearchBtn = QtWidgets.QPushButton(self.centralwidget)
        self.clearSearchBtn.setObjectName("clearSearchBtn")
        self.gridLayout.addWidget(self.clearSearchBtn, 2, 7, 1, 1)
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy)
        self.treeWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.treeWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.treeWidget.setColumnCount(4)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        self.treeWidget.headerItem().setText(1, "2")
        self.treeWidget.headerItem().setText(2, "3")
        self.treeWidget.headerItem().setText(3, "4")
        self.gridLayout.addWidget(self.treeWidget, 3, 0, 1, 10)
        self.searchLabel = QtWidgets.QLabel(self.centralwidget)
        self.searchLabel.setObjectName("searchLabel")
        self.gridLayout.addWidget(self.searchLabel, 2, 0, 1, 1)
        self.mameExeBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mameExeBtn.sizePolicy().hasHeightForWidth())
        self.mameExeBtn.setSizePolicy(sizePolicy)
        self.mameExeBtn.setMaximumSize(QtCore.QSize(25, 16777215))
        self.mameExeBtn.setObjectName("mameExeBtn")
        self.gridLayout.addWidget(self.mameExeBtn, 1, 5, 1, 1)
        self.amDir = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.amDir.sizePolicy().hasHeightForWidth())
        self.amDir.setSizePolicy(sizePolicy)
        self.amDir.setMinimumSize(QtCore.QSize(300, 0))
        self.amDir.setObjectName("amDir")
        self.gridLayout.addWidget(self.amDir, 0, 1, 1, 4)
        self.mameExe = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mameExe.sizePolicy().hasHeightForWidth())
        self.mameExe.setSizePolicy(sizePolicy)
        self.mameExe.setMinimumSize(QtCore.QSize(300, 0))
        self.mameExe.setObjectName("mameExe")
        self.gridLayout.addWidget(self.mameExe, 1, 1, 1, 4)
        self.amDirLbl = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.amDirLbl.sizePolicy().hasHeightForWidth())
        self.amDirLbl.setSizePolicy(sizePolicy)
        self.amDirLbl.setObjectName("amDirLbl")
        self.gridLayout.addWidget(self.amDirLbl, 0, 0, 1, 1)
        self.amDirBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.amDirBtn.sizePolicy().hasHeightForWidth())
        self.amDirBtn.setSizePolicy(sizePolicy)
        self.amDirBtn.setMaximumSize(QtCore.QSize(25, 16777215))
        self.amDirBtn.setObjectName("amDirBtn")
        self.gridLayout.addWidget(self.amDirBtn, 0, 5, 1, 1)
        self.searchBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchBtn.sizePolicy().hasHeightForWidth())
        self.searchBtn.setSizePolicy(sizePolicy)
        self.searchBtn.setMaximumSize(QtCore.QSize(25, 16777215))
        self.searchBtn.setObjectName("searchBtn")
        self.gridLayout.addWidget(self.searchBtn, 2, 5, 1, 1)
        self.mameExeLbl = QtWidgets.QLabel(self.centralwidget)
        self.mameExeLbl.setObjectName("mameExeLbl")
        self.gridLayout.addWidget(self.mameExeLbl, 1, 0, 1, 1)
        self.searchLine = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchLine.sizePolicy().hasHeightForWidth())
        self.searchLine.setSizePolicy(sizePolicy)
        self.searchLine.setMinimumSize(QtCore.QSize(300, 0))
        self.searchLine.setObjectName("searchLine")
        self.gridLayout.addWidget(self.searchLine, 2, 1, 1, 4)
        self.expColBtn = QtWidgets.QPushButton(self.centralwidget)
        self.expColBtn.setObjectName("expColBtn")
        self.gridLayout.addWidget(self.expColBtn, 1, 6, 1, 1)
        self.saveConfigBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveConfigBtn.sizePolicy().hasHeightForWidth())
        self.saveConfigBtn.setSizePolicy(sizePolicy)
        self.saveConfigBtn.setObjectName("saveConfigBtn")
        self.gridLayout.addWidget(self.saveConfigBtn, 0, 6, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(135, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 9, 1, 1)
        self.lockBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lockBtn.sizePolicy().hasHeightForWidth())
        self.lockBtn.setSizePolicy(sizePolicy)
        self.lockBtn.setObjectName("lockBtn")
        self.gridLayout.addWidget(self.lockBtn, 1, 8, 1, 1)
        self.startBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startBtn.sizePolicy().hasHeightForWidth())
        self.startBtn.setSizePolicy(sizePolicy)
        self.startBtn.setObjectName("startBtn")
        self.gridLayout.addWidget(self.startBtn, 2, 8, 1, 1)
        self.cloneBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cloneBtn.sizePolicy().hasHeightForWidth())
        self.cloneBtn.setSizePolicy(sizePolicy)
        self.cloneBtn.setObjectName("cloneBtn")
        self.gridLayout.addWidget(self.cloneBtn, 0, 8, 1, 1)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(80, 60))
        self.frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(1)
        self.frame.setMidLineWidth(1)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(11, -4, 58, 28))
        self.label.setObjectName("label")
        self.parentBtn = QtWidgets.QRadioButton(self.frame)
        self.parentBtn.setGeometry(QtCore.QRect(5, 22, 56, 17))
        self.parentBtn.setObjectName("parentBtn")
        self.titleBtn = QtWidgets.QRadioButton(self.frame)
        self.titleBtn.setGeometry(QtCore.QRect(5, 39, 44, 17))
        self.titleBtn.setObjectName("titleBtn")
        self.gridLayout.addWidget(self.frame, 0, 7, 2, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 906, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.dupBtn.setText(_translate("MainWindow", "Find Duplicates"))
        self.clearSearchBtn.setText(_translate("MainWindow", "Clear Search"))
        self.treeWidget.setSortingEnabled(True)
        self.searchLabel.setText(_translate("MainWindow", "Search"))
        self.mameExeBtn.setText(_translate("MainWindow", "..."))
        self.amDirLbl.setText(_translate("MainWindow", "AttractMode Directory"))
        self.amDirBtn.setText(_translate("MainWindow", "..."))
        self.searchBtn.setText(_translate("MainWindow", "Go"))
        self.mameExeLbl.setText(_translate("MainWindow", "Mame Executable"))
        self.expColBtn.setText(_translate("MainWindow", "Expand"))
        self.saveConfigBtn.setText(_translate("MainWindow", "Save Config"))
        self.lockBtn.setText(_translate("MainWindow", "Lock Selected"))
        self.startBtn.setText(_translate("MainWindow", "Validate"))
        self.cloneBtn.setText(_translate("MainWindow", "Unselect Clones"))
        self.label.setText(_translate("MainWindow", "Group Mode"))
        self.parentBtn.setText(_translate("MainWindow", "Parent"))
        self.titleBtn.setText(_translate("MainWindow", "Title"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
