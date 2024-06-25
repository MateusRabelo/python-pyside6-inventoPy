from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QApplication
from PySide6.QtCore import Qt
from environment.envVariables import LOGIN_STYLESHEET_PATH
from db import database

class LoginWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Login")
        self.setGeometry(100, 100, 300, 150)  # Define a geometria da janela (largura, altura)
        self.centerDialog()  # Centraliza a janela na tela
        self.setupUserInterface()
        self.setClassStyle()

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
            self.accept()  # Aceita o diálogo
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid username or password.")

    def setClassStyle(self):
        with open(str(LOGIN_STYLESHEET_PATH), "r") as file:
            self.setStyleSheet(file.read())

    def centerDialog(self):
        screen = QApplication.primaryScreen()
        screenGeometry = screen.availableGeometry()
        dialogGeometry = self.frameGeometry()
        centerPoint = screenGeometry.center()
        dialogGeometry.moveCenter(centerPoint)
        self.move(dialogGeometry.topLeft())
