#43. Calcule e mostre a área de um triângulo e mostre a área de um losango.

print()
print("** Calcule e mostre a área de um triângulo e losango. **")
print()

base = int(input("Digite a base do triângulo: "))
altura = int(input("Digite a altura do triângulo: "))
areatriangulo = (base * altura)/2
print("--------------------------------------")
diagonalmenor = int(input("Digite a diagonal do losango  - menor: "))
diagonamaior = int(input("Digite a diagonal do losango - maior: "))
arealosango = (diagonamaior*diagonalmenor)/2
print("//////////////////////////////////////")
print("A área do triangulo é {:.0f}.".format(areatriangulo))
print("A área do losango é {:.0f}.".format(arealosango))
