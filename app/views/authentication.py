from PySide6.QtWidgets import QDialog, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QApplication, QWidget, QVBoxLayout, QSpacerItem, QSizePolicy
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
        mainLayout = QHBoxLayout()  # Usar QHBoxLayout como layout principal
        self.setLayout(mainLayout)

        # Layout secundário 1 para a imagem
        imageWidget = QWidget()
        imageWidget.setFixedSize(500, 500)  # Definir tamanho fixo para o widget
        imageLoginLabel = QLabel(imageWidget)
        imageLoginLabel.setPixmap(QPixmap(LOGIN_IMAGE_PATH))
        imageLoginLabel.setGeometry(0, 0, 500, 500)  # Definir a posição e tamanho do QLabel dentro do widget
        mainLayout.addWidget(imageWidget)

        # Layout secundário 2 para os demais widgets
        loginWidget = QWidget()
        loginWidget.setFixedSize(450, 500)  # Definir largura fixa para o widget
        loginLayout = QVBoxLayout(loginWidget)
        loginLayout.setContentsMargins(0, 0, 0, 0)  # Remover espaçamento interno
        loginLayout.addSpacing(10)
        # loginLayout.setAlignment(Qt.AlignVCenter)

        loginLayout.addSpacerItem(QSpacerItem(0, 75, QSizePolicy.Minimum, QSizePolicy.Fixed))  # Adicionar um espaço de 100 pixels
        titleLabel = QLabel("Faça seu Login", alignment=Qt.AlignLeft)
        titleLabel.setObjectName("titleLabel")
        # loginLayout.addSpacing(100)

        # titleLabel.setGeometry(50, 50, 500, 300)
        loginLayout.addWidget(titleLabel)

        loginLayout.addSpacerItem(QSpacerItem(0, 50, QSizePolicy.Minimum, QSizePolicy.Fixed))  # Adicionar um espaço de 50 pixels
        self.usernameLabel = QLabel("Usuário")
        loginLayout.addWidget(self.usernameLabel)

        self.usernameLine = QLineEdit()
        loginLayout.addWidget(self.usernameLine)

        self.passwordLabel = QLabel("Senha")
        loginLayout.addWidget(self.passwordLabel)

        self.passwordLine = QLineEdit()
        loginLayout.addWidget(self.passwordLine)

        loginLayout.addSpacerItem(QSpacerItem(0, 20, QSizePolicy.Minimum, QSizePolicy.Fixed))  # Adicionar um espaço de 20 pixels

        self.submitButton = QPushButton("Entrar")
        self.submitButton.setMinimumWidth(150)
        self.submitButton.clicked.connect(self.handleLogin)

        loginLayout.addWidget(self.submitButton, alignment=Qt.AlignHCenter)
        loginLayout.addSpacerItem(QSpacerItem(0, 100, QSizePolicy.Minimum, QSizePolicy.Expanding))  # Adicionar um espaço de 100 pixels

        mainLayout.addWidget(loginWidget)

        # Adicionar espaçamento horizontal
        loginLayout.setContentsMargins(50, 0, 50, 0)

    def handleLogin(self):
        username = self.usernameLine.text()
        password = self.passwordLine.text()

        if database.authUser(username, password):
            # QMessageBox.information(self, "Login Successful", "Welcome!")
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