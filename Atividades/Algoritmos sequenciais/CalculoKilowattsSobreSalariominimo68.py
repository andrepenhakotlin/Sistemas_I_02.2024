# 68. Antes de o racionamento de energia ser decretado, quase ninguém falava em quilowatts; mas, agora, todos
# incorporaram essa palavra em seu vocabulário. Sabe-se que 100 quilowatss de energia custa um sétimo do salário mínimo,
# fazer um algoritmo que receba o valor do salário mínimo e a quantidade de quilowatts gasta por uma residência e
# calcule. Imprima:

# • o valor em reais de cada quilowatts
# • o valor em reais a ser pago
# • o novo valor a ser pago por essa residência com um desconto de 10%

print()
print("** Calcule a quantidade de quilowatts gasto por uma residência **")
print()

salarioMinimo = float(input("Insira o valor do salário mínimo: "))
quantidadeKilowattsResidencia = float(input("Insira a quantidade quilowatts gasto por uma residência: "))

valorReaisCadaKilowatts = (salarioMinimo/7)/100
valorReaisSerPago  = valorReaisCadaKilowatts * quantidadeKilowattsResidencia
valorDoDesconto10 = (valorReaisSerPago * 10) / 100
novoValorComDesconto = valorReaisSerPago - valorDoDesconto10

print()
print(" O valor em reais de cada kilowatt é R$: {:2.2f}.".format(valorReaisCadaKilowatts))
print(" O valor a ser pago em reais é de R$ : {:2.2f}.".format(valorReaisSerPago))
print(" O novo valor a ser pago com desconto é de R$: {:2.2f}.".format(valorDoDesconto10))
print(" O valor a ser pago em reais com desconto é de R$ : {:2.2f}.".format(novoValorComDesconto))



