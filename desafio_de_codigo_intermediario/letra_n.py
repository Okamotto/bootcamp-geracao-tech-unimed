"""
# Desafio - Alfabeto

Dada a letra N do alfabeto, nos diga qual a sua posição.

## Entrada
Um único caracter N, uma letra maiúscula ('A'-'Z') do alfabeto (que contém 26 letras).

## Saída
Um único inteiro, que representa a posição da letra no alfabeto.

| Exemplos de Entrada | Exemplos de Saída |
| ------- | -------- |
| C | 3 |
| J | 10 |
| Z | 26 |
| A | 1 |
"""

#Solução

letra = input()

print(ord(letra)-96) #funcionou em meu computador e não no desafio

print(ord(letra)-64) #funcionou no desafio e não no meu computador
