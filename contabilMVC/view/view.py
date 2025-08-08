import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout,QLabel,QListWidget
class ContaView:
   def __init__(self):
      #Se ainda não existir um QApplication, cria um.
       if not QApplication.instance():
          self.app = QApplication(sys.argv)
       else:
          self.app = QApplication.instance()
        
          super().__init__()
          self.initUI()
   
   def initUI(self):
      self.setWindowTitle("Contas Contábeis")
      self.setGeometry(300, 300, 400, 300)

      layout = QVBoxLayout()
      self.label = QLabel("Movimentações da conta:")
      layout.addWidget(self.label)

      self.lista = QListWidget()
      layout.addWidget(self.lista)

      self.setLayout(layout)
      self.show() #mostra a janela assim que a view for criada.
    
   def mostrar_mensagem(self, mensagem):
       #exibe uma mensagem na lista da interface
       self.lista.addItem(mensagem)
       print(mensagem)  # também imprime no console para depuração
    
   def executar(self):
      #executa o loop da aplicação , se for o processo principal
      if hasattr(self, 'app'):
         self.exit(self.app.exec_())

   

      