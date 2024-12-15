#49. Lê um valor de hora e informa quantos minutos se passaram desde início do dia.

import datetime

print()
print("** Calcular quantos minutos se passaram desde o início do dia - FORMATO 24 HORAS **")
print()

horainicial = float(input('Informe a hora inicial: '))

minutos = horainicial * 60

print("Desde o início do dia até a hora informada já se passaram {:2.2f} minutos.".format(minutos))

