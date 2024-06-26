from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QApplication, QSpacerItem, QHBoxLayout
from PySide6.QtCore import Qt, QPoint
from PySide6.QtGui import QPixmap, QIcon

from environment.envVariables import LOGIN_STYLESHEET_PATH, LOGIN_IMAGE_PATH, WINDOW_ICON_PATH

from db import database

class LoginWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("InventoPy - Authentication")
        self.icon = QIcon(str(WINDOW_ICON_PATH))
        self.setWindowIcon(self.icon)

        self.setupUserInterface()
        self.setClassStyle()
        self.centerDialog()  # Centraliza a janela na tela

    def setupUserInterface(self):
        mainLayout = QHBoxLayout()
        self.setLayout(mainLayout)

        imageLoginLayout = QVBoxLayout()

        imageLoginLabel = QLabel()
        imageLoginLabel.setPixmap(QPixmap(LOGIN_IMAGE_PATH))
        spacerImageBottom = QSpacerItem(550,0)

        loginLayout = QVBoxLayout()
        titleLabel = QLabel("Efetue o Login para continuar", alignment=Qt.AlignCenter)
        spacerTitleBottom = QSpacerItem(400,20) 
        self.usernameLabel = QLabel("Usuário")
        self.usernameLine = QLineEdit()
        self.passwordLabel = QLabel("Senha")
        self.passwordLine = QLineEdit()
        self.passwordLine.setEchoMode(QLineEdit.Password)
        self.submitButton = QPushButton("Entrar")
        self.submitButton.clicked.connect(self.handleLogin)

        imageLoginLayout.addWidget(imageLoginLabel)
        imageLoginLayout.addItem(spacerImageBottom)

        loginLayout.addWidget(titleLabel)
        loginLayout.addItem(spacerTitleBottom)
        loginLayout.addWidget(self.usernameLabel)
        loginLayout.addWidget(self.usernameLine)
        loginLayout.addWidget(self.passwordLabel)
        loginLayout.addWidget(self.passwordLine)
        loginLayout.addWidget(self.submitButton)

        mainLayout.addLayout(imageLoginLayout)
        mainLayout.addLayout(loginLayout)

    def handleLogin(self):
        username = self.usernameLine.text()
        password = self.passwordLine.text()

        if database.authUser(username, password):
            QMessageBox.information(self, "Login Successful", "Welcome!")
            self.accept()  # Aceita o diálogo
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid username or password.")

    def setClassStyle(self):
        with open(str(LOGIN_STYLESHEET_PATH), "r") as file:
            self.setStyleSheet(file.read())

    def centerDialog(self):
        screen = QApplication.primaryScreen()
        screenGeometry = screen.availableGeometry()
        windowGeometry = self.frameGeometry()
        centerPoint = screenGeometry.center()
        windowGeometry.moveCenter(centerPoint)
        offset = screenGeometry.topLeft() - windowGeometry.topLeft()
        self.move(windowGeometry.topLeft() - QPoint(150, 0))