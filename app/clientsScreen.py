from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget
from PySide6.QtCore import Qt

from db import database


class ClientsScreen(QWidget):
    def __init__(self, navigationController):
        super().__init__()

        self.navigationController = navigationController
        self.setupUserInterface()
        self.setClassStyle()

    def setupUserInterface(self):
        mainLayout = QVBoxLayout()
        self.setLayout(mainLayout)

        titleLabel = QLabel("Registered Clients", alignment=Qt.AlignCenter)

        self.clientsList = QListWidget()

        mainLayout.addWidget(titleLabel)
        mainLayout.addWidget(self.clientsList)

        self.loadClients()

    def loadClients(self):
        users = database.getUsers()
        self.clientsList.clear()
        for user in users:
            self.clientsList.addItem(f"ID: {user[0]},\nUSERNAME: {user[1]}\n")


    def setClassStyle(self):
        ...