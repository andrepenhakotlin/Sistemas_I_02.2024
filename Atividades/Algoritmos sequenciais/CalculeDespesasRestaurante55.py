#55. Todo restaurante, embora por lei não possa obrigar o cliente a pagar, cobra 10% para o garçom.
# Faça um programa que leia o valor gasto com as despesas realizadas em um restaurante e mostre o valor total com a
# gorjeta.

print()
print("** Calcule as despesas de um restaurante mais gorjeta **")

print()
salarioFuncionarios = float(input("Salário de funcionários: "))
despesasAlimentacao = float(input("Despesas com alimentação: "))
despesasLimpeza= float(input("Material de limpeza: "))
despesasEnergiaEletrica = float(input("Despesas com Energia Elétrica: "))
despesasAgua = float(input("Despesas com água: "))
percentualGarcom = float(input("Digite o percentual do garçom: "))
quantidadeGarcons = float(input("Número de garçons: "))
print()

despesasTotal = salarioFuncionarios + despesasAlimentacao + despesasLimpeza + despesasEnergiaEletrica + despesasAgua
despesasPercentualGorjeta = (quantidadeGarcons + despesasTotal) * percentualGarcom/100


print("Salário de funcionários: {:2.2f}.".format(salarioFuncionarios))
print("Despesas com alimentação: {:2.2f}.".format(despesasAlimentacao))
print("Material de limpeza: {:2.2f}.".format(despesasLimpeza))
print("Despesas com Energia Elétrica: {:2.2f}.".format(despesasEnergiaEletrica))
print("Despesas com água: {:2.2f}.".format(despesasAgua))
print("Percentual do garçom: {:2.0f}%.".format(percentualGarcom))
print("Quantidade de garçons: {:2.0f}.".format(quantidadeGarcons))
print()
print("Despesas  total: {:2.2f}.".format(despesasTotal))
print("Gorjetas  sobre despesas: {:2.2f}.".format(despesasPercentualGorjeta))

