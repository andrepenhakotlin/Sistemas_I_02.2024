#Lista de Exercícios — Estruturas de decisão
#Questão 9. Faça um algoritmo que leia três valores e mostra quantos são negativos.

#Autor: André L. B. Penha
#Data: 25.10.2024

valores = []
for i in range(3):
    valor = float(input(f"Digite o {i + 1}º valor: "))
    valores.append(valor)

negativos = sum(1 for v in valores if v < 0)

print(f"Quantidade de valores negativos: {negativos}")
