from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt

class LoginScreen(QWidget):
    def __init__(self, navigationController):
        super().__init__()
        self.navigationController = navigationController
        self.setupUserInterface()

    # def to create the Login Screen
    def setupUserInterface(self):
        mainLayout = QVBoxLayout()
        self.setLayout(mainLayout)


        titleLabel =  QLabel("This will be the login screen", alignment=Qt.AlignCenter)
        mainLayout.addWidget(titleLabel)
