#Lista de Exercícios — Estruturas de decisão
#Questão 2. Faça um algoritmo que leia um número e mostrar se ele é positivo ou negativo.

#Autor: André L. B. Penha
#Data: 25.10.2024

numero = float(input("Digite um número: "))

if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")
