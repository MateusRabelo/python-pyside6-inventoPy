from PySide6 import QtWidgets, QtCore

class SplashScreen(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Presentation Screen")
        self.setGeometry(100, 100, 800, 600)
        
        # Layout and widgets
        layout = QtWidgets.QVBoxLayout()
        self.label = QtWidgets.QLabel("Welcome to the App!", alignment=QtCore.Qt.AlignCenter)
        self.button = QtWidgets.QPushButton("Go to Login")
        
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)
        
        # Button click event
        self.button.clicked.connect(self.go_to_login)

    def go_to_login(self):
        # Logic to go to login screen
        pass
