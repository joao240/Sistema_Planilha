import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
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
        if motor['potencia'] >= respostas['potencia']:
            pontuacao += 1
        if motor['tensao'] == respostas['tensao']:
            pontuacao += 1
        if motor['tipo_combustivel'] == respostas['combustivel']:
            pontuacao += 1
        if motor['rpm'] >= respostas['rpm']:
            pontuacao += 1
        if motor['fase'] == respostas['fase']:
            pontuacao += 1
        if motor['frequencia'] == respostas['frequencia']:
            pontuacao += 1
        if motor['tipo_arranque'] == respostas['arranque']:
            pontuacao += 1

        if pontuacao > melhor_pontuacao:
            melhor_pontuacao = pontuacao
            melhor_motor = motor