from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget, QHBoxLayout
from PySide6.QtGui import  QIcon

from controllers.navigationController import NavigationController

from app.homeScreen import HomeScreen
from app.loginScreen import LoginScreen

from environment.envVariables import WINDOW_ICON_PATH


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        #------------------------------------------------ window setting ------------------------------------------------
        self.setWindowTitle("InventoPy")
        self.setGeometry(1, 1, 600, 400)
        self.icon = QIcon(str(WINDOW_ICON_PATH))
        self.setWindowIcon(self.icon)                                                                                                                            

        # central widget configuration
        self.centralWidget = QWidget()
        self.mainLayout = QHBoxLayout(self.centralWidget)
        self.setCentralWidget(self.centralWidget)

        # create the navigation controller
        self.navigationController = NavigationController()

        # class methods
        self.createSidebar()
        self.createScreens()
        self.centerGenerationWindow()

    # making the sidebar
    def createSidebar(self):

        # layout to create the sidebar widgets
        self.sidebar = QVBoxLayout()

        #----------------------------------------------- SIDEBAR BUTTONS -----------------------------------------------
        self.toShowMainButton = QPushButton("Main")

        self.toShowLoginButton = QPushButton("Authentication")

        self.toShowClientsButton = QPushButton("Clients")
        self.toClientsRegisterButton = QPushButton("Clients Registration")

        self.toShowColaboratorsButton = QPushButton("Colaborators")
        self.toColaboratorsRegisterButton = QPushButton("Colaborators Registration")

        self.toShowProductsButton = QPushButton("Products")
        self.toAddProductsButton = QPushButton("<PRODUCTS ADD NONE>")

        self.toShowSalesButton = QPushButton("Sales")

        self.toShowSuppliersButton = QPushButton("Suppliers")


        # adding the widgtes 
        self.sidebar.addWidget(self.toShowMainButton)

        self.sidebar.addWidget(self.toShowLoginButton)

        self.sidebar.addWidget(self.toShowClientsButton)
        self.sidebar.addWidget(self.toClientsRegisterButton)
        
        self.sidebar.addWidget(self.toShowColaboratorsButton)
        self.sidebar.addWidget(self.toColaboratorsRegisterButton)
        
        self.sidebar.addWidget(self.toShowProductsButton)
        self.sidebar.addWidget(self.toAddProductsButton)
        
        self.sidebar.addWidget(self.toShowSalesButton)
        
        self.sidebar.addWidget(self.toShowSuppliersButton)

        # adding a layout to main layout
        self.mainLayout.addLayout(self.sidebar)

        # make buttons fucntionally
        self.toShowMainButton.clicked.connect(lambda: self.navigationController.navigateTo("home_screen"))
        self.toShowLoginButton.clicked.connect(lambda: self.navigationController.navigateTo("login_screen"))

    def createScreens(self):
        # create and configure the screens
        self.homeScreen = HomeScreen(self.navigationController)
        self.loginScreen = LoginScreen(self.navigationController)
    


        # add the screens to navigate controller
        self.navigationController.add_widget(self.homeScreen, "home_screen")
        self.navigationController.add_widget(self.loginScreen, "login_screen")

        # add the stacked layout to main layout
        self.mainLayout.addWidget(self.navigationController.get_stack())


    def fixAllSize(self):
        # self.adjustSize()
        self.setFixedSize(self.width(), self.height())


    def centerGenerationWindow(self):
        # Centraliza a janela na tela
        screen = QApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        window_geometry = self.frameGeometry()
        center_point = screen_geometry.center()
        window_geometry.moveCenter(center_point)
        self.move(window_geometry.topLeft())


if __name__ == "__main__":
    app = QApplication()

    window = MainWindow()
    window.show()

    window.fixAllSize()
    app.exec()