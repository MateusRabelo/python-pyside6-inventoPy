from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QSpacerItem, QSizePolicy
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

class HomeScreen(QWidget):
    def __init__(self, navigationController):
        super().__init__()

        # configure the navigation controller beacuse the on clicked button function
        self.navigationController = navigationController
        self.setupUserInterface()

    def setupUserInterface(self):
        mainLayout = QHBoxLayout()


        # welcome section
        welcomeLayout = QVBoxLayout()

        welcomeSpacerTop = QSpacerItem(5, 5, QSizePolicy.Minimum, QSizePolicy.Expanding)
        welcomeLabel = QLabel("Bem vindo ao InvetoPy\nA melhor forma de gerenciar seu estoque!", alignment=Qt.AlignCenter)
        welcomeSpacerBottom = QSpacerItem(20,100, QSizePolicy.Minimum, QSizePolicy.Expanding)

        topSalesLabel = QLabel("Campeões em vendas", alignment=Qt.AlignCenter)
        top1SalesLabel = QLabel("Sofá", alignment=Qt.AlignCenter)
        top2SalesLabel = QLabel("Cama", alignment=Qt.AlignCenter)
        top3SalesLabel = QLabel("Pepsi", alignment=Qt.AlignCenter)

        lastSalesLabel = QLabel("Últimas vendas", alignment=Qt.AlignCenter)
        sale1Label = QLabel("sale 1", alignment=Qt.AlignCenter)
        sale2Label = QLabel("sale 2", alignment=Qt.AlignCenter)
        sale3Label = QLabel("sale 3", alignment=Qt.AlignCenter)


        # adds in layout
        welcomeLayout.addItem(welcomeSpacerTop)
        welcomeLayout.addWidget(welcomeLabel)
        welcomeLayout.addItem(welcomeSpacerBottom)

        welcomeLayout.addWidget(topSalesLabel)
        welcomeLayout.addWidget(top1SalesLabel)
        welcomeLayout.addWidget(top2SalesLabel)
        welcomeLayout.addWidget(top3SalesLabel)

        welcomeLayout.addWidget(lastSalesLabel)
        welcomeLayout.addWidget(sale1Label)
        welcomeLayout.addWidget(sale2Label)
        welcomeLayout.addWidget(sale3Label)



        # news section
        newsLayout = QVBoxLayout()

        newsTitleLabel = QLabel("Últimas notícias", alignment=Qt.AlignCenter)
        news1Label = QLabel("Não recebeu seu passe? Entre em contato com o RH\nvia e-mail ou faça um chamado.")
        news2Label = QLabel("Use à vontade nossos ambientes de descontração!")
        news3Label = QLabel("Tem alguma sugestão do que podemos melhorar?\nSe sim, deixe sua sugestão com o RH.")


        newsLayout.addWidget(newsTitleLabel)
        newsLayout.addWidget(news1Label)
        newsLayout.addWidget(news2Label)
        newsLayout.addWidget(news3Label)

        

        # button = QPushButton("Fazer Login")
        # button.clicked.connect(self.toLoginPage)

        # mainLayout.addWidget(mainLabel)
        # layout.addWidget(button)
        mainLayout.addLayout(welcomeLayout)
        mainLayout.addLayout(newsLayout)

        self.setLayout(mainLayout)

    def toLoginPage(self):
        self.navigationController.navigateTo("login_screen")
