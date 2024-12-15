# 70. Efetuar o cálculo do valor de uma prestação em atraso, utilizando a fórmula:
# prestação = valor + (valor * (taxa/100)*tempo)

print()
print("** Calcule a prestação em atraso com sua taxa  de juros **")
print()

valorPrestacao = float(input("Insira o valor da prestação: "))
tempoAtraso = float(input("Insira os dias em atraso: "))
taxaJuros = float(input("Insira o percentual de juros: "))

valorPrestacao = valorPrestacao
tempoAtraso = tempoAtraso
taxaJuros = taxaJuros

valorJuros = valorPrestacao * (taxaJuros/100)
jurosAcumulados = valorJuros * tempoAtraso
valorTotalPagar = valorPrestacao + jurosAcumulados

print()
print(" O valor da prestação é de R$: {:2.2f}.".format(valorPrestacao))
print(" Tempo de atraso é de R$: {:2.0f} dias.".format(tempoAtraso))
print(" A taxa de juros é de: {:2.2f}%.".format(taxaJuros))
print()
print(" O valor de juros por dia é de R$ : {:2.2f}.".format(valorJuros))
print(" Juros acumulados foi de R$: {:2.2f}.".format(jurosAcumulados))
print(" A prestação a pagar incluindo juros acumulados é de R$: {:2.2f}.".format(valorTotalPagar))



