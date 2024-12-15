#Lista de Exercícios — Algoritmos sequenciais
#4. Faça um Programa que peça as 4 notas bimestrais e mostre a média.

#Autor: André L. B. Penha
#Data: 25.10.2024

print()
print("** Mostrar a média de 4 notas bimestrais **")
print()

nota1 = float(input("Digite a primeira nota: "))

nota2 = float(input("Digite a segunda nota: "))

nota3 = float(input("Digite a terceira nota: "))

nota4 = float(input("Digite a quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4
print()

print(f'Média final: {media}')