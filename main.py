from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QTextEdit,
    QPushButton, QComboBox, QFormLayout, QHBoxLayout,
    QFrame
)
from PyQt5.QtCore import Qt
import sys


class OrçamentoWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Orçamento Técnico-Comercial")
        self.setMinimumSize(780, 680)
        self.setup_ui()
        self.setStyleSheet(self.get_styles())

    def setup_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(12)

        header = QLabel("Formulário — Informações para Orçamento")
        header.setObjectName("header")
        header.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(header)

        card = QFrame()
        card.setObjectName("card")
        card_layout = QVBoxLayout()
        card_layout.setContentsMargins(20, 20, 20, 20)
        card_layout.setSpacing(12)

        form = QFormLayout()
        form.setLabelAlignment(Qt.AlignLeft)
        form.setFormAlignment(Qt.AlignTop)
        form.setSpacing(10)

        # 1) Nome
        self.input_nome = QLineEdit()
        self.input_nome.setPlaceholderText("Ex: Rafael")
        form.addRow("1) Qual seu Nome?", self.input_nome)

        # 2) Cargo
        self.input_cargo = QLineEdit()
        self.input_cargo.setPlaceholderText("Ex: CEO")
        form.addRow("2) Qual seu Cargo?", self.input_cargo)
        

        # 3) Email
        self.input_email = QLineEdit()
        self.input_email.setPlaceholderText("Ex: nome@empresa.com.br")
        form.addRow("3) Qual seu Email?", self.input_email)

        # 4) Cidade / Estado
        self.input_cidade = QLineEdit()
        self.input_cidade.setPlaceholderText("Ex: Belo Horizonte / MG")
        form.addRow("4) Cidade e estado (destino do gerador):", self.input_cidade)

        # 5) CNPJ/CPF
        self.input_doc = QLineEdit()
        self.input_doc.setPlaceholderText("Ex: 71.504.328/0001-93")
        form.addRow("5) Qual será o CNPJ/CPF?", self.input_doc)

        # 6) Potência kVA
        self.input_kva = QLineEdit()
        self.input_kva.setPlaceholderText("Ex: 100")
        form.addRow("6) Qual Potência em kVA?", self.input_kva)

        # 7) Especificações técnicas/desenho
        self.input_esp = QTextEdit()
        self.input_esp.setPlaceholderText("Descreva se houver: especificações técnicas, desenho elétrico ou civil")
        self.input_esp.setFixedHeight(80)
        form.addRow("7) Tem especificações técnicas e/ou desenho?", self.input_esp)

        # 8) Fase / Tensão
        tira_box = QHBoxLayout()
        self.combo_fase = QComboBox()
        self.combo_fase.addItems(["Trifásico", "Bifásico", "Monofásico"])
        self.combo_tensao = QComboBox()
        self.combo_tensao.addItems(["220/127V", "380/220V", "400/230V", "Outra..."])
        tira_box.addWidget(self.combo_fase)
        tira_box.addWidget(self.combo_tensao)
        form.addRow("8) Será trifásico / bifásico / monofásico? Tensão:", tira_box)

        # 9) Aberto ou silenciado
        self.combo_tipo = QComboBox()
        self.combo_tipo.addItems(["Silenciado", "Aberto"])  
        form.addRow("9) Será aberto ou silenciado?", self.combo_tipo)

        # 10) Transferência automática / Partida manual
        self.combo_partida = QComboBox()
        self.combo_partida.addItems(["Automática (ATS)", "Partida manual"])  
        form.addRow("10) Será com transferência automática ou partida manual?", self.combo_partida)

        card_layout.addLayout(form)

        # Observações e botões
        self.input_obs = QTextEdit()
        self.input_obs.setPlaceholderText("Observações adicionais (opcional)")
        self.input_obs.setFixedHeight(80)
        card_layout.addWidget(QLabel("Observações adicionais:"))
        card_layout.addWidget(self.input_obs)

        self.input_quant = QLineEdit()
        self.input_quant.setPlaceholderText("Ex: 1")
        form.addRow("Quantidade de geradores:", self.input_quant)

        

        btns_layout = QHBoxLayout()
        btns_layout.setSpacing(12)

        card_layout.addLayout(btns_layout)
        card.setLayout(card_layout)

        main_layout.addWidget(card)

        footer = QLabel("Preencha as informações acima para que possamos montar o orçamento técnico-comercial.")
        footer.setAlignment(Qt.AlignCenter)
        footer.setObjectName("footer")
        main_layout.addWidget(footer)

        self.setLayout(main_layout)

    def get_form_data(self):
        data = {
            "nome": self.input_nome.text().strip(),
            "cargo": self.input_cargo.text().strip(),
            "email": self.input_email.text().strip(),
            "cidade_estado": self.input_cidade.text().strip(),
            "cnpj_cpf": self.input_doc.text().strip(),
            "potencia_kva": self.input_kva.text().strip(),
            "especificacoes": self.input_esp.toPlainText().strip(),
            "fase": self.combo_fase.currentText(),
            "tensao": self.combo_tensao.currentText(),
            "tipo_gerador": self.combo_tipo.currentText(),
            "partida": self.combo_partida.currentText(),
            "observacoes": self.input_obs.toPlainText().strip()
        }
        return data

    def validar(self, data):
        # valida campos essenciais
        erros = []
        if not data['nome']:
            erros.append("Nome")
        if not data['email']:
            erros.append("Email")
        if not data['cidade_estado']:
            erros.append("Cidade / Estado")
        if not data['potencia_kva']:
            erros.append("Potência (kVA)")
        return erros

    def limpar_form(self):
        self.input_nome.clear()
        self.input_cargo.clear()
        self.input_email.clear()
        self.input_cidade.clear()
        self.input_doc.clear()
        self.input_kva.clear()
        self.input_esp.clear()
        self.combo_fase.setCurrentIndex(0)
        self.combo_tensao.setCurrentIndex(0)
        self.combo_tipo.setCurrentIndex(0)
        self.combo_partida.setCurrentIndex(0)
        self.input_obs.clear()
        self.input_quant.clear()

    def get_styles(self):
        return """
        QWidget {
            background-color: #0f1720;
            color: #e6eef8;
            font-family: 'Segoe UI', Tahoma, Arial;
            font-size: 13px;
        }
        #header {
            font-size: 20px;
            font-weight: 700;
            color: #ffffff;
            padding: 8px;
        }
        #card {
            background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #0b1220, stop:1 #0f1a2b);
            border-radius: 12px;
            border: 1px solid rgba(255,255,255,0.04);
            box-shadow: 0 8px 20px rgba(0,0,0,0.6);
        }
        QLineEdit, QTextEdit, QComboBox {
            background-color: #08101a;
            border: 1px solid rgba(255,255,255,0.06);
            border-radius: 8px;
            padding: 8px;
            color: #dbeafe;
        }
        QComboBox { padding-left: 6px; }
        QLabel { color: #cfe8ff; }
        QPushButton {
            background-color: #1f6feb;
            color: #fff;
            border-radius: 8px;
            padding: 8px 14px;
            font-weight: 600;
        }
        QPushButton:hover { background-color: #3b82f6; }
        QPushButton:disabled { background-color: #264653; color: #99a3b3 }
        #footer { color: #9fb3d6; font-size: 12px; margin-top: 8px }
        """


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = OrçamentoWidget()
    win.showMaximized()
    sys.exit(app.exec_())
