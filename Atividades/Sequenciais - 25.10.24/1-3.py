#Lista de Exercícios — Algoritmos sequenciais
#3. Faça um Programa que peça dois números e imprima a soma.

#Autor: André L. B. Penha
#Data: 25.10.2024

print()
print("** Mostre a soma entre dois números  **")
print()
input_01 = int(input("Digite o primeiro número: "))
input_02 = int(input("Digite o segundo número: "))
print()
resposta = input_01 + input_02
print("A SOMA entre os números {} e {} fornecidos é: {:.0f}.".format(input_01, input_02, resposta))