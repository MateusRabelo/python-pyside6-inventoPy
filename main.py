from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget, QHBoxLayout
from PySide6.QtGui import  QIcon

from controllers.navigationController import NavigationController

from app.homeScreen import HomeScreen
from app.loginScreen import LoginScreen

from environmentVariables import WINDOW_ICON_PATH


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

    # making the sidebar
    def createSidebar(self):

        # layout to create the sidebar widgets
        self.sidebar = QVBoxLayout()

        # creating all necessary widgets
        self.button_main = QPushButton("Main Window")
        self.button_login = QPushButton("Login Screen")

        # adding the widgtes 
        self.sidebar.addWidget(self.button_main)
        self.sidebar.addWidget(self.button_login)

        # adding a layout to main layout
        self.mainLayout.addLayout(self.sidebar)

        # make buttons fucntionally
        self.button_main.clicked.connect(lambda: self.navigationController.navigateTo("main_screen"))
        self.button_login.clicked.connect(lambda: self.navigationController.navigateTo("login_screen"))

    def createScreens(self):
        # Cria e configura as telas
        self.main_screen = HomeScreen(self.navigationController)
        self.login_screen = LoginScreen(self.navigationController)

        # Adiciona as telas ao controlador de navegação
        self.navigationController.add_widget(self.main_screen, "main_screen")
        self.navigationController.add_widget(self.login_screen, "login_screen")

        # Adiciona o QStackedWidget ao layout principal
        self.mainLayout.addWidget(self.navigationController.get_stack())

    def fixAllSize(self):
        # self.adjustSize()
        self.setFixedSize(self.width(), self.height())


if __name__ == "__main__":
    app = QApplication()

    window = MainWindow()
    window.show()

    window.fixAllSize()
    app.exec()