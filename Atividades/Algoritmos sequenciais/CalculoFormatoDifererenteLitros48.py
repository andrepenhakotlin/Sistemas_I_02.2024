#48. A fabrica de refrigerantes Meia-Cola vende seu produto em três formatos: lata de 350 ml, garrafa de 600 ml e
# garrafa de 2 litros. Se um comerciante compra uma determinada quantidade de cada formato, faca um algoritmo para
# calcular quantos litros de refrigerante ele comprou.

print()
print("** Calcule o formato de diferente mls e litros para obtenção dos litros adquiridos **")
print()
qtdformato350ml = float(input("Digite a quantidade de formatos de 350ml: "))
qtdformato600ml  = float(input("Digite a quantidade de formatos de 600ml:  "))
qtdformatolitros  = float(input("Digite a quantidade de formatos de 2 litros: "))
print()

totalformato350ml = 0.350 * qtdformato350ml
totalformato600ml = 0.600 * qtdformato600ml
totalformatolitros = 2 * qtdformatolitros
qtdtotallitros = totalformato350ml + totalformato600ml + totalformatolitros

print()
print("A quantidade total de latas é de {:.0f} de 350 ml com {:.3f} litros.".format(qtdformato350ml,totalformato350ml))
print("A quantidade total de garrafas é de {:.0f} de 600 ml com {:.3f} litros.".format(qtdformato600ml ,totalformato600ml))
print("A quantidade total de garrafas é de {:.0f} de 2 litros com {:.0f} litros.".format(qtdformatolitros ,totalformatolitros))

print()
print("=========================================================================================================")
print("A quantidade total em litros dos formatos produzidos pela fábrica é de {:.3f}.".format(qtdtotallitros ))
print("=========================================================================================================")
