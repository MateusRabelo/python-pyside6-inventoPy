from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PySide6.QtCore import Qt


class ProductsRegisterScreen(QWidget):
    def __init__(self, navigationController):
        super().__init__()

        self.navigationController = navigationController
        self.setupUserInterface()
        self.setClassStyle()

    # to create the content
    def setupUserInterface(self):
        # define layout
        mainLayout = QVBoxLayout()
        self.setLayout(mainLayout)

        # adding widgets
        titleLabel = QLabel("This will be the Products Register screen", alignment=Qt.AlignCenter)

        # applying widgets
        mainLayout.addWidget(titleLabel)

    # to set the qss
    def setClassStyle(self):
        ...