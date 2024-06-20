from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PySide6.QtCore import Qt

class LoginScreen(QWidget):
    def __init__(self, navigationController):
        super().__init__()
        self.navigationController = navigationController
        self.setupUserInterface()

    # to create the Login Screen
    def setupUserInterface(self):
        mainLayout = QVBoxLayout()
        self.setLayout(mainLayout)


        titleLabel =  QLabel("This will be the login screen", alignment=Qt.AlignCenter)

        userLabel = QLabel("Usuário: ")
        userLine = QLineEdit()

        passwordLabel = QLabel("Senha: ")
        passwordLine = QLineEdit()

        submitButton = QPushButton("Entrar")



        mainLayout.addWidget(titleLabel)

        mainLayout.addWidget(userLabel)
        mainLayout.addWidget(userLine)

        mainLayout.addWidget(passwordLabel)
        mainLayout.addWidget(passwordLine)

        mainLayout.addWidget(submitButton)
