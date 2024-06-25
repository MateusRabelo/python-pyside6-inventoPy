from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget, QHBoxLayout
from PySide6.QtGui import  QIcon

from controllers.navigationController import NavigationController

from app.homeScreen import HomeScreen
from app.loginScreen import LoginScreen
from app.clientsScreen import ClientsScreen
from app.clientsRegisterScreen import ClientRegisterScreen
from app.colaboratorsRegisterScreen import ColaboratorsRegisterScreen
from app.colaboratorsScreen import ColaboratorsScreen
from app.productsScreen import ProductsScreen
from app.salesScreen import SalesScreen
from app.suppliersScreen import SuppliersScreen
from app.productsRegisterScreen import ProductsRegisterScreen

from environment.envVariables import WINDOW_ICON_PATH

from db import database


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        # ------------------------------------------------ SINDOW SETTING ------------------------------------------------
        self.setWindowTitle("InventoPy") # set title
        self.setGeometry(1, 1, 600, 400) #set window geometry

        self.icon = QIcon(str(WINDOW_ICON_PATH)) #set icon
        self.setWindowIcon(self.icon) #apply icon                                                                                                                         

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

        # ----------------------------------------------- SIDEBAR BUTTONS -----------------------------------------------
        
        self.toShowHomeButton = QPushButton("Home") # define home button

        self.toShowLoginButton = QPushButton("Authentication") # define login button

        self.toShowClientsButton = QPushButton("Clients") # define clients button
        self.toClientsRegisterButton = QPushButton("Clients Registration") # define clients registration button

        self.toShowColaboratorsButton = QPushButton("Colaborators") # define colaborators button
        self.toColaboratorsRegisterButton = QPushButton("Colaborators Registration") # define colaborators registration button

        self.toShowProductsButton = QPushButton("Products") # define products button
        self.toAddProductsButton = QPushButton("<PRODUCTS ADD NONE>") 

        self.toShowSalesButton = QPushButton("Sales") # define sales button

        self.toShowSuppliersButton = QPushButton("Suppliers") # define suppliers button


        # adding the widgtes  
        self.sidebar.addWidget(self.toShowHomeButton) 

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
        self.toShowHomeButton.clicked.connect(lambda: self.navigationController.navigateTo("home_screen"))

        self.toShowLoginButton.clicked.connect(lambda: self.navigationController.navigateTo("login_screen"))

        self.toShowClientsButton.clicked.connect(lambda: self.navigationController.navigateTo("clients_screen"))
        self.toClientsRegisterButton.clicked.connect(lambda: self.navigationController.navigateTo("clients_register_screen"))

        self.toShowColaboratorsButton.clicked.connect(lambda: self.navigationController.navigateTo("colaborators_screen"))
        self.toColaboratorsRegisterButton.clicked.connect(lambda: self.navigationController.navigateTo("colaborators_register_screen"))

        self.toShowProductsButton.clicked.connect(lambda: self.navigationController.navigateTo("products_screen"))
        self.toAddProductsButton.clicked.connect(lambda: self.navigationController.navigateTo("products_register_screen"))

        self.toShowSalesButton.clicked.connect(lambda: self.navigationController.navigateTo("sales_screen"))

        self.toShowSuppliersButton.clicked.connect(lambda: self.navigationController.navigateTo("suppliers_screen"))



    def createScreens(self):
        # create and configure the screens
        self.homeScreen = HomeScreen(self.navigationController)

        self.loginScreen = LoginScreen(self.navigationController)

        self.clientsScreen = ClientsScreen(self.navigationController)
        self.clientsRegisterScreen = ClientRegisterScreen(self.navigationController)

        self.colaboratorsScreen = ColaboratorsScreen(self.navigationController)
        self.colaboratorsRegisterScreen = ColaboratorsRegisterScreen(self.navigationController)

        self.productsScreen = ProductsScreen(self.navigationController)
        self.productsRegisterScreen = ProductsRegisterScreen(self.navigationController)

        self.salesScreen = SalesScreen(self.navigationController)

        self.suppliersScreen = SuppliersScreen(self.navigationController)


        # add the screens to navigate controller
        self.navigationController.add_widget(self.homeScreen, "home_screen")

        self.navigationController.add_widget(self.loginScreen, "login_screen")

        self.navigationController.add_widget(self.clientsScreen, "clients_screen")
        self.navigationController.add_widget(self.clientsRegisterScreen, "clients_register_screen")

        self.navigationController.add_widget(self.colaboratorsScreen, "colaborators_screen")
        self.navigationController.add_widget(self.colaboratorsRegisterScreen, "colaborators_register_screen")

        self.navigationController.add_widget(self.productsScreen, "products_screen")
        self.navigationController.add_widget(self.productsRegisterScreen, "products_register_screen")

        self.navigationController.add_widget(self.salesScreen, "sales_screen")

        self.navigationController.add_widget(self.suppliersScreen, "suppliers_screen")

        # add the stacked layout to main layout
        self.mainLayout.addWidget(self.navigationController.get_stack())




    def fixAllSize(self):
        # self.adjustSize()
        self.setFixedSize(self.width(), self.height())



    # to center the screen on the generation
    def centerGenerationWindow(self):

        screen = QApplication.primaryScreen() # define main screen

        screenGeometry = screen.availableGeometry() # define available geometry in the screen
        windowGeometry = self.frameGeometry() # define window geometry
        
        centrePoint = screenGeometry.center() # define the central point in the screen

        windowGeometry.moveCenter(centrePoint) # move the center of the geoemtry to center of the screen

        self.move(windowGeometry.topLeft()) # move the top left of the window (pixel 0, 0), to the center of the geometry in the screen 



if __name__ == "__main__":
    app = QApplication()

    window = MainWindow()
    window.show()

    window.fixAllSize()
    app.exec()