#Lista de Exercícios — Estruturas de Repetição
#Questão 7. Faça um programa que mostra na tela a soma dos números ímpares de 20 até 50 e
#mostra o total de valores somados.

#Autor: André L. B. Penha
#Data: 26.10.2024

soma = 0
cont = 0

for i in range(20, 51):
    if i % 2 != 0:  
        soma += i
        cont += 1

print("A soma dos números ímpares de 20 a 50 é:", soma)
print("Quantidade de números ímpares utilizados:", cont)
