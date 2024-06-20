from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class AddProductsScreen(QWidget):
    def __inti__(self, navigationController):
        super().__init__()

        self.navigationController = navigationController
        self.setupUserInterface()
        self.setClassStyle()

        def setupUserInterface(self):
            ...

        def setClassStyle():
            pass