#Lista de Exercícios — Algoritmos sequenciais
#10 - Faça um Programa que peça 2 números inteiros e um número real. Calcule e
#mostre o produto do dobro do primeiro com metade do segundo. a soma do triplo do primeiro
#com o terceiro. o terceiro elevado ao cubo

#Autor: André L. B. Penha
#Data: 25.10.2024

print()
print("** Calcule de números inteiros, real com elevação ao cubo ***")
print()
n1 = int(input('Digite o primeiro número inteiro: '))
n2 = int(input('Digite o segundo número inteiro: '))
n3 = float(input('Digite o número real: '))
print()
soma = ((2*n1) * (n2/2))
produto = (3 * n1) + n3
cubo = n3**3
print("A soma entre dois numeros inteiros é :  {}.".format(soma))
print("Informe a soma do triplo do primeiro com o terceiro é :  {}.".format(produto))
print("O número real elevado ao cubo é :  {}.".format(cubo))
