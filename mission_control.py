# Mission Control AI

missao = "Apollo 18"
equipe = "Asas Livres"

dados_missao = [
    [24, 92, 88, 96, 90],
    [27, 80, 72, 94, 85],
    [31, 65, 58, 91, 70],
    [36, 42, 38, 87, 55],
    [39, 28, 19, 78, 35],
    [34, 55, 32, 82, 50]
]

areas_monitoradas = [
    "Temperatura interna",
    "Comunicação com a base",
    "Sistema de energia",
    "Suporte de oxigênio",
    "Estabilidade operacional"
]


def analisar_temperatura(valor):
    if valor < 18:
        return "ATENÇÃO", 1
    elif valor <= 30:
        return "NORMAL", 0
    elif valor <= 35:
        return "ATENÇÃO", 1
    else:
        return "CRÍTICO", 2


def analisar_comunicacao(valor):
    if valor < 30:
        return "CRÍTICO", 2
    elif valor < 60:
        return "ATENÇÃO", 1
    else:
        return "NORMAL", 0


def analisar_bateria(valor):
    if valor < 20:
        return "CRÍTICO", 2
    elif valor < 50:
        return "ATENÇÃO", 1
    else:
        return "NORMAL", 0


def analisar_oxigenio(valor):
    if valor < 80:
        return "CRÍTICO", 2
    elif valor < 90:
        return "ATENÇÃO", 1
    else:
        return "NORMAL", 0


def analisar_estabilidade(valor):
    if valor < 40:
        return "CRÍTICO", 2
    elif valor < 70:
        return "ATENÇÃO", 1
    else:
        return "NORMAL", 0


def classificar_ciclo(risco):
    if risco <= 2:
        return "MISSÃO ESTÁVEL"
    elif risco <= 5:
        return "MISSÃO EM ATENÇÃO"
    else:
        return "MISSÃO CRÍTICA"


riscos = []
pontuacao_areas = [0, 0, 0, 0, 0]

print("=" * 60)
print("MISSION CONTROL AI")
print("=" * 60)
print("Missão:", missao)
print("Equipe:", equipe)
print("Quantidade de ciclos analisados:", len(dados_missao))

for i, ciclo in enumerate(dados_missao, start=1):

    resultados = [
        analisar_temperatura(ciclo[0]),
        analisar_comunicacao(ciclo[1]),
        analisar_bateria(ciclo[2]),
        analisar_oxigenio(ciclo[3]),
        analisar_estabilidade(ciclo[4])
    ]

    risco = 0

    for j, resultado in enumerate(resultados):
        risco += resultado[1]
        pontuacao_areas[j] += resultado[1]

    riscos.append(risco)

    print("\n" + "-" * 40)
    print(f"CICLO {i}")
    print("-" * 40)
    print("Temperatura:", ciclo[0], "°C")
    print("Comunicação:", ciclo[1], "%")
    print("Bateria:", ciclo[2], "%")
    print("Oxigênio:", ciclo[3], "%")
    print("Estabilidade:", ciclo[4], "%")
    print("Pontuação de risco:", risco)
    print("Classificação:", classificar_ciclo(risco))

if riscos[-1] > riscos[0]:
    tendencia = "A missão apresentou tendência de piora."
elif riscos[-1] < riscos[0]:
    tendencia = "A missão apresentou tendência de melhora."
else:
    tendencia = "A missão permaneceu estável."

area_mais_afetada = areas_monitoradas[
    pontuacao_areas.index(max(pontuacao_areas))
]

print("\n" + "=" * 60)
print("RELATÓRIO FINAL")
print("=" * 60)

print("Maior risco:", max(riscos))
print("Risco médio:", round(sum(riscos) / len(riscos), 2))
print("Área mais afetada:", area_mais_afetada)
print("Tendência:", tendencia)

print("\nPontuação por área:")
for area, pontos in zip(areas_monitoradas, pontuacao_areas):
    print(area, "-", pontos, "pontos")