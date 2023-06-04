from PyQt6.QtGui import QAction, QColor, QBrush
from PyQt6.QtWidgets import (
    QMainWindow, QMenu
)
from PyQt6 import QtCore, QtGui, QtWidgets


class Oak(QMainWindow):

    __centralWidget, __horizontalLayoutWidget, __horizontalLayout, __objectExplorerWidget, __tabWidget,\
        __menubar, __toolBar = \
        None, None, None, None, None, None, None

    def __init__(self, parent=None):
        super().__init__(parent)
        self._init()
        self._createCentralWidget()
        self._createHorizontalLayoutWidget()
        self._createHorizontalLayout()
        self._createMenuBar()
        self._createToolBar()
        self._createObjectExplorerWidget()
        self._createTabWidget()

    def _init(self):
        self.setWindowTitle("Oak")
        self.setObjectName("MainWindow")
        self.resize(804, 803)
        self.setMinimumSize(QtCore.QSize(800, 100))
        self.setAcceptDrops(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./Assets/icons/project/Oak_clipartmax.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.setWindowIcon(icon)
        self.setStyleSheet("background-color: rgb(214, 219, 233);")
        self.setAnimated(True)
        self.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        QtCore.QMetaObject.connectSlotsByName(self)

    def _createMenuBar(self):
        self.__menubar = QtWidgets.QMenuBar(parent=self)
        self.__menubar.setGeometry(QtCore.QRect(0, 0, 804, 21))
        self.__menubar.setStyleSheet("background-color: rgb(214, 219, 233);border-color: rgb(148, 152, 161);")
        self.__menubar.setObjectName("menubar")
        self.menuFile = self._createMenuBarNode(self.__menubar, "File")
        self.menuNew = self._createMenuBarNode(self.__menubar, "New")
        self.menuEdit = self._createMenuBarNode(self.__menubar, "Edit")
        self.menuHelp = self._createMenuBarNode(self.__menubar, "Help")
        self.setMenuBar(self.__menubar)

        self.actionConnectObjectExplorer = self._createMenuBarAction(self, "Connect Object Explorer",
                                                                       self._createObjectExplorerItem,
                                                                       "../Assets/icons/icons/plug-connect.png", "Ctrl+C")

        self.actionDisconnectObjectExplorer = self._createMenuBarAction(self, "Disconnect Object Explorer",
                                                                       self._createNewTab,
                                                                       "../Assets/icons/icons/plug-disconnect.png",
                                                                          "Ctrl+D")
        self.actionSave = self._createMenuBarAction(self, "Save",
                                                                       self._createNewTab,
                                                                       "../Assets/Images/status_ico_error.png",
                                                                          "Ctrl+S")
        self.actionCPU = self._createMenuBarAction(self, "CPU",
                                                                       self._createNewTab,
                                                                       "../Assets/Images/status_ico_error.png",
                                                                          "Ctrl+Shift+C")

        self.menuNew.addAction(self.actionCPU)
        self.menuFile.addAction(self.actionConnectObjectExplorer)
        self.menuFile.addAction(self.actionDisconnectObjectExplorer)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.menuNew.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.__menubar.addAction(self.menuFile.menuAction())
        self.__menubar.addAction(self.menuEdit.menuAction())
        self.__menubar.addAction(self.menuHelp.menuAction())

    def _createToolBar(self):
        self.__toolBar = QtWidgets.QToolBar(parent=self)
        self.__toolBar.setIconSize(QtCore.QSize(15, 15))
        self.__toolBar.setMouseTracking(True)
        self.__toolBar.setAcceptDrops(False)
        self.__toolBar.setObjectName("toolBar")
        self.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.__toolBar)
        self.__toolBar.addAction(self.actionConnectObjectExplorer)
        self.__toolBar.addAction(self.actionDisconnectObjectExplorer)
        self.__toolBar.addSeparator()
        self.__toolBar.addAction(self.actionSave)
        self.__toolBar.setWindowTitle("toolBar")

    def _createObjectExplorerWidget(self):
        self.__objectExplorerWidget = QtWidgets.QTreeWidget(parent=self.__horizontalLayoutWidget)
        self.__objectExplorerWidget.itemDoubleClicked.connect(self.onObjectExplorerItemDoubleClicked)
        # self.__objectExplorerWidget.setStyleSheet("background-color: #fff29d;")
        self.__objectExplorerWidget.setMaximumSize(QtCore.QSize(250, 16777215))
        self.__objectExplorerWidget.setObjectName("objectExplorerWidget")

        self.__objectExplorerWidget.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.CustomContextMenu)
        self.__objectExplorerWidget.customContextMenuRequested.connect(self._showObjectExplorerRightClickMenu)

        self.__objectExplorerWidget.headerItem().setText(0, "Object Explorer")

        # brush = QBrush()
        # brush.setColor(QColor().blue())
        # self.__objectExplorerWidget.headerItem().setBackground(0, brush)
        __sortingEnabled = self.__objectExplorerWidget.isSortingEnabled()
        self.__objectExplorerWidget.setSortingEnabled(False)
        self.__objectExplorerWidget.setSortingEnabled(__sortingEnabled)
        self.__horizontalLayout.addWidget(self.__objectExplorerWidget)

    def _createObjectExplorerItem(self):
        parent = QtWidgets.QTreeWidgetItem(self.__objectExplorerWidget)
        parent.setText(0, "ServerName")
        child = QtWidgets.QTreeWidgetItem(parent)
        child.setText(0, "Databases")
        child = QtWidgets.QTreeWidgetItem(parent)
        child.setText(0, "Views")
        self.__objectExplorerWidget.addTopLevelItem(parent)

    @QtCore.pyqtSlot(QtWidgets.QTreeWidgetItem, int)
    def onObjectExplorerItemDoubleClicked(self):
        gp = QtGui.QCursor.pos()
        point = self.__objectExplorerWidget.viewport().mapFromGlobal(gp)
        item = self.__objectExplorerWidget.itemAt(point)
        childCount = item.childCount()
        if childCount is not None:
            for i in reversed(range(childCount)):
                item.removeChild(item.child(i))

        child = QtWidgets.QTreeWidgetItem(item)
        child.setText(0, "ddd")
        # item_1 = QtWidgets.QTreeWidgetItem(item_0)

    def _showObjectExplorerRightClickMenu(self, position):
        display_action1 = self.actionConnectObjectExplorer
        # display_action1 = QAction("Display Selection")
        # display_action1.triggered.connect(self.display_selection)
        menu = QMenu(self.__objectExplorerWidget)
        menu.addAction(display_action1)
        menu.exec(self.__objectExplorerWidget.mapToGlobal(position))

    # the action executed when menu is clicked
    # def _sampleActionRightClickSelection(self):
    #     column = self.__objectExplorerWidget.currentColumn()
    #     text = self.__objectExplorerWidget.currentItem().text(column)
    #     print("right-clicked item is " + text)

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
        self.__horizontalLayout.addWidget(self.__tabWidget)

    def _createNewTab(self):
        name = 'test'
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName(name)
        self.tab.acceptDrops()
        self.__tabWidget.addTab(self.tab, "")
        self.__tabWidget.setTabText(self.__tabWidget.indexOf(self.tab), name)

    def _createMenuBarNode(self, parent: QtWidgets.QMenu, name: str):
        menuNode = QtWidgets.QMenu(parent=parent)
        menuNode.setObjectName(name)
        menuNode.setTitle(name)
        return menuNode

    def _createMenuBarAction(self, parent, name, event, iconPath=None, shortcut=None):
        action = QtGui.QAction(parent=parent)
        if iconPath is not None:
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(iconPath), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            action.setIcon(icon)
            action.setObjectName(name)
            action.setText(name)
        if shortcut is not None:
            action.setShortcut(shortcut)
        action.triggered.connect(event)
        return action



