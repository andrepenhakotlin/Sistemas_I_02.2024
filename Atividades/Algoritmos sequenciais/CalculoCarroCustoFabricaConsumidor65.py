#65. O custo ao consumidor de um carro novo é a soma do custo de fábrica com a percentagem do distribuidor e dos
# impostos (aplicados, primeiro os impostos sobre o custo de fábrica, e depois a percentagem do distribuidor sobre o
# resultado). Supondo que a percentagem do distribuidor seja de 28% e os impostos 45%. Escrever um algoritmo que leia o
# custo de fábrica de um carro e informe o custo ao consumidor do mesmo.

print()
print("** Calcule o custo de fabrica até a entrega ao consumidor **")
print()

valorDeFabricaCarro = float(input("Insira o valor do carro: "))

percentualDistribuidor = valorDeFabricaCarro * (28/100)
percentualImpostos = valorDeFabricaCarro * (45/100)
custoAoConsumidorCarro = valorDeFabricaCarro + percentualDistribuidor + percentualImpostos

print()
print(" Valor de fábrica do carro: {:2.0f}.".format(valorDeFabricaCarro))
print(" Valor de 28% para Distribuidora: {:2.0f}.".format(percentualDistribuidor))
print(" Valor de 45% para impostos: {:2.0f}.".format(percentualImpostos))
print(" Valor final para o consumidor: {:2.0f}.".format(custoAoConsumidorCarro))

