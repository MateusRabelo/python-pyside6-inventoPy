from PySide6.QtWidgets import QApplication, QSplashScreen, QLabel, QVBoxLayout, QHBoxLayout, QDialog
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, QPoint

from app.views.authentication import LoginWindow
from app.views.application import MainWindow

import time

from environment.envVariables import SPLASHSCREEN_PATH

class SplashScreen(QSplashScreen):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUI()

    def initUI(self):
        # Criar um layout horizontal para a splash screen
        layout = QHBoxLayout(self)
        self.setLayout(layout)

        # Adicionar a imagem à splash screen
        splashPix = QPixmap(SPLASHSCREEN_PATH)
        imageLabel = QLabel()
        imageLabel.setPixmap(splashPix.scaled(100, 100, Qt.AspectRatioMode.KeepAspectRatio))
        layout.addWidget(imageLabel)

        # Adicionar uma mensagem à splash screen
        message = QLabel("Loading . . .")
        message.setStyleSheet("font-size: 40px; color: white;")
        layout.addWidget(message, Qt.AlignLeft | Qt.AlignBottom)

        self.centerDialog()

    def centerDialog(self):
        screen = QApplication.primaryScreen()
        screenGeometry = screen.availableGeometry()
        windowGeometry = self.frameGeometry()
        centerPoint = screenGeometry.center()
        windowGeometry.moveCenter(centerPoint)
        # offset = screenGeometry.topLeft() - windowGeometry.topLeft()
        self.move(windowGeometry.topLeft() - QPoint(180, 100))

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    splash = SplashScreen()
    splash.show()

    # Simular um carregamento demorado
    time.sleep(2)

    # Fechar a splash screen
    splash.close()

    # Criar e exibir a janela de login
    login_window = LoginWindow()
    login_window.setWindowModality(Qt.ApplicationModal)
    if login_window.exec() == QDialog.Accepted:
        main_window = MainWindow()
        main_window.show()
        main_window.fixAllSize()
        sys.exit(app.exec())
