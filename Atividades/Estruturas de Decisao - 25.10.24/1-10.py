#Lista de Exercícios — Estruturas de decisão
#Questão 10. Faça um algoritmo que leia dois números inteiros, efetue a adição e a multiplicação;
#Se o resultado da multiplicação for menor que 75, mostre na tela os valores e a soma, senão
#mostre os valores e a multiplicação

#Autor: André L. B. Penha
#Data: 25.10.2024

num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

soma = num1 + num2
multiplicacao = num1 * num2

if multiplicacao < 75:
    print(f"Valores: {num1}, {num2}")
    print(f"Soma: {soma}")
else:
    print(f"Valores: {num1}, {num2}")
    print(f"Multiplicação: {multiplicacao}")
