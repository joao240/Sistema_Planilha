from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QTextEdit,
    QPushButton, QComboBox, QFormLayout, QHBoxLayout,
    QFrame
)
from PyQt5.QtCore import Qt
import sys
class addmotorWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Adicionar Motor")
        self.showMaximized()
        self.setup_ui()
        self.setStyleSheet(self.get_styles())

    def setup_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(12)

        header = QLabel("Adicionar Motor ao Orçamento")
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

         # Chave Carenado
        self.input_chaveCarenado = QLineEdit()
        self.input_chaveCarenado.setPlaceholderText("Ex: MSIK-25Carenado")
        form.addRow("ChaveCarenado:", self.input_chaveCarenado)

         # Modelo
        self.input_Modelo = QLineEdit()
        self.input_Modelo.setPlaceholderText("Ex: MSIK-25")
        form.addRow("Modelo:", self.input_Modelo)

         # Fornecedor
        self.input_Fornecedor = QLineEdit()
        self.input_Fornecedor.setPlaceholderText("Ex: KF-POWER")
        form.addRow("Modelo:", self.input_Fornecedor)

         # Kva stand by
        self.input_standby = QLineEdit()
        self.input_standby.setPlaceholderText("Ex: 25")
        form.addRow("Modelo:", self.input_standby)

        # Kva Prime
        # Modelo
        # Acoplamento
        # Comprimento
        # Largura
        # Altura
        # Potencia(Cv)
        # Injeção
        # Marca Bomba Injetora
        # Marca KIT REV.
        # Diamentro/Polegada
        # Preço
        # Peso
        # Vibra stop
        # Bateria
        # Grupo
        # Modelo T
        # Localização
        # Tanque L
        # FCI
        # PRAZO DE ENTREGA
        # Emissão
        # CONSUMO DE COMBUSTIVEL
        # Capacidade do LIQUIDO DE ARREFECIMENTO (L)
        # MARCA E MODELO FILTRO DE AR PRIMARIO
        # MARCA E MODELO FILTRO DE AR SECUNDARIO
        # MARCA E MODELO FILTRO DE COMBUSTIVEL 
        # MARCA E MODELO FILTRO DE COMBUSTIVEL PRIMERIO + SEPARADOR DE AGUA
        # MARCA E MODELO FILTRO DE COMBUSTIVEL SECUNDARIO
        # MARCA E MODELO FILTRO DE OLEO LUBRIFICANTE
        # MARCA E MODELO OLEO LUBRIFICANTE SECUNDARIO
        # MARCA E MODELO CORREIA DO ALTERNADOR
        # AUTONOMIA PARA 8 HORAS A 75% DE CARGA 
        # KW STAND BY
        # KW PRIME
        # MODELO MS GERADORES




        # Tipo de motor
        self.input_tipo_motor = QComboBox()
        self.input_tipo_motor.addItems(["Diesel", "Gasolina", "GNV", "Elétrico"])
        form.addRow("Tipo de motor:", self.input_tipo_motor)

        # Potência
        self.input_potencia = QLineEdit()
        self.input_potencia.setPlaceholderText("Ex: 1000 kW")
        form.addRow("Potência do motor:", self.input_potencia)

        # Marca
        self.input_marca = QLineEdit()
        self.input_marca.setPlaceholderText("Ex: Cummins")
        form.addRow("Marca do motor:", self.input_marca)

        # Modelo
        self.input_modelo = QLineEdit()
        self.input_modelo.setPlaceholderText("Ex: X15")
        form.addRow("Modelo do motor:", self.input_modelo)

        # Observações
        self.input_obs = QTextEdit()
        self.input_obs.setPlaceholderText("Observações adicionais sobre o motor...")
        card_layout.addLayout(form)
        card_layout.addWidget(QLabel("Observações adicionais:"))
        card_layout.addWidget(self.input_obs)

        btns_layout = QHBoxLayout()
        self.btn_add = QPushButton("Adicionar Motor")
        self.btn_cancel = QPushButton("Cancelar")
        btns_layout.addWidget(self.btn_add)
        btns_layout.addWidget(self.btn_cancel)

        card_layout.addLayout(btns_layout)
        card.setLayout(card_layout)
        main_layout.addWidget(card)
        self.setLayout(main_layout)

    def get_styles(self):
        return  """
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
    win = addmotorWidget()
    win.showMaximized()
    sys.exit(app.exec_())
