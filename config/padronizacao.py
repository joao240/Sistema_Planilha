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

def recomendar_motor(respostas):
    melhor_motor = None
    melhor_pontuacao = 0

    for motor in obter_motores():
        pontuacao = 0
        
        # Comparações e pontuação
        if motor['potencia'] >= respostas.get('potencia', 0):
            pontuacao += 1
        if motor['tensao'] == respostas.get('tensao'):
            pontuacao += 1
        if motor['tipo_combustivel'] == respostas.get('combustivel'):
            pontuacao += 1
        if motor['rpm'] >= respostas.get('rpm', 0):
            pontuacao += 1
        if motor['fase'] == respostas.get('fase'):
            pontuacao += 1
        if motor['frequencia'] == respostas.get('frequencia'):
            pontuacao += 1
        if motor['tipo_arranque'] == respostas.get('arranque'):
            pontuacao += 1

        # Atualiza o melhor motor encontrado
        if pontuacao > melhor_pontuacao:
            melhor_pontuacao = pontuacao
            melhor_motor = motor

    # Exibe e retorna o resultado final
    if melhor_motor:
        print(f"\n✅ Melhor motor encontrado:")
        print(f"Nome: {melhor_motor['nome']}")
        print(f"Potência: {melhor_motor['potencia']} W")
        print(f"Tensão: {melhor_motor['tensao']} V")
        print(f"Combustível: {melhor_motor['tipo_combustivel']}")
        print(f"RPM: {melhor_motor['rpm']}")
        print(f"Fase: {melhor_motor['fase']}")
        print(f"Frequência: {melhor_motor['frequencia']} Hz")
        print(f"Arranque: {melhor_motor['tipo_arranque']}")
        print(f"Pontuação: {melhor_pontuacao}\n")

        return melhor_motor, melhor_pontuacao
    else:
        print("\n❌ Nenhum motor compatível encontrado.\n")
        return None, 0


# Exemplo de uso:
respostas_usuario = {
    "potencia": 150,
    "tensao": 220,
    "combustivel": "diesel",
    "rpm": 1750,
    "fase": 3,
    "frequencia": 60,
    "arranque": "direto"
}

recomendar_motor(respostas_usuario)
