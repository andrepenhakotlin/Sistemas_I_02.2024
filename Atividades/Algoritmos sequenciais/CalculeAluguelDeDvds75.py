#75. Faça um algoritmo que leia a quantidade de DVDs que uma locadora possui e o valor que ela cobra por cada aluguel,
# mostrando ao final as informações de acordo com as questões:

# Sabe-se que um terço dos DVDs são alugadas por mês, mostre o faturamento anual da locadora;
# Quando um cliente atrasa a entrega, é cobrada uma multa de 10% sobre o valor do aluguel.
# Sabe-se que um décimo dos DVDs alugados no mês são devolvidos com atraso, calcule o valor ganho com multas por mês;
# Sabe-se ainda que 2% dos DVDs acabam estragando ao longo do ano, e um décimo do total é comprado para reposição,
# mostre a quantidade de DVDs que a locadora terá no final do ano.

print()
print("** Calcule o aluguel de DVDs de uma localdora **")

print()
valorDiariaDVD = float(input("Insira o valor do aluguel do DVD: "))
quantidadeDvdsLocadora = float(input("Insira a quantidade de DVDs no acervo da locadora: "))
print()

faturamentoAnual = (quantidadeDvdsLocadora/3)*12
atrasoNaEntrega = valorDiariaDVD * (10/100)
locatariosEntregaComAtraso = (quantidadeDvdsLocadora/10)*atrasoNaEntrega
danosMateriaisAno = quantidadeDvdsLocadora * (2/100)
reposicaoDvdsPerdas = quantidadeDvdsLocadora * (10/100)
totalAcervoDvdsNoAno = quantidadeDvdsLocadora + reposicaoDvdsPerdas

print()
print("Faturamento anual da locadora: {:.2f}.".format(faturamentoAnual))
print("Quantidade DVDs no fim de ano: {:.2f}.".format(totalAcervoDvdsNoAno))
print("O valor médio arrecadado com a promoção é: {:.2f}.".format(valorDiariaComPromocao))
print()
print("Lucro ou Prejuízo é de: {:.2f}.".format(lucroOuPrejuizo))

