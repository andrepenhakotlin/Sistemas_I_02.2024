#8 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
## Calcule e mostre o total do seu salário no referido mês.

#Autor: André L. B. Penha
#Data: 25.10.2024

print()
print("** Total de salário no mês **")
print()

valor_hora_dia = float(input("Digite o valor da hora trabalhada: "))
numero_horas_mes= float(input("Digite a quantidade de horas trabalhadas no mês: "))

salario_mensal = valor_hora_dia * numero_horas_mes
print()

print("- Valor hora dia R$ {:.2f}.".format(valor_hora_dia))
print("- Valor de horas trabalhadas no mês R$ {:.2f}.".format(numero_horas_mes))

print("+ Salário mensal é de: R$ {:.2f}.".format(salario_mensal))



