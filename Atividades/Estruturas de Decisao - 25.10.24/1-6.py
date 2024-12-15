#Lista de Exercícios — Estruturas de decisão
#Questão 6. Faça um algoritmo que leia dois números inteiros e efetue a adição; Se o resultado
#for maior que 10, mostre na tela a soma, senão mostre os dois valores apenas.

#Autor: André L. B. Penha
#Data: 25.10.2024

n1 = int(input("Digite o primeiro número inteiro: "))
n2 = int(input("Digite o segundo número inteiro: "))

soma = n1 + n2

if soma > 10:
    print("A soma é:", soma)
else:
    print("Os números são:", n1, "e", n2)
