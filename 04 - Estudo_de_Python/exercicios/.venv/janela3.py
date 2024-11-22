from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QComboBox
import sys

class Janela3(QWidget):
    def __init__(self):
        super().__init__()

        # Definir o texto que irá aparecer no título da janela
        self.setWindowTitle("Cadastro de Cliente")
        # Definir a posição e tamanho da janela
        self.setGeometry(10,10,500,400)
        # Criar as labels para nome usuario, email, senha e nivel acesso
        self.label_nome_usuario = QLabel("Nome de Usuário:")
        self.label_nome_usuario.setStyleSheet("QLabel{color:#424242; font-size:10pt; font-weight:bold}")
        self.label_email = QLabel("Email:")
        self.label_email.setStyleSheet("QLabel{color:#424242; font-size:10pt; font-weight:bold}")
        self.label_senha = QLabel("Senha:")
        self.label_senha.setStyleSheet("QLabel{color:#424242; font-size:10pt; font-weight:bold}")
        self.label_nivel_acesso = QLabel("Nivel Acesso:")
        self.label_nivel_acesso.setStyleSheet("QLabel{color:#424242; font-size:10pt; font-weight:bold}")

        # Criação das LineEdits
        self.edit_nome_usuario = QLineEdit()
        self.edit_nome_usuario.setStyleSheet("QLineEdit{background-color:#e0e0e0; color:#424242; border-radius:5px; padding: 5px;}")
        self.edit_senha = QLineEdit()
        self.edit_senha.setEchoMode(QLineEdit.EchoMode.Password)
        self.edit_senha.setStyleSheet("QLineEdit{background-color:#e0e0e0; color:#424242; border-radius:5px; padding: 5px;}")
        self.edit_email = QLineEdit()
        self.edit_email.setStyleSheet("QLineEdit{background-color:#e0e0e0; color:#424242; border-radius:5px; padding: 5px;}")
        self.edit_nivel_acesso = QLineEdit()
        self.edit_nivel_acesso.setStyleSheet("QLineEdit{background-color:#e0e0e0; color:#424242; border-radius:5px; padding: 5px;}")

        self.combo_nivel_acesso = QComboBox()
        lst_nivel_acesso =["Admin", "Visualizar"]

        # Adicionar a lista a combo_nivel_acesso
        self.combo_nivel_acesso.addItems(lst_nivel_acesso)

        # Criar o botão
        self.button_cadastrar = QPushButton("Cadastrar")
        self.button_cadastrar.setStyleSheet("QPushButton{background-color:#2979ff; color:#fafafa; border-radius:5px; padding: 5px; font-weight:bold}")
        self.button_cadastrar.clicked.connect(self.mensagem)

        # Criar o layout na vertical para organizar os controles
        layout = QVBoxLayout()
        # Adicionar os controles de Layout
        layout.addWidget(self.label_nome_usuario)
        layout.addWidget(self.edit_nome_usuario)

        layout.addWidget(self.label_senha)
        layout.addWidget(self.edit_senha)

        layout.addWidget(self.label_email)
        layout.addWidget(self.edit_email)

        layout.addWidget(self.label_nivel_acesso)
        layout.addWidget(self.combo_nivel_acesso)

        layout.addWidget(self.button_cadastrar)
        

         # Adicionar o layout a tela
        self.setLayout(layout)
    
    def mensagem(self):
        print(self.edit_nome_usuario.text())
        print(self.edit_senha.text())
        print(self.edit_email.text())
        print(self.edit_nivel_acesso.text())



app = QApplication(sys.argv)
jan = Janela3()
jan.show()
app.exec_()