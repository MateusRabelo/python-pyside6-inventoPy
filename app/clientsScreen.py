from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget, QTableWidget, QTableWidgetItem
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

        # Configuração do QTableWidget
        self.clientsTable = QTableWidget()
        self.clientsTable.setColumnCount(2)  # Definindo o número de colunas
        self.clientsTable.setHorizontalHeaderLabels(["ID", "Username"])

        mainLayout.addWidget(titleLabel)
        mainLayout.addWidget(self.clientsTable)

        self.loadClients()

    def loadClients(self):
        users = database.getUsers()  # Obtém os usuários do banco de dados
        self.clientsTable.setRowCount(len(users))  # Definindo o número de linhas

        for row, user in enumerate(users):
            self.clientsTable.setItem(row, 0, QTableWidgetItem(str(user[0])))
            self.clientsTable.setItem(row, 1, QTableWidgetItem(user[1]))


    def setClassStyle(self):
        ...