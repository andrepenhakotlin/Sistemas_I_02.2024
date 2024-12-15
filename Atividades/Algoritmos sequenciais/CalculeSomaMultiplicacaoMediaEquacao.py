#20 - Elabore um algoritmo que lê 4 valores inteiros e mostra: a soma dos valores; a
# subtração do 1o valor e o 2o valor; a multiplicação dos 3 primeiros valores digitados;a média dos
# valores; o resultado da equação (1o valor + 2o valor) / (3o valor – 4o valor).

print()
print("** Mostrar a soma, subtração, multiplicação, média e equação **")
print()
entrada_01 = int(input("Digite o primeiro número: "))
entrada_02 = int(input("Digite o segundo número: "))
entrada_03 = int(input("Digite o terceiro número: "))
entrada_04 = int(input("Digite o quarto número: "))
print()

soma = entrada_01 + entrada_02 + entrada_03 + entrada_04
subtracao = entrada_01 - entrada_02
multiplicacao = entrada_01 * entrada_02 * entrada_03
media = (soma + subtracao + multiplicacao)/3
equacao = (entrada_01 + entrada_02) / (entrada_03 - entrada_04)

print()
print("A soma das quatro entradas é: {}.".format(soma))
print("A subtração da primeira entrada {} e a segunda {} é: {}.".format(entrada_01, entrada_02, subtracao))
print("A multiplicação das três primeiras entradas {},{} e {} é: {}.".format(entrada_01, entrada_02, entrada_03, multiplicacao))
print("A média da soma, subtração, multiplicação é: {}.".format(media))
print("O resultado da equação (1o valor + 2o valor) / (3o valor – 4o valor). é: {}.".format(equacao))