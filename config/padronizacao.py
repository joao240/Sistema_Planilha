import mysql.connector

# Conexão com o banco
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # se tiver senha, coloque aqui
    database="power_manager"
)

def obter_motores():
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM motores")
    motores = cursor.fetchall()
    cursor.close()
    return motores


def _to_int(value):
    """Converte valores possivelmente em string para int de forma segura.
    Se não for possível converter, retorna 0.
    """
    try:
        if value is None:
            return 0
        if isinstance(value, (int, float)):
            return int(value)
        # tenta extrair dígitos (por ex. '220V' -> 220, '220/127V' -> 220)
        import re
        s = str(value)
        m = re.search(r"\d+", s)
        return int(m.group()) if m else 0
    except Exception:
        return 0

def recomendar_motor(respostas):
    melhor_motor = None
    melhor_pontuacao = 0

    for motor in obter_motores():
        pontuacao = 0
        
        # Comparações e pontuação (converte campos numéricos para int antes)
        if _to_int(motor.get('potencia')) >= respostas.get('potencia', 0):
            pontuacao += 1
        if _to_int(motor.get('tensao')) == respostas.get('tensao'):
            pontuacao += 1
        if str(motor.get('tipo_combustivel')).lower() == str(respostas.get('combustivel')).lower():
            pontuacao += 1
        if _to_int(motor.get('rpm')) >= respostas.get('rpm', 0):
            pontuacao += 1
        if _to_int(motor.get('fase')) == respostas.get('fase'):
            pontuacao += 1
        if _to_int(motor.get('frequencia')) == respostas.get('frequencia'):
            pontuacao += 1
        if str(motor.get('tipo_arranque')).lower() == str(respostas.get('arranque')).lower():
            pontuacao += 1

        # Atualiza o melhor motor encontrado
        if pontuacao > melhor_pontuacao:
            melhor_pontuacao = pontuacao
            melhor_motor = motor

    # Exibe e retorna o resultado final
    if melhor_motor:
        # Normaliza o dicionário do motor para garantir chaves esperadas
        motor_norm = {
            'nome': melhor_motor.get('nome', '—'),
            'potencia': _to_int(melhor_motor.get('potencia')),
            'tensao': _to_int(melhor_motor.get('tensao')),
            'tipo_combustivel': melhor_motor.get('tipo_combustivel', '—'),
            'rpm': _to_int(melhor_motor.get('rpm')),
            'fase': _to_int(melhor_motor.get('fase')),
            'frequencia': _to_int(melhor_motor.get('frequencia')),
            'tipo_arranque': melhor_motor.get('tipo_arranque', '—')
        }

        print(f"\n✅ Melhor motor encontrado:")
        print(f"Nome: {motor_norm['nome']}")
        print(f"Potência: {motor_norm['potencia']} W")
        print(f"Tensão: {motor_norm['tensao']} V")
        print(f"Combustível: {motor_norm['tipo_combustivel']}")
        print(f"RPM: {motor_norm['rpm']}")
        print(f"Fase: {motor_norm['fase']}")
        print(f"Frequência: {motor_norm['frequencia']} Hz")
        print(f"Arranque: {motor_norm['tipo_arranque']}")
        print(f"Pontuação: {melhor_pontuacao}\n")

        return motor_norm, melhor_pontuacao
    else:
        print("\n❌ Nenhum motor compatível encontrado.\n")
        return None, 0


# NOTE: Removido exemplo de uso que executava `recomendar_motor` no momento
# da importação do módulo. A função `recomendar_motor` deve ser chamada
# explicitamente a partir da interface (por exemplo, ao clicar em um botão).
