#39. Elabore um algoritmo que lê um número e imprime a raiz quadrada do número.

import math

print()
print("** Imprime a raiz quadrada de um número **")
print()

num = float(input("Entre com um número: "))
print()
raiz = math.pow(num, 1/2)

print("A raiz quadrada de {:.0f} é: {:.2f}.".format(num,raiz))

