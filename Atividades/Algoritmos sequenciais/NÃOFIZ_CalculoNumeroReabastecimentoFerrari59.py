#59. A equipe Ferrari deseja calcular o número mínimo de litros que deverá colocar no tanque de seu carro para que ele
# possa percorrer um determinado número de voltas até o primeiro reabastecimento. Escreva um algoritmo que leia o
# comprimento da pista (em metros), o número total de voltas a serem percorridas no grande prêmio, o número de
# reabastecimentos desejados, e o consumo de combustível do carro (em Km/l). Calcular e escrever o número mínimo de
# litros necessários para percorrer até o primeiro reabastecimento.
# OBS: Considere que o número de voltas entre os reabastecimentos é o mesmo.

#[Exemplo de dados de entrada]
#4000 (comprimento da pista em metros)
#70 (quantidade de voltas)
#3 (quantidade de reabastecimentos)
#3.5 (consumo em Km/l)

#[Saída para os dados de entrada acima]
#20 (quantidade mínima de litros)

print()
print("** Calculo de número de litros de um tanque até o primeiro abastecimento **")

print()
comprimentoPista = float(input("Insira o comprimento da pista em metros: "))
voltasPercorridas = float(input("Insira o número total de voltas percorridas: "))
reabastecimentoDesejados = float(input("Insira o número de reabastecimentos desejados: "))
consumoLitroKmRodado = float(input("Insira o consumo do carro em litros por km rodado: "))
litrosPrimeiroReabastecimento = float(input("Insira o números de litros necessários até o primeiro reabastecimento: "))
print()

voltasParada1 = 0

reabastecimentoParada1 = voltasPercorridas/reabastecimentoDesejados
reabastecimento1 = voltasParada1*(comprimentoPista)

#kilometrosRodados  = odometroFinal - odometroIinicial
#mediaConsumo = kilometrosRodados/litrosAbastecidos
#litrosAbastecidosTotal = litrosAbastecidos * combustivelValorLitro
#lucroTaxiLiquido = lucroTaxi - litrosAbastecidosTotal

print()
print("Total de combustivel até o 1º reabastecimento: {:.0f} litros.".format(reabastecimento1))
#print("Kilometros rodados: {:3.0f}.".format(kilometrosRodados))
#print("Média de consumo: {:.0f} kilometros por litro.".format(mediaConsumo))
#print("Despesas com combustivel: R$ {:3.2f}.".format(litrosAbastecidosTotal))
#print("Litros Abastecidos: {:.0f}.".format(litrosAbastecidos))
#print("Lucro do taxi: R$ {:3.2f}".format(lucroTaxi))
#print()
#print("Lucro do taxi menos despesas: R$ {:3.2f}".format(lucroTaxiLiquido))
