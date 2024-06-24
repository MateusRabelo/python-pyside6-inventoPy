from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PySide6.QtCore import Qt

class HomeScreen(QWidget):
    def __init__(self, navigationController):
        super().__init__()

        # configure the navigation controller beacuse the on clicked button function
        self.navigationController = navigationController
        self.setupUserInterface()

    def setupUserInterface(self):
        layout = QVBoxLayout()

        mainLabel = QLabel("InvetoPy - a melhor forma de gerenciar seu estoque!", alignment=Qt.AlignCenter)

        newsTitleLabel = QLabel("Últimas notícias")

        button = QPushButton("Fazer Login")
        button.clicked.connect(self.toLoginPage)

        layout.addWidget(mainLabel)
        layout.addWidget(button)

        self.setLayout(layout)

    def toLoginPage(self):
        self.navigationController.navigateTo("login_screen")
