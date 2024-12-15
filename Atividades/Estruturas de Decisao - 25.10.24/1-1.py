#Lista de Exercícios — Estruturas de decisão
#Questão 1. Faça um algoritmo que lê um número e verificar se ele é par ou é ímpar.

#Autor: André L. B. Penha
#Data: 25.10.2024


numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")
