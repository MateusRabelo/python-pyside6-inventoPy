from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PySide6.QtCore import Qt

from environment.envVariables import LOGIN_STYLESHEET_PATH

from db import database

class LoginScreen(QWidget):
    def __init__(self, navigationController):
        super().__init__()
        self.navigationController = navigationController

        self.setupUserInterface()
        self.setClassStyle()

    # to create the Login Screen
    def setupUserInterface(self):
        mainLayout = QVBoxLayout()
        self.setLayout(mainLayout)

        titleLabel = QLabel("This will be the login screen", alignment=Qt.AlignCenter)

        self.usernameLabel = QLabel("Usuário")
        self.usernameLine = QLineEdit()

        self.passwordLabel = QLabel("Senha")
        self.passwordLine = QLineEdit()
        self.passwordLine.setEchoMode(QLineEdit.Password)

        self.submitButton = QPushButton("Entrar")
        self.submitButton.clicked.connect(self.handleLogin)

        mainLayout.addWidget(titleLabel)
        mainLayout.addWidget(self.usernameLabel)
        mainLayout.addWidget(self.usernameLine)
        mainLayout.addWidget(self.passwordLabel)
        mainLayout.addWidget(self.passwordLine)
        mainLayout.addWidget(self.submitButton)



    def handleLogin(self):
        username = self.usernameLine.text()
        password = self.passwordLine.text()

        if database.authUser(username, password):
            QMessageBox.information(self, "Login Successful", "Welcome!")
            self.navigationController.navigateTo("clients_screen")
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid username or password.")



    def setClassStyle(self):
        # Carrega e aplica o arquivo QSS para estilização
        with open(str(LOGIN_STYLESHEET_PATH), "r") as file:
            self.setStyleSheet(file.read())
