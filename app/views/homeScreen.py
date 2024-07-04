from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QSpacerItem, QSizePolicy
from PySide6.QtGui import QPixmap, QPalette, QColor, QBrush
from PySide6.QtCore import Qt

from environment.envVariables import HOME_STYLESHEET_PATH

class HomeScreen(QWidget):
    def __init__(self, navigationController):
        super().__init__()

        # configure the navigation controller beacuse the on clicked button function
        self.navigationController = navigationController
        self.setupUserInterface()
        self.setClassStyle()

    def setupUserInterface(self):
        mainLayout = QHBoxLayout()


        # welcome section
        welcomeLayout = QVBoxLayout()

        welcomeSpacerTop = QSpacerItem(5, 5, QSizePolicy.Minimum, QSizePolicy.Expanding)
        welcomeLabel = QLabel("Bem vindo ao InvetoPy\nA melhor forma de gerenciar seu estoque!", alignment=Qt.AlignCenter)
        welcomeLabel.setObjectName("welcomeLabel")
        welcomeSpacerBottom = QSpacerItem(20,100, QSizePolicy.Minimum, QSizePolicy.Expanding)

        topSalesLabel = QLabel("Campeões em vendas", alignment=Qt.AlignCenter)
        topSalesLabel.setObjectName("topSalesLabel")

        top1SalesLabel = QLabel("Sofá", alignment=Qt.AlignCenter)
        top1SalesLabel.setObjectName("top1SalesLabel")

        top2SalesLabel = QLabel("Cama", alignment=Qt.AlignCenter)
        top2SalesLabel.setObjectName("top2SalesLabel")

        top3SalesLabel = QLabel("Pepsi", alignment=Qt.AlignCenter)
        top3SalesLabel.setObjectName("top3SalesLabel")



        lastSalesLabel = QLabel("Últimas vendas", alignment=Qt.AlignCenter)
        lastSalesLabel.setObjectName("lastSalesLabel")

        sale1Label = QLabel("sale 1", alignment=Qt.AlignCenter)
        sale1Label.setObjectName("sale1Label")

        sale2Label = QLabel("sale 2", alignment=Qt.AlignCenter)
        sale2Label.setObjectName("sale2Label")

        sale3Label = QLabel("sale 3", alignment=Qt.AlignCenter)
        sale3Label.setObjectName("sale3Label")



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
        newsContainer = QWidget()
        newsContainer.setObjectName("newsContainer")

        # Create a QPalette object
        palette = QPalette()

        # Set the background color using the setBrush function
        palette.setBrush(QPalette.Window, QBrush(QColor("#FF0000")))  # Replace #FF0000 with your desired color

        # Apply the palette to the newsContainer
        newsContainer.setPalette(palette)

        newsLayout = QVBoxLayout()
        newsLayout.setObjectName("newsLayout")

        newsTitleLabel = QLabel("Últimas notícias", alignment=Qt.AlignCenter)
        newsTitleLabel.setObjectName("newsTitleLabel")

        news1Label = QLabel("Não recebeu seu passe? Entre em contato com o RH\nvia e-mail ou faça um chamado.")
        news1Label.setObjectName("news1Label")

        news2Label = QLabel("Use à vontade nossos ambientes de descontração!")
        news2Label.setObjectName("news2Label")

        news3Label = QLabel("Tem alguma sugestão do que podemos melhorar?\nSe sim, deixe sua sugestão com o RH.")
        news3Label.setObjectName("news3Label")

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

        

    def setClassStyle(self):
        # Carrega e aplica o arquivo QSS para estilização
        with open(str(HOME_STYLESHEET_PATH), "r") as file:
            self.setStyleSheet(file.read())
