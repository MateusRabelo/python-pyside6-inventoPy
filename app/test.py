from PySide6.QtWidgets import QApplication, QVBoxLayout, QHBoxLayout, QLabel, QWidget
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
import sys

class NewsPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Últimas Notícias")
        self.setupUI()
    
    def setupUI(self):
        mainLayout = QVBoxLayout()
        self.setLayout(mainLayout)
        
        # Title
        titleLabel = QLabel("Últimas Notícias", alignment=Qt.AlignCenter)
        titleLabel.setStyleSheet("font-size: 24px; color: white;")
        
        # First news item
        news1Layout = QHBoxLayout()
        busIcon = QLabel()
        busPixmap = QPixmap("path_to_bus_icon.png").scaled(50, 50, Qt.KeepAspectRatio)
        busIcon.setPixmap(busPixmap)
        busText = QLabel("Não recebeu seu passe? Entre em contato com o rh via e-mail ou faça um chamado.")
        busText.setStyleSheet("font-size: 16px; color: white;")
        news1Layout.addWidget(busIcon)
        news1Layout.addWidget(busText)
        
        # Second news item
        news2Layout = QHBoxLayout()
        relaxIcon = QLabel()
        relaxPixmap = QPixmap("path_to_relax_icon.png").scaled(50, 50, Qt.KeepAspectRatio)
        relaxIcon.setPixmap(relaxPixmap)
        relaxText = QLabel("Use a vontade nossos ambientes de descontração!")
        relaxText.setStyleSheet("font-size: 16px; color: white;")
        news2Layout.addWidget(relaxIcon)
        news2Layout.addWidget(relaxText)
        
        # Third news item
        news3Layout = QHBoxLayout()
        ideaIcon = QLabel()
        ideaPixmap = QPixmap("path_to_idea_icon.png").scaled(50, 50, Qt.KeepAspectRatio)
        ideaIcon.setPixmap(ideaPixmap)
        ideaText = QLabel("Tem alguma sugestão do que podemos melhorar? Se sim, deixe sua sugestão com o rh.")
        ideaText.setStyleSheet("font-size: 16px; color: white;")
        news3Layout.addWidget(ideaIcon)
        news3Layout.addWidget(ideaText)
        
        # Logo
        logoLayout = QVBoxLayout()
        logoLabel = QLabel()
        logoPixmap = QPixmap("path_to_logo.png").scaled(100, 100, Qt.KeepAspectRatio)
        logoLabel.setPixmap(logoPixmap)
        logoLabel.setAlignment(Qt.AlignCenter)
        logoText = QLabel("PYSTOCK", alignment=Qt.AlignCenter)
        logoText.setStyleSheet("font-size: 20px; color: white;")
        logoLayout.addWidget(logoLabel)
        logoLayout.addWidget(logoText)
        
        mainLayout.addWidget(titleLabel)
        mainLayout.addLayout(news1Layout)
        mainLayout.addLayout(news2Layout)
        mainLayout.addLayout(news3Layout)
        mainLayout.addLayout(logoLayout)

        self.setStyleSheet("background-color: #8a2be2;")

    def fixAllSize(self):
        self.setFixedSize(self.width(), self.height())

    def centerGenerationWindow(self):
        screen = QApplication.primaryScreen()
        screenGeometry = screen.availableGeometry()
        windowGeometry = self.frameGeometry()
        centerPoint = screenGeometry.center()
        windowGeometry.moveCenter(centerPoint)
        self.move(windowGeometry.topLeft())

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = NewsPanel()
    window.resize(400, 600)
    window.show()

    sys.exit(app.exec())