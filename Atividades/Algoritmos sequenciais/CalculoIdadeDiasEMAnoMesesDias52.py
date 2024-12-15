#50. Faça um algoritmo que leia a idade de uma pessoa expressa em dias e mostre-a expressa em anos, meses e dias.
import datetime

print()
print("** Converta sua idade de dias, em anos, meses e dias **")
print()

idade = float(input('Informe sua idade em dias: '))

anos =  365 * idade
mes = 12 * idade
idadeEmDias = anos
print()
print("Idade atual em anos é : {:2.0f}".format(idade))
print("A idade em meses é {:2.0f}".format(mes))
print("A idade em dias é {:2.0f}".format(anos))

