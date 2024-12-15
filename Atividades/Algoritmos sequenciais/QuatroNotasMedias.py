#4. Faça um Programa que peça as 4 notas bimestrais e mostre a média.

print()
print("** Mostrar a média de 4 notas bimestrais **")
print()

# digita as notas e os pesos
nota1 = float(input("Digite a primeira nota: "))

nota2 = float(input("Digite a segunda nota: "))

nota3 = float(input("Digite a terceira nota: "))

nota4 = float(input("Digite a quarta nota: "))

# calcula média
media = (nota1 + nota2 + nota3 + nota4) / 4
print()
# imprime a média
print(f'Média final: {media}')