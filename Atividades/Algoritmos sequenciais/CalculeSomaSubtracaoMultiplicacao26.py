#26 - Elabore um algoritmo que lê 3 valores, mostra a soma do 1o e do 3o valor, a divisão do 3o pelo 2o valor,
# o produto do 1o e 2o valor e a subtração do 2o e 3o valor.

print()
print("** Calcule a soma, subtração e a Multiplicação - Parte II **")
print()
entrada_01 = int(input("Digite o primeiro número: "))
entrada_02 = int(input("Digite o segundo número: "))
entrada_03 = int(input("Digite o terceiro número: "))
print()

soma = entrada_01 + entrada_03
divisao = entrada_03 / entrada_02
multiplicacao = entrada_01 * entrada_02
subtracao = entrada_02 - entrada_03

print()
print("A soma das entradas {}+{} é: {}.".format(entrada_01, entrada_03,soma))
print("A divisão das entradas {}/{} é: {}.".format(entrada_02, entrada_03,divisao))
print("A multiplicação das entradas {}X{} é: {}.".format(entrada_01, entrada_02, multiplicacao))
print("A subtração das entradas {}-{} é: {}.".format(entrada_02, entrada_03, subtracao))
