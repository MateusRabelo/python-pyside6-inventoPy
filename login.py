# loginWindow.py
from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QWidget
from PySide6.QtCore import Qt
from environment.envVariables import LOGIN_STYLESHEET_PATH
from db import database

class LoginWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.setGeometry(1, 1, 300, 200)

        self.mainLayout = QVBoxLayout(self)
        self.setupUserInterface()
        self.setClassStyle()

    def setupUserInterface(self):
        titleLabel = QLabel("This will be the login screen", alignment=Qt.AlignCenter)

        self.usernameLabel = QLabel("Usuário")
        self.usernameLine = QLineEdit()

        self.passwordLabel = QLabel("Senha")
        self.passwordLine = QLineEdit()
        self.passwordLine.setEchoMode(QLineEdit.Password)

        self.submitButton = QPushButton("Entrar")
        self.submitButton.clicked.connect(self.handleLogin)

        self.mainLayout.addWidget(titleLabel)
        self.mainLayout.addWidget(self.usernameLabel)
        self.mainLayout.addWidget(self.usernameLine)
        self.mainLayout.addWidget(self.passwordLabel)
        self.mainLayout.addWidget(self.passwordLine)
        self.mainLayout.addWidget(self.submitButton)

    def handleLogin(self):
        username = self.usernameLine.text()
        password = self.passwordLine.text()

        if database.authUser(username, password):
            QMessageBox.information(self, "Login Successful", "Welcome!")
            self.accept()
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid username or password.")

    def setClassStyle(self):
        with open(str(LOGIN_STYLESHEET_PATH), "r") as file:
            self.setStyleSheet(file.read())
