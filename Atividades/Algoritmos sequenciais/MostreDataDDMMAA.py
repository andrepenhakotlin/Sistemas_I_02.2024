#32. Entre com uma data e mostre a data no formato: DD/MM/ANO

import datetime

print()
print("** Mostrar a data no formato DD/MM/AAAA **")
print()

date_str = str(input("Digite uma data no formato DD/MM/AAAA: "))
format_str = '%d/%m/%Y' # Formato atual
datetime_obj = datetime.datetime.strptime(date_str, format_str)

# Uma vez convertida a data ficará no formato padrão 2017-12-29 00:00:00
# Usaremos o strftime() para formatar
print(datetime_obj.strftime("%d/%m/%Y"))

