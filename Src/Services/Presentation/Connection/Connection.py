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
        self.show()

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
        line = QtWidgets.QFrame(parent=self.verticalLayoutWidget)
        line.setMinimumSize(QtCore.QSize(0, 2))
        line.setMaximumSize(QtCore.QSize(16777215, 1))
        line.setStyleSheet("background-color: rgb(254, 135, 24);")
        line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        line.setObjectName("line")
        self.verticalLayout.addWidget(line)

    def _createHeader(self):
        header = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        header.setMaximumSize(QtCore.QSize(480, 65))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(25)
        header.setFont(font)
        header.setStyleSheet("color: rgb(56, 56, 56);\n"
                                  "background-color: rgb(240, 240, 240);")
        header.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        header.setObjectName("header")
        header.setText("SQL Server")
        self.verticalLayout.addWidget(header)

    def _createForm(self):
        verticalLayoutForm = QtWidgets.QVBoxLayout()
        verticalLayoutForm.setContentsMargins(10, 10, 10, 10)
        verticalLayoutForm.setSpacing(0)
        verticalLayoutForm.setObjectName("verticalLayoutForm")

        firstFormLayout = QtWidgets.QFormLayout()
        firstFormLayout.setContentsMargins(0, 0, 0, 0)
        firstFormLayout.setHorizontalSpacing(90)
        firstFormLayout.setVerticalSpacing(5)
        firstFormLayout.setObjectName("firstFormLayout")

        serverNameLabel = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        serverNameLabel.setObjectName("serverNameLabel")
        serverNameLabel.setText("Server name:")
        firstFormLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, serverNameLabel)

        self.serverName = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.serverName.setMaximumSize(QtCore.QSize(300, 16777215))
        self.serverName.setObjectName("serverName")
        self.serverName.setStyleSheet("border: 1px solid #d0d0d0;")
        firstFormLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.serverName)

        self.authenticationLabel = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.authenticationLabel.setObjectName("authenticationLabel")
        self.authenticationLabel.setText("Authentication:")
        firstFormLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.authenticationLabel)
        self.authentication = QtWidgets.QComboBox(parent=self.verticalLayoutWidget)
        self.authentication.setMinimumSize(QtCore.QSize(290, 0))
        self.authentication.setMaximumSize(QtCore.QSize(290, 16777215))
        self.authentication.setObjectName("authentication")
        self.authentication.addItem("Windows Authentication")
        self.authentication.addItem("SQL Server Authentication")
        firstFormLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.authentication)
        verticalLayoutForm.addLayout(firstFormLayout)

        secondFormLayout = QtWidgets.QFormLayout()
        secondFormLayout.setContentsMargins(20, -1, -1, -1)
        secondFormLayout.setHorizontalSpacing(120)
        secondFormLayout.setVerticalSpacing(5)
        secondFormLayout.setObjectName("secondFormLayout")

        self.userNameLabel = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.userNameLabel.setObjectName("userNameLabel")
        self.userNameLabel.setText("User Name:")
        secondFormLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.userNameLabel)
        self.userName = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.userName.setMaximumSize(QtCore.QSize(270, 16777215))
        self.userName.setObjectName("userName")
        self.userName.setText("localhost")
        self.userName.setStyleSheet("border: 1px solid #d0d0d0;")
        secondFormLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.userName)

        self.passwordLabel = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.passwordLabel.setObjectName("passwordLabel")
        self.passwordLabel.setText("Password:")
        secondFormLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.passwordLabel)
        self.password = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.password.setMaximumSize(QtCore.QSize(270, 16777215))
        self.password.setObjectName("password")
        self.password.setStyleSheet("border: 1px solid #d0d0d0;")
        secondFormLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.password)

        verticalLayoutForm.addLayout(secondFormLayout)

        separator = QtWidgets.QFrame(parent=self.verticalLayoutWidget)
        separator.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        separator.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        separator.setObjectName("separator")
        verticalLayoutForm.addWidget(separator)

        self.buttonBox = QtWidgets.QDialogButtonBox(parent=self.verticalLayoutWidget)
        self.buttonBox.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.addButton(QtWidgets.QDialogButtonBox.StandardButton.Cancel).setText("Cancel")
        self.buttonBox.addButton(QtWidgets.QDialogButtonBox.StandardButton.Ok).setText("Connect")
        self.buttonBox.button(QtWidgets.QDialogButtonBox.StandardButton.Cancel).clicked.connect(self._cancel)
        self.buttonBox.button(QtWidgets.QDialogButtonBox.StandardButton.Ok).clicked.connect(self._connect)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        verticalLayoutForm.addWidget(self.buttonBox)

        self._disabledFormAuthenticationType()
        self.verticalLayout.addLayout(verticalLayoutForm)
        QtCore.QMetaObject.connectSlotsByName(self)

    def _enabledFormAuthenticationType(self):
        self.passwordLabel.setDisabled(False)
        self.userNameLabel.setDisabled(False)
        self.userName.setDisabled(False)
        self.password.setDisabled(False)

    def _disabledFormAuthenticationType(self):
        self.passwordLabel.setDisabled(True)
        self.userNameLabel.setDisabled(True)
        self.userName.setDisabled(True)
        self.password.setDisabled(True)

    def _cancel(self):
        self.destroy()
        self.close()

    def _connect(self):
        self.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = Window(None)
    sys.exit(app.exec())

