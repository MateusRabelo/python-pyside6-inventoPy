# navigationController.py
from PySide6.QtWidgets import QStackedWidget, QWidget

class NavigationController:
    def __init__(self):
        # Inicializa o controlador de navegação com um QStackedWidget
        # QStackedWidget é usado para gerenciar múltiplos widgets, permitindo trocar entre eles
        self.stack = QStackedWidget()

    def add_widget(self, widget: QWidget, name: str):
        # Adiciona um widget ao QStackedWidget
        self.stack.addWidget(widget)
        # Define um nome para o widget, que será usado para navegação
        widget.setObjectName(name)

    def navigateTo(self, name: str):
        # Navega para o widget com o nome fornecido
        for i in range(self.stack.count()):
            # Verifica se o nome do widget na posição i é igual ao nome fornecido
            if self.stack.widget(i).objectName() == name:
                # Define o índice atual do QStackedWidget para o widget correspondente
                self.stack.setCurrentIndex(i)
                break

    def get_stack(self):
        # Retorna o QStackedWidget para ser adicionado ao layout principal
        return self.stack