#Lista de Exercícios — Estruturas de Repetição
#Questão 4. Faça um programa que mostra na tela a soma dos números pares de 1 até 50 e
#mostra quantos números foram utilizados para calcular a soma.

#Autor: André L. B. Penha
#Data: 26.10.2024

soma = 0
cont = 0

for i in range(1, 51):
    if i % 2 == 0:  
        soma += i
        cont += 1

print("A soma dos números pares de 1 a 50 é:", soma)
print("Quantidade de números pares utilizados:", cont)
