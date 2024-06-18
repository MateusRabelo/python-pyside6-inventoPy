import sys  # Importa o módulo sys, que fornece acesso a algumas variáveis usadas ou mantidas pelo interpretador e a funções que interagem fortemente com o interpretador.
import random  # Importa o módulo random, que implementa geradores de números pseudoaleatórios para várias distribuições.
from PySide6 import QtCore, QtWidgets, QtGui  # Importa as classes e módulos necessários do PySide6, que é um conjunto de bindings Python para as bibliotecas Qt usadas para criar interfaces gráficas de usuário.

class MyWidget(QtWidgets.QWidget):  # Define uma nova classe `MyWidget` que herda de `QtWidgets.QWidget`, tornando-se um widget personalizado.
    def __init__(self):  # Método construtor da classe, inicializa a instância.
        super().__init__()  # Chama o construtor da classe pai (`QWidget`) para garantir a inicialização adequada.

        self.hello = ["Aqui a gente começa o programa", "é isso e sucesso pra vocês!", "na verdade, sucesso pra gente :)"]  # Inicializa uma variável de instância `hello` como uma lista contendo uma string vazia.

        self.button = QtWidgets.QPushButton("Botão mágico")  # Cria um botão com o texto "Botão mágico".
        self.text = QtWidgets.QLabel("Hello World! Jhon and Cheezeman", alignment=QtCore.Qt.AlignCenter)  # Cria um rótulo com o texto "Hello World" e alinha-o ao centro.

        self.layout = QtWidgets.QVBoxLayout(self)  # Cria um layout vertical para organizar widgets.
        self.layout.addWidget(self.text)  # Adiciona o rótulo ao layout.
        self.layout.addWidget(self.button)  # Adiciona o botão ao layout.

        self.button.clicked.connect(self.magic)  # Conecta o sinal de clique do botão ao método `magic`.

    @QtCore.Slot()  # Declara `magic` como um slot do Qt.
    def magic(self):  # Define o método `magic`, que será chamado quando o botão for clicado.
        self.text.setText(random.choice(self.hello))  # Atualiza o texto do rótulo com um valor aleatório da lista `hello`.

if __name__ == "__main__":  # Verifica se o script está sendo executado diretamente.
    app = QtWidgets.QApplication([])  # Cria uma aplicação Qt.

    widget = MyWidget()  # Cria uma instância do widget personalizado `MyWidget`.
    widget.resize(800, 600)  # Redimensiona o widget para 800x600 pixels.
    widget.show()  # Exibe o widget.

    sys.exit(app.exec())  # Entra no loop de eventos da aplicação e sai quando ele termina.
