#Lista de Exercícios — Estruturas de decisão
#Questão 7. Faça um algoritmo que leia três valores e mostra se a soma dos valores é par ou ímpar

#Autor: André L. B. Penha
#Data: 25.10.2024

valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
valor3 = int(input("Digite o terceiro valor: "))

soma = valor1 + valor2 + valor3

if soma % 2 == 0:
    print("A soma dos valores é par.")
else:
    print("A soma dos valores é ímpar.")
