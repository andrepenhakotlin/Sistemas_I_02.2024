#51. Um funcionário recebe um salário fixo mais 4% de comissão sobre as vendas. Faca
#um algoritmo que receba o salário fixo de um funcionário e o valor de suas vendas, calcule e
#mostre a comissão e o salário final do funcionário.

import datetime

print()
print("** Cálculo de salário mais comissão **")
print()

salarioFixo = float(input('Informe o salário fixo: '))
vendas = float(input('Informe o valor das vendas: '))

comissaoPrcentual = 4/100
comissao = vendas * 4/100
salarioFinal = comissao + salarioFixo

print()
print("Mostre o percentual de comissao: {:2.2f}".format(comissaoPrcentual))
print("Mostre a comissao: {:2.2f}".format(comissao))
print("Salário fixo do funcionário: {:2.2f}".format(salarioFixo))
##print("Comissão recebida: {:2.0f}".format(valorVendas))
print("Salário final do funcionário: {:2.2f}".format(salarioFinal))

