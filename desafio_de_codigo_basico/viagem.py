# SOLUÇÃO

valores = input().split()

CONSUMO_CARRO = 12
tempo = int(valores[0])
velocidade_media = int(valores[1])

combustivel_necessario = (tempo * velocidade_media) / CONSUMO_CARRO

print(f"{combustivel_necessario:.3f}")
