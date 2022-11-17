"""
# Desafio
A empresa que você trabalha resolveu conceder um aumento salarial a todos funcionários, de acordo com a tabela abaixo:

| Salário | Percentual de Reajuste |
| ------- | -------- |
| 0 - 600.00 | 17% |
| 600.01 - 900.00 | 13% |
| 900.01 - 1500.00 | 12% |
| 1500.01 - 2000.00 | 10% |
| Acima de 2000.00 | 5% |

Leia o salário do funcionário e calcule e mostre o novo salário, bem como o valor de reajuste ganho e o índice reajustado, em percentual.
A entrada contém apenas um valor de ponto flutuante, que pode ser maior ou igual a zero, com duas casas decimais, conforme exemplos abaixo.

#### Exemplo 1

| Exemplos de Entrada | Exemplos de Saída |
| ------- | -------- |
| 1000 | Novo salario: 1120,00 |
|      | Reajuste ganho: 120,00|                                                                                     
|      | Em percentual: 12 % |

#### Exemplo 2

| Exemplos de Entrada | Exemplos de Saída |
| ------- | -------- |
| 2000 | Novo salario: 2200,00 |
|      | Reajuste ganho: 200,00|                                                                                     
|      | Em percentual: 10 % |
"""
#SOLUÇÃO
salario = int(input())

if ((salario > 0) and (salario <= 600)):
    reajuste = salario * 0.17
    aumento = reajuste + salario
    percentual = 17
elif (salario <= 900):
    reajuste = salario * 0.13
    aumento = reajuste + salario
    percentual = 13
elif (salario <= 1500):
    reajuste = salario * 0.12
    aumento = reajuste + salario
    percentual = 12
elif (salario <= 2000):
    reajuste = salario * 0.10
    aumento = reajuste + salario
    percentual = 10
else:
    reajuste = salario * 0.05
    aumento = reajuste + salario
    percentual = 5


#texto_aumento = f'{aumento:.2f}'
#texto_aumento = texto_aumento.replace('.',',')
#texto_reajuste = f'{reajuste:.2f}'
#texto_reajuste = texto_reajuste.replace('.',',')
#print(f"Novo salário: {aumento:.2f}\nReajuste ganho: {reajuste:.2f}\n{percentual}")
print("Novo salario:", "{:.2f}".format(aumento))
print("Reajuste ganho:", "{:.2f}".format(reajuste))
print("Em percentual:", percentual, "%")