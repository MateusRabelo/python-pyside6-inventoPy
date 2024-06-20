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

        label = QLabel("This will be the home screen", alignment=Qt.AlignCenter)

        button = QPushButton("Go to Login")
        button.clicked.connect(self.go_to_login)

        layout.addWidget(label)
        layout.addWidget(button)

        self.setLayout(layout)

    def go_to_login(self):
        self.navigationController.navigateTo("login_screen")
