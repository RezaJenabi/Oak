from PyQt6.QtWidgets import (
    QMainWindow
)
from PyQt6 import QtCore, QtGui, QtWidgets


class Oak(QMainWindow):

    __centralWidget, __horizontalLayoutWidget, __horizontalLayout, __objectExplorerWidget, __tabWidget = \
        None, None, None, None, None

    def __init__(self, parent=None):
        super().__init__(parent)
        self._init()

    def _init(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Oak"))
        self.setObjectName("MainWindow")
        self.resize(804, 803)
        self.setMinimumSize(QtCore.QSize(800, 100))
        self.setAcceptDrops(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./Assets/Images/Oak_clipartmax.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.setWindowIcon(icon)
        self.setStyleSheet("background-color: rgb(214, 219, 233);")
        self.setAnimated(True)
        self.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)

        self._createCentralWidget()
        self._createHorizontalLayoutWidget()
        self._createHorizontalLayout()
        self._createObjectExplorerWidget()
        self._createTabWidget()
        self._createMenuBar()
        QtCore.QMetaObject.connectSlotsByName(self)

    def _createMenuBar(self):
        # menu bar
        self.menubar = QtWidgets.QMenuBar(parent=self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 804, 21))
        self.menubar.setStyleSheet("background-color: rgb(214, 219, 233);border-color: rgb(148, 152, 161);")
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(parent=self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuNew = QtWidgets.QMenu(parent=self.menuFile)
        self.menuNew.setObjectName("menuNew")
        self.menuEdit = QtWidgets.QMenu(parent=self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QtWidgets.QMenu(parent=self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.setMenuBar(self.menubar)

        # tab bar
        self.toolBar = QtWidgets.QToolBar(parent=self)
        self.toolBar.setMouseTracking(True)
        self.toolBar.setAcceptDrops(False)
        self.toolBar.setObjectName("toolBar")
        self.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.actionConnect_Object_Explrer = QtGui.QAction(parent=self)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./Assets/Images/ssms.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionConnect_Object_Explrer.setIcon(icon2)
        self.actionConnect_Object_Explrer.setObjectName("actionConnect_Object_Explrer")

        self.actionDisconnect_Object_Explorer = QtGui.QAction(parent=self)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("./Assets/Images/status_ico_error.png"), QtGui.QIcon.Mode.Normal,
                        QtGui.QIcon.State.Off)
        self.actionDisconnect_Object_Explorer.setIcon(icon3)
        self.actionDisconnect_Object_Explorer.setObjectName("actionDisconnect_Object_Explorer")

        self.actionSave = QtGui.QAction(parent=self)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("./Assets/Images/status_ico_trusted.png"), QtGui.QIcon.Mode.Normal,
                        QtGui.QIcon.State.Off)
        self.actionSave.setIcon(icon4)
        self.actionSave.setObjectName("actionSave")

        self.actionSave_All = QtGui.QAction(parent=self)
        self.actionSave_All.setObjectName("actionSave_All")

        self.actionCPU = QtGui.QAction(parent=self)
        self.actionCPU.setObjectName("actionCPU")

        self.actionMemory = QtGui.QAction(parent=self)
        self.actionMemory.setObjectName("actionMemory")

        self.actionLock = QtGui.QAction(parent=self)
        self.actionLock.setObjectName("actionLock")

        self.menuNew.addAction(self.actionCPU)
        self.menuNew.addAction(self.actionMemory)
        self.menuNew.addAction(self.actionLock)
        self.menuFile.addAction(self.actionConnect_Object_Explrer)
        self.menuFile.addAction(self.actionDisconnect_Object_Explorer)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.menuNew.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_All)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.toolBar.addAction(self.actionConnect_Object_Explrer)
        self.toolBar.addAction(self.actionDisconnect_Object_Explorer)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSave)

        _translate = QtCore.QCoreApplication.translate

        self.menuFile.setTitle("File")
        self.menuNew.setTitle(_translate("MainWindow", "New"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionConnect_Object_Explrer.setText(_translate("MainWindow", "Connect Object Explrer"))
        self.actionConnect_Object_Explrer.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionDisconnect_Object_Explorer.setText(_translate("MainWindow", "Disconnect Object Explrer"))
        self.actionDisconnect_Object_Explorer.setShortcut(_translate("MainWindow", "Ctrl+D"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionSave_All.setText(_translate("MainWindow", "Save All"))
        self.actionSave_All.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        self.actionCPU.setText(_translate("MainWindow", "CPU"))
        self.actionMemory.setText(_translate("MainWindow", "Memory"))
        self.actionLock.setText(_translate("MainWindow", "Lock"))
        self.actionLock.setShortcut(_translate("MainWindow", "Ctrl+Shift+L"))

    def _createToolBar(self):
        pass

    def _createObjectExplorerWidget(self):
        self.__objectExplorerWidget = QtWidgets.QTreeWidget(parent=self.__horizontalLayoutWidget)
        self.__objectExplorerWidget.setMaximumSize(QtCore.QSize(200, 16777215))
        self.__objectExplorerWidget.setObjectName("objectExplorerWidget")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../Assets/Images/DatabaseProject.ico"), QtGui.QIcon.Mode.Normal,
                        QtGui.QIcon.State.Off)
        self.__objectExplorerWidget.headerItem().setIcon(0, icon1)

        item_0 = QtWidgets.QTreeWidgetItem(self.__objectExplorerWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.__objectExplorerWidget)

        self.__horizontalLayout.addWidget(self.__objectExplorerWidget)

        _translate = QtCore.QCoreApplication.translate
        self.__objectExplorerWidget.headerItem().setText(0, "Object Explorer")
        __sortingEnabled = self.__objectExplorerWidget.isSortingEnabled()
        self.__objectExplorerWidget.setSortingEnabled(False)
        self.__objectExplorerWidget.topLevelItem(0).setText(0, "First")
        self.__objectExplorerWidget.topLevelItem(1).setText(0, "Second")

        self.__objectExplorerWidget.setSortingEnabled(__sortingEnabled)

    def _createHorizontalLayoutWidget(self):
        self.__horizontalLayoutWidget = QtWidgets.QWidget(parent=self.__centralWidget)
        self.__horizontalLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 801, 741))
        self.__horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")

    def _createHorizontalLayout(self):
        self.__horizontalLayout = QtWidgets.QHBoxLayout(self.__horizontalLayoutWidget)
        self.__horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.__horizontalLayout.setObjectName("horizontalLayout")

    def _createCentralWidget(self):
        self.__centralWidget = QtWidgets.QWidget(parent=self)
        self.__centralWidget.setObjectName("centralwidget")
        self.setCentralWidget(self.__centralWidget)

    def _createTabWidget(self):
        self.__tabWidget = QtWidgets.QTabWidget(parent=self.__horizontalLayoutWidget)
        self.__tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.__tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.__tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.__tabWidget.addTab(self.tab_2, "")
        self.__horizontalLayout.addWidget(self.__tabWidget)
        self.__tabWidget.setCurrentIndex(0)

        self.__tabWidget.setTabText(self.__tabWidget.indexOf(self.tab), "Tab 1")
        self.__tabWidget.setTabText(self.__tabWidget.indexOf(self.tab_3), "Page")
        self.__tabWidget.setTabText(self.__tabWidget.indexOf(self.tab_2), "Tab 2")


