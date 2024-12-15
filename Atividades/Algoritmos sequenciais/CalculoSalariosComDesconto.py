#14 - Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
# 8% para o INSS e 5% para o sindicato, faça um programa que nos dê: salário bruto, quanto pagou ao INSS, quanto pagou
# ao sindicato, o salário líquido, calcule os descontos e o salário líquido, conforme tabela abaixo:

#- Salario Bruto: R$
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato (5%) : R$
#- Salario Liquido : R$

print()
print("** Salário com descontos **")
print()

valor_hora = float(input("Digite o valor da hora trabalhada: "))
numero_horas = int(input("Digite a quantidade de horas trabalhadas no mês: "))
salario_bruto = numero_horas * valor_hora
ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
descontos = ir + inss + sindicato
salario_liquido = salario_bruto - descontos
print()
print("+ Salário Bruto : R$ {:.2f}.".format(salario_bruto))
print("- IR (11%) : R$ {:.2f}.".format(ir))
print("- INSS (8%) : R$ {:.2f}.".format(inss))
print("- Sindicato ( 5%) : R$ {:.2f}.".format(sindicato))
print("+ Salário Líquido : R$ {:.2f}.".format(salario_liquido))
