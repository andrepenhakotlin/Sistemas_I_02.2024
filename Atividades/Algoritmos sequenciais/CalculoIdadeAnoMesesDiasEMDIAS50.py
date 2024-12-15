#50. Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e mostre-a expressa apenas em dias.

import datetime

print()
print("** Converta sua idade de anos, em meses e em dias **")
print()

idade = float(input('Informe sua idade: '))

anos =  365 * idade
mes = 12 * idade
idadeEmDias =  360 * 52
print()
print("Idade é {:2.0f}".format(idade))
print("A idade em meses é {:2.0f}".format(mes))
print("A idade em dias é {:2.0f}".format(anos))

