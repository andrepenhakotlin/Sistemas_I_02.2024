#37. Elabore um algoritmo que lê o raio de um círculo e mostre como saída o perímetro e a área.

print()
print("** Mostre a área e o perímetro de um círculo **")
print()

raio = int(input("Digite o raio do círculo: "))

pi = 3.14
perimetro = 2*pi*raio
area = pi * (raio*raio)
print()

print("A área do círculo é {}.".format(area))
print()
print("O perímetro do círculo é {}.".format(perimetro))



