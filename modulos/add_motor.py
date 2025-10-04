from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QTextEdit,
    QPushButton, QComboBox, QFormLayout, QHBoxLayout, QFrame, QTabWidget,
    QScrollArea, QMessageBox
)
import mysql.connector

from PyQt5.QtCore import Qt
import sys


class addmotorWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Adicionar Motor")
        self.showMaximized()
        self.setup_ui()
        self.setStyleSheet(self.get_styles())

        self.btn_add.clicked.connect(self.salvar_motor_no_banco) 

    def salvar_motor_no_banco(self):
        try:
            dados = {
                "chave_carenado": self.input_chaveCarenado.text(),
                "modelo": self.input_Modelo.text(),
                "fornecedor": self.input_Fornecedor.text(),
                "kva_standby": self.input_standby.text(),
                "kva_prime": self.input_kva_prime.text(),
                "modelo_2": self.input_modelo_2.text(),
                "acoplamento": self.input_Aclopamento.text(),
                "comprimento": self.input_Comprimento.text(),
                "largura": self.input_Largura.text(),
                "altura": self.input_Altura.text(),
                "peso": self.input_Peso.text(),
                "vibra_stop": self.input_Vibra_stop.text(),
                "potencia": self.input_Potencia.text(),
                "injecao": self.input_Injecao.text(),
                "bomba_injetora": self.input_Marca_Bomba_Injetora.currentText(),
                "kit_rev": self.input_Marca_KIT_REV.text(),
                "diametro_polegada": self.input_Diamentro_Polegada.text(),
                "preco": self.input_Preco.text(),
                "bateria": self.input_Bateria.text(),
                "grupo": self.input_Grupo.text(),
                "modelo_t": self.input_Modelo_T.text(),
                "kw_standby": self.input_kw_standby.text(),
                "kw_prime": self.input_kw_prime.text(),
                "modelo_ms_geradores": self.input_MODELO_MS_GERADORES.text(),
                "tanque_l": self.input_Tanque_L.text(),
                "fci": self.input_FCI.text(),
                "consumo_combustivel": self.input_Consumo_Combustivel.text(),
                "capacidade_arrefecimento": self.input_Capacidade_LIQUIDO_ARREFECIMENTO.text(),
                "autonomia_8h": self.input_AUTONOMIA_8_HORAS_75_CARGA.text(),
                "filtro_ar_primario": self.input_MARCA_MODELO_FILTRO_AR_PRIMARIO.text(),
                "filtro_ar_secundario": self.input_MARCA_MODELO_FILTRO_AR_SECUNDARIO.text(),
                "filtro_combustivel": self.input_MARCA_MODELO_FILTRO_COMBUSTIVEL.text(),
                "filtro_combustivel_primeiro": self.input_MARCA_MODELO_FILTRO_COMBUSTIVEL_PRIMERIO.text(),
                "filtro_combustivel_secundario": self.input_MARCA_MODELO_FILTRO_COMBUSTIVEL_SECUNDARIO.text(),
                "filtro_oleo_lubrificante": self.input_MARCA_MODELO_FILTRO_OLEO_LUBRIFICANTE.text(),
                "oleo_lubrificante_secundario": self.input_MARCA_MODELO_OLEO_LUBRIFICANTE_SECUNDARIO.text(),
                "correia_alternador": self.input_MARCA_MODELO_CORREIA_ALTERNADOR.text(),
                "observacoes": self.input_obs.toPlainText()
            }

            # 2. Conectar ao MySQL
            conn = mysql.connector.connect(
                host="localhost",
                user="root",        # ajuste para o seu usuário
                database="power_manager"
            )
            cursor = conn.cursor()

            # 3. Montar o INSERT dinamicamente
            colunas = ", ".join(dados.keys())
            valores = ", ".join(["%s"] * len(dados))
            sql = f"INSERT INTO motores ({colunas}) VALUES ({valores})"

            cursor.execute(sql, tuple(dados.values()))
            conn.commit()

            QMessageBox.information(self, "Sucesso", "Motor adicionado ao banco com sucesso!")

        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao salvar no banco: {e}")

        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'conn' in locals() and conn.is_connected():
                conn.close()

    def setup_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(12)

        header = QLabel("Adicionar Motor ao Orçamento")
        header.setObjectName("header")
        header.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(header)

        card = QFrame()
        card.setObjectName("card")
        card_layout = QVBoxLayout(card)
        card_layout.setContentsMargins(12, 12, 12, 12)
        card_layout.setSpacing(12)

        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.North)
        tabs.setMovable(False)

        # Helper: cria uma aba com scroll contendo um form (lista de (label, widget))
        def make_tab(tab_title, rows):
            content_widget = QWidget()
            content_layout = QVBoxLayout(content_widget)
            content_layout.setContentsMargins(8, 8, 8, 8)
            content_layout.setSpacing(8)

            form = QFormLayout()
            form.setLabelAlignment(Qt.AlignLeft)
            form.setFormAlignment(Qt.AlignTop)
            form.setSpacing(10)

            for label_text, w in rows:
                # se w for QTextEdit e você quer ocupar mais espaço, setMinimumHeight
                if isinstance(w, QTextEdit):
                    w.setMinimumHeight(120)
                form.addRow(label_text, w)

            # Envolver o form num widget para o scroll
            form_container = QWidget()
            form_container.setLayout(form)

            scroll = QScrollArea()
            scroll.setWidgetResizable(True)
            scroll.setWidget(form_container)

            content_layout.addWidget(scroll)
            tab = QWidget()
            tab.setLayout(content_layout)
            tabs.addTab(tab, tab_title)
            return tab

        self.input_chaveCarenado = QLineEdit()
        self.input_chaveCarenado.setPlaceholderText("Ex: MSIK-25Carenado")
        self.input_Modelo = QLineEdit()
        self.input_Modelo.setPlaceholderText("Ex: MSIK-25")
        self.input_Fornecedor = QLineEdit()
        self.input_Fornecedor.setPlaceholderText("Ex: KF-POWER")
        self.input_standby = QLineEdit()
        self.input_standby.setPlaceholderText("Ex: 25")
        self.input_kva_prime = QLineEdit()
        self.input_kva_prime.setPlaceholderText("Ex: 23")
        self.input_modelo_2 = QLineEdit()
        self.input_modelo_2.setPlaceholderText("Ex: 4YT23-20D")

        make_tab("Identificação", [
            ("Chave Carenado:", self.input_chaveCarenado),
            ("Modelo:", self.input_Modelo),
            ("Fornecedor:", self.input_Fornecedor),
            ("KVA Stand By:", self.input_standby),
            ("KVA Prime:", self.input_kva_prime),
            ("Modelo 2:", self.input_modelo_2),
        ])

        # Dimensões & Peso
        self.input_Aclopamento = QLineEdit()
        self.input_Aclopamento.setPlaceholderText("Ex: SAE 4 / 7.5")
        self.input_Comprimento = QLineEdit()
        self.input_Comprimento.setPlaceholderText("Ex: 1870")
        self.input_Largura = QLineEdit()
        self.input_Largura.setPlaceholderText("Ex: 750")
        self.input_Altura = QLineEdit()
        self.input_Altura.setPlaceholderText("Ex: 1025")
        self.input_Peso = QLineEdit()
        self.input_Peso.setPlaceholderText("Ex: 350")
        self.input_Vibra_stop = QLineEdit()
        self.input_Vibra_stop.setPlaceholderText("Ex: 3/8 mini")

        make_tab("Dimensões & Peso", [
            ("Aclopamento:", self.input_Aclopamento),
            ("Comprimento (mm):", self.input_Comprimento),
            ("Largura (mm):", self.input_Largura),
            ("Altura (mm):", self.input_Altura),
            ("Peso (kg):", self.input_Peso),
            ("Vibra stop:", self.input_Vibra_stop),
        ])

        # Características técnicas
        self.input_Potencia = QLineEdit()
        self.input_Potencia.setPlaceholderText("Ex: 27")
        self.input_Injecao = QLineEdit()
        self.input_Injecao.setPlaceholderText("Ex: mecânico")
        self.input_Marca_Bomba_Injetora = QComboBox()
        self.input_Marca_Bomba_Injetora.addItems(["Mecânico", "Eletrônico"])
        self.input_Marca_KIT_REV = QLineEdit()
        self.input_Marca_KIT_REV.setPlaceholderText("Ex: WOODWARD")
        self.input_Diamentro_Polegada = QLineEdit()
        self.input_Diamentro_Polegada.setPlaceholderText("Ex: 2\" ")
        self.input_Preco = QLineEdit()
        self.input_Preco.setPlaceholderText("Ex: MSIK")
        self.input_Bateria = QLineEdit()
        self.input_Bateria.setPlaceholderText("Ex: 12Vcc = 1 bataria de 60 A/H")
        self.input_Grupo = QLineEdit()
        self.input_Grupo.setPlaceholderText("Ex: Grupo XYZ")
        self.input_Modelo_T = QLineEdit()
        self.input_Modelo_T.setPlaceholderText("Ex: ")
        self.input_kw_standby = QLineEdit()
        self.input_kw_standby.setPlaceholderText("Ex: ")
        self.input_kw_prime = QLineEdit()
        self.input_kw_prime.setPlaceholderText("Ex: ")
        self.input_MODELO_MS_GERADORES = QLineEdit()
        self.input_MODELO_MS_GERADORES.setPlaceholderText("Ex: ")

        make_tab("Características Técnicas", [
            ("Potência (Cv):", self.input_Potencia),
            ("Injeção:", self.input_Injecao),
            ("Bomba Injetora:", self.input_Marca_Bomba_Injetora),
            ("Marca KIT REV.:", self.input_Marca_KIT_REV),
            ("Diâmetro / Polegada:", self.input_Diamentro_Polegada),
            ("Preço:", self.input_Preco),
            ("Bateria:", self.input_Bateria),
            ("Grupo:", self.input_Grupo),
            ("Modelo T:", self.input_Modelo_T),
            ("KW Stand By:", self.input_kw_standby),
            ("KW Prime:", self.input_kw_prime),
            ("Modelo MS Geradores:", self.input_MODELO_MS_GERADORES),
        ])

        # Tanque & Consumo
        self.input_Tanque_L = QLineEdit()
        self.input_Tanque_L.setPlaceholderText("Ex: ")
        self.input_FCI = QLineEdit()
        self.input_FCI.setPlaceholderText("Ex: ")
        self.input_Consumo_Combustivel = QLineEdit()
        self.input_Consumo_Combustivel.setPlaceholderText("Ex: ")
        self.input_Capacidade_LIQUIDO_ARREFECIMENTO = QLineEdit()
        self.input_Capacidade_LIQUIDO_ARREFECIMENTO.setPlaceholderText("Ex: ")
        self.input_AUTONOMIA_8_HORAS_75_CARGA = QLineEdit()
        self.input_AUTONOMIA_8_HORAS_75_CARGA.setPlaceholderText("Ex: ")

        make_tab("Tanque & Consumo", [
            ("Tanque (L):", self.input_Tanque_L),
            ("FCI:", self.input_FCI),
            ("Consumo Combustível:", self.input_Consumo_Combustivel),
            ("Capacidade Líq. Arrefecimento (L):", self.input_Capacidade_LIQUIDO_ARREFECIMENTO),
            ("Autonomia 8h @ 75%:", self.input_AUTONOMIA_8_HORAS_75_CARGA),
        ])

        # Filtros & Lubrificação
        self.input_MARCA_MODELO_FILTRO_AR_PRIMARIO = QLineEdit()
        self.input_MARCA_MODELO_FILTRO_AR_PRIMARIO.setPlaceholderText("Ex: ")
        self.input_MARCA_MODELO_FILTRO_AR_SECUNDARIO = QLineEdit()
        self.input_MARCA_MODELO_FILTRO_AR_SECUNDARIO.setPlaceholderText("Ex: ")
        self.input_MARCA_MODELO_FILTRO_COMBUSTIVEL = QLineEdit()
        self.input_MARCA_MODELO_FILTRO_COMBUSTIVEL.setPlaceholderText("Ex: ")
        self.input_MARCA_MODELO_FILTRO_COMBUSTIVEL_PRIMERIO = QLineEdit()
        self.input_MARCA_MODELO_FILTRO_COMBUSTIVEL_PRIMERIO.setPlaceholderText("Ex: ")
        self.input_MARCA_MODELO_FILTRO_COMBUSTIVEL_SECUNDARIO = QLineEdit()
        self.input_MARCA_MODELO_FILTRO_COMBUSTIVEL_SECUNDARIO.setPlaceholderText("Ex: ")
        self.input_MARCA_MODELO_FILTRO_OLEO_LUBRIFICANTE = QLineEdit()
        self.input_MARCA_MODELO_FILTRO_OLEO_LUBRIFICANTE.setPlaceholderText("Ex: ")
        self.input_MARCA_MODELO_OLEO_LUBRIFICANTE_SECUNDARIO = QLineEdit()
        self.input_MARCA_MODELO_OLEO_LUBRIFICANTE_SECUNDARIO.setPlaceholderText("Ex: ")
        self.input_MARCA_MODELO_CORREIA_ALTERNADOR = QLineEdit()
        self.input_MARCA_MODELO_CORREIA_ALTERNADOR.setPlaceholderText("Ex: ")

        make_tab("Filtros & Lubrificação", [
            ("Filtro Ar Primário:", self.input_MARCA_MODELO_FILTRO_AR_PRIMARIO),
            ("Filtro Ar Secundário:", self.input_MARCA_MODELO_FILTRO_AR_SECUNDARIO),
            ("Filtro Combustível:", self.input_MARCA_MODELO_FILTRO_COMBUSTIVEL),
            ("Filtro Comb. + Separador Água:", self.input_MARCA_MODELO_FILTRO_COMBUSTIVEL_PRIMERIO),
            ("Filtro Combustível Secundário:", self.input_MARCA_MODELO_FILTRO_COMBUSTIVEL_SECUNDARIO),
            ("Filtro Óleo Lubrificante:", self.input_MARCA_MODELO_FILTRO_OLEO_LUBRIFICANTE),
            ("Óleo Lubrificante Secundário:", self.input_MARCA_MODELO_OLEO_LUBRIFICANTE_SECUNDARIO),
            ("Correia Alternador:", self.input_MARCA_MODELO_CORREIA_ALTERNADOR),
        ])

        # Observações
        self.input_obs = QTextEdit()
        self.input_obs.setPlaceholderText("Observações adicionais sobre o motor...")
        make_tab("Observações", [
            ("Observações:", self.input_obs),
        ])

        # Coloca as tabs no card
        card_layout.addWidget(tabs)

        # Botões finais
        btns_layout = QHBoxLayout()
        self.btn_add = QPushButton("Adicionar Motor")
        self.btn_cancel = QPushButton("Cancelar")
        btns_layout.addWidget(self.btn_add)
        btns_layout.addWidget(self.btn_cancel)
        card_layout.addLayout(btns_layout)

        main_layout.addWidget(card)

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
        QComboBox { padding-left: 6px; min-height: 28px; }
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

        /* Garantir texto das abas visível no tema escuro */
        QTabBar::tab {
            background: #0b1220;
            color: #cfe8ff;
            padding: 8px 14px;
            border-top-left-radius: 6px;
            border-top-right-radius: 6px;
        }
        QTabBar::tab:selected {
            background: #1f6feb;
            color: white;
        }
        QTabWidget::pane {
            border: 1px solid #1e293b;
            border-radius: 8px;
            margin-top: -2px;
        }
        """

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = addmotorWidget()
    win.showMaximized()
    sys.exit(app.exec_())
