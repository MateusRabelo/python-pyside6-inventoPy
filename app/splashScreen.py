from PySide6.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QLabel, QVBoxLayout, QPushButton
from PySide6.QtCore import Qt

from app.homeScreen import HomeScreen

class SplashScreen(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.setWindowTitle("Presentation Screen")
        self.setGeometry(100, 100, 800, 600)
        # self.windowIcon
        # self.setWindowIcon

        self.centralWidget = QWidget()
        self.vLayout = QVBoxLayout()
        self.centralWidget.setLayout(self.vLayout)

        self.label1 = QLabel("This is a future splash screen", alignment=Qt.AlignCenter)
        self.vLayout.addWidget(self.label1)

        self.button1 = QPushButton("go to main window")
        self.button1.clicked.connect(self.go_to_login)
        self.vLayout.addWidget(self.button1)

        self.setCentralWidget(self.centralWidget)

            


    def go_to_login(self):

        self.mainWindow = HomeScreen()  # Cria uma instância da nova tela
        self.mainWindow.show()  # Mostra a nova tela
        self.close()
