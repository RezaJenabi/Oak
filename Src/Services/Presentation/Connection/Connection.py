from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget


class Window(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._init()
        self._MainLayout()
        self._createHeader()
        self._createHeaderLine()
        self._createForm()

    def _init(self):
        self.setObjectName("ConnectToServer")
        self.setWindowTitle("Connect to Server")
        self.resize(480, 250)
        self.setMinimumSize(QtCore.QSize(480, 250))

    def _MainLayout(self):
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 481, 241))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
    def _createHeaderLine(self):
        self.line = QtWidgets.QFrame(parent=self.verticalLayoutWidget)
        self.line.setMinimumSize(QtCore.QSize(0, 2))
        self.line.setMaximumSize(QtCore.QSize(16777215, 1))
        self.line.setStyleSheet("background-color: rgb(254, 135, 24);")
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)

    def _createHeader(self):
        self.Header = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.Header.setMaximumSize(QtCore.QSize(480, 65))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(25)
        self.Header.setFont(font)
        self.Header.setStyleSheet("color: rgb(56, 56, 56);\n"
                                  "background-color: rgb(240, 240, 240);")
        self.Header.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Header.setObjectName("Header")
        self.Header.setText("SQL Server")
        self.verticalLayout.addWidget(self.Header)

    def _createForm(self):
        verticalLayoutForm = QtWidgets.QVBoxLayout()
        verticalLayoutForm.setContentsMargins(10, 10, 10, 10)
        verticalLayoutForm.setSpacing(0)
        verticalLayoutForm.setObjectName("verticalLayoutForm")

        firstFormLayout = QtWidgets.QFormLayout()
        firstFormLayout.setContentsMargins(0, 0, 0, 0)
        firstFormLayout.setHorizontalSpacing(10)
        firstFormLayout.setVerticalSpacing(5)
        firstFormLayout.setObjectName("firstFormLayout")

        self.label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.label.setText("Server name:")
        firstFormLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)

        self.lineEdit = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.lineEdit.setMaximumSize(QtCore.QSize(300, 16777215))
        self.lineEdit.setObjectName("lineEdit")
        firstFormLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit)


        self.label_2 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.label_2.setText("Authentication:")
        firstFormLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
        self.comboBox = QtWidgets.QComboBox(parent=self.verticalLayoutWidget)
        self.comboBox.setMinimumSize(QtCore.QSize(300, 0))
        self.comboBox.setMaximumSize(QtCore.QSize(300, 16777215))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setItemText(0, "Windows Authentication")
        self.comboBox.setItemText(1, "SQL Server Authentication")
        firstFormLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.comboBox)
        verticalLayoutForm.addLayout(firstFormLayout)

        secondFormLayout = QtWidgets.QFormLayout()
        secondFormLayout.setContentsMargins(20, -1, -1, -1)
        secondFormLayout.setHorizontalSpacing(40)
        secondFormLayout.setVerticalSpacing(5)
        secondFormLayout.setObjectName("secondFormLayout")

        self.userNameLabel = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.userNameLabel.setObjectName("userNameLabel")
        self.userNameLabel.setText("User Name:")
        secondFormLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.userNameLabel)
        self.userNameLineEdit = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.userNameLineEdit.setMaximumSize(QtCore.QSize(270, 16777215))
        self.userNameLineEdit.setObjectName("userNameLineEdit")
        secondFormLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.userNameLineEdit)

        self.passwordLabel = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.passwordLabel.setObjectName("passwordLabel")
        self.passwordLabel.setText("Password:")
        secondFormLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.passwordLabel)
        self.passwordLineEdit = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.passwordLineEdit.setMaximumSize(QtCore.QSize(270, 16777215))
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        secondFormLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.passwordLineEdit)

        self.checkBox = QtWidgets.QCheckBox(parent=self.verticalLayoutWidget)
        self.checkBox.setObjectName("checkBox")
        self.checkBox.setText("Remember password")
        secondFormLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.checkBox)

        verticalLayoutForm.addLayout(secondFormLayout)

        self.line_2 = QtWidgets.QFrame(parent=self.verticalLayoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        verticalLayoutForm.addWidget(self.line_2)

        self.buttonBox = QtWidgets.QDialogButtonBox(parent=self.verticalLayoutWidget)
        self.buttonBox.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.StandardButton.Cancel | QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        verticalLayoutForm.addWidget(self.buttonBox)
        self.verticalLayout.addLayout(verticalLayoutForm)
        QtCore.QMetaObject.connectSlotsByName(self)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = Window(None)
    ui.show()
    sys.exit(app.exec())

