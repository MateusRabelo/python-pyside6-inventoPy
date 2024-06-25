from PySide6.QtWidgets import QApplication, QSplashScreen, QLabel, QVBoxLayout, QHBoxLayout, QDialog
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

from app.views.authentication import LoginWindow
from main import MainWindow

import time

from environment.envVariables import SPLASHSCREEN_PATH

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    # Criar a splash screen
    splash_pix = QPixmap(SPLASHSCREEN_PATH)
    splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)

    # Criar um layout horizontal para a splash screen
    layout = QHBoxLayout(splash)
    splash.setLayout(layout)

    # Adicionar a imagem à splash screen
    image_label = QLabel()
    image_label.setPixmap(splash_pix.scaled(100, 100, Qt.AspectRatioMode.KeepAspectRatio))
    layout.addWidget(image_label)

    # Adicionar uma mensagem à splash screen
    message = QLabel("Loading . . .")
    message.setStyleSheet("font-size: 24px; color: white;")
    layout.addWidget(message, Qt.AlignLeft | Qt.AlignBottom)

    splash.show()

    # Simular um carregamento demorado
    time.sleep(5)

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