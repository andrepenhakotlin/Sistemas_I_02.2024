# 71. Crie um algoritmo que leia uma hora do dia e informe quantos minutos se passaram
# desde o início do dia.

import datetime

print("** Converta horas em minutos **")
print()

d1 = datetime.datetime(2023,11,14,9, 4)
d2 = datetime.datetime.now()
minutos = 0
diff = d2 - d1

days = diff.days
years, days = days // 365, days % 365
months, days = days // 30, days % 30

seconds = diff.seconds
hours, seconds = seconds // 3600, seconds % 3600
minutes, seconds = seconds // 60, seconds % 60
minutos = diff * 60

print("Os minutos que se passaram foi de {} desde o dia: {}.".format(minutos, d1))
print(diff)


