from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PySide6.QtCore import Qt


class ColaboratorsScreen(QWidget):
    def __init__(self, navigationController):
        super().__init__()

        self.navigationController = navigationController
        self.setupUserInterface()
        self.setClassStyle()

    def setupUserInterface(self):
        # define layout
        mainLayout = QVBoxLayout()
        self.setLayout(mainLayout)

        # adding widgets
        titleLabel = QLabel("This will be the Colaborators screen", alignment=Qt.AlignCenter)

        # applying widgets
        mainLayout.addWidget(titleLabel)

    def setClassStyle(self):
        ...