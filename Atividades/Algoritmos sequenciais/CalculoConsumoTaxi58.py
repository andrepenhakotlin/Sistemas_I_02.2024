#58. Um motorista de taxi deseja calcular o rendimento de seu carro na praça. Sabendo-se que o preço do combustível é de
# R$ 2,50 , escreva um algoritmo para ler: a marcação do odômetro (Km) no início do dia, a marcação (Km) no final do
# dia, o número de litros de combustível gasto e o valor total (R$) recebido dos passageiros. Calcular e escrever:
# a média do consumo em Km/L e o lucro (líquido) do dia.

#[Exemplo de dados de entrada]
#1500 (marcação no início do dia)
#1700 (marcação no fim do dia)
#20 (quantidade de litros de combustível)
#80 (valor recebido)

#[Saída para os dados de entrada acima]
#10 (média de consumo)

print()
print("** Calculo de consumo de um taxi **")

print()
combustivelValorLitro = float(input("Insira o valor do combustivel por litro: "))
litrosAbastecidos = float(input("Insira litros abastecidos: "))
odometroIinicial = float(input("Insira o odômetro inicial: "))
odometroFinal = float(input("Insira o odômetro final: "))
lucroTaxi = float(input("Insira o lucro do dia do taxi: "))
print()

kilometrosRodados  = odometroFinal - odometroIinicial
mediaConsumo = kilometrosRodados/litrosAbastecidos
litrosAbastecidosTotal = litrosAbastecidos * combustivelValorLitro
lucroTaxiLiquido = lucroTaxi - litrosAbastecidosTotal

print()
print("O valor do combustivel por litro: {:2.2f}.".format(combustivelValorLitro))
print("Kilometros rodados: {:3.0f}.".format(kilometrosRodados))
print("Média de consumo: {:.0f} kilometros por litro.".format(mediaConsumo))
print("Despesas com combustivel: R$ {:3.2f}.".format(litrosAbastecidosTotal))
print("Litros Abastecidos: {:.0f}.".format(litrosAbastecidos))
print("Lucro do taxi: R$ {:3.2f}".format(lucroTaxi))
print()
print("Lucro do taxi menos despesas: R$ {:3.2f}".format(lucroTaxiLiquido))
