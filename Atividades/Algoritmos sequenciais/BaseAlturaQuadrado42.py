#42. Elabora um algoritmo onde o usuário informa o tamanho de um quadrado e o resultado é mostrar a área e o
# perímetro do quadrado (Perímetro; 4 * L; área = L**2 ).

print()
print("** Calcule o tamanho de um quadrado e mostre área e o perímetro **")
print()
lado = int(input("Digite  um lado do quadrado: "))

area = lado**2
perimetro = lado*4
print()
print("A área do quadrado é {} e o perimetro {}.".format(area, perimetro))