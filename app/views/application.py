from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QDialog
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt

from controllers.navigationController import NavigationController
from app.views.homeScreen import HomeScreen
from app.views.clientsScreen import ClientsScreen
from app.views.colaboratorsScreen import ColaboratorsScreen
from app.views.productsScreen import ProductsScreen
from app.views.salesScreen import SalesScreen
from app.views.suppliersScreen import SuppliersScreen

from environment.envVariables import WINDOW_ICON_PATH, APPLICATION_STYLESHEET_PATH

from app.views.authentication import LoginWindow


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget = None, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.setWindowTitle("InventoPy - Gerenciador de estoque")
        self.icon = QIcon(str(WINDOW_ICON_PATH))
        self.setWindowIcon(self.icon)

        self.centralWidget = QWidget()
        self.mainLayout = QHBoxLayout(self.centralWidget)
        self.setCentralWidget(self.centralWidget)

        self.navigationController = NavigationController()

        self.setClassStyle()

        self.createSidebar()
        self.createScreens()

        self.showFullScreen()
        self.setWindowFlags(Qt.Window | Qt.CustomizeWindowHint | Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint | Qt.WindowStaysOnTopHint)
        
        self.setFixedSize(self.size())  # Define um tamanho fixo para a janela

        


    def createSidebar(self):
        self.sidebar = QVBoxLayout()
        self.toShowHomeButton = QPushButton("Home")
        self.toShowClientsButton = QPushButton("Clients")
        self.toShowColaboratorsButton = QPushButton("Colaborators")
        self.toShowProductsButton = QPushButton("Products")
        self.toShowSalesButton = QPushButton("Sales")
        self.toShowSuppliersButton = QPushButton("Suppliers")

        self.sidebar.addWidget(self.toShowHomeButton)
        self.sidebar.addWidget(self.toShowClientsButton)
        self.sidebar.addWidget(self.toShowColaboratorsButton)
        self.sidebar.addWidget(self.toShowProductsButton)
        self.sidebar.addWidget(self.toShowSalesButton)
        self.sidebar.addWidget(self.toShowSuppliersButton)

        self.mainLayout.addLayout(self.sidebar)

        self.toShowHomeButton.clicked.connect(lambda: self.navigationController.navigateTo("home_screen"))
        self.toShowClientsButton.clicked.connect(lambda: self.navigationController.navigateTo("clients_screen"))
        self.toShowColaboratorsButton.clicked.connect(lambda: self.navigationController.navigateTo("colaborators_screen"))
        self.toShowProductsButton.clicked.connect(lambda: self.navigationController.navigateTo("products_screen"))
        self.toShowSalesButton.clicked.connect(lambda: self.navigationController.navigateTo("sales_screen"))
        self.toShowSuppliersButton.clicked.connect(lambda: self.navigationController.navigateTo("suppliers_screen"))


    def createScreens(self):
        self.homeScreen = HomeScreen(self.navigationController)
        self.clientsScreen = ClientsScreen(self.navigationController)
        self.colaboratorsScreen = ColaboratorsScreen(self.navigationController)
        self.productsScreen = ProductsScreen(self.navigationController)
        self.salesScreen = SalesScreen(self.navigationController)
        self.suppliersScreen = SuppliersScreen(self.navigationController)

        self.navigationController.add_widget(self.homeScreen, "home_screen")
        self.navigationController.add_widget(self.clientsScreen, "clients_screen")
        self.navigationController.add_widget(self.colaboratorsScreen, "colaborators_screen")
        self.navigationController.add_widget(self.productsScreen, "products_screen")
        self.navigationController.add_widget(self.salesScreen, "sales_screen")
        self.navigationController.add_widget(self.suppliersScreen, "suppliers_screen")

        self.mainLayout.addWidget(self.navigationController.get_stack())


    def fixAllSize(self):
        self.setFixedSize(self.width(), self.height())


    def centerGenerationWindow(self):
        screen = QApplication.primaryScreen()
        screenGeometry = screen.availableGeometry()
        windowGeometry = self.frameGeometry()
        centerPoint = screenGeometry.center()
        windowGeometry.moveCenter(centerPoint)
        self.move(windowGeometry.topLeft())


    def setClassStyle(self):
        # Carrega e aplica o arquivo QSS para estilização
        with open(str(APPLICATION_STYLESHEET_PATH), "r") as file:
            self.setStyleSheet(file.read())


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    login_window = LoginWindow()
    login_window.setWindowModality(Qt.ApplicationModal)  # Torna a janela modal para garantir que o foco permaneça nela
    if login_window.exec() == QDialog.Accepted:
        main_window = MainWindow()
        main_window.show()

        sys.exit(app.exec())  # Encerra a execução do código quando a janela principal for fechada
    else:
        QApplication.instance().quit()  # Fecha o aplicativo corretamente se o login não for autenticado