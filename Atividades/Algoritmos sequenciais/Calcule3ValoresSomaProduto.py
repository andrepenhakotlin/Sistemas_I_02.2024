#21 - Elabore um algoritmo que lê 3 valores, mostra os 3 valores, a soma e o produto.

print()
print("** Calcule três valores que mostre a soma e o produto **")
print()
entrada_01 = int(input("Digite o primeiro número: "))
entrada_02 = int(input("Digite o segundo número: "))
entrada_03 = int(input("Digite o terceiro número: "))
print()

soma = entrada_01 + entrada_02 + entrada_03
multiplicacao = entrada_01 * entrada_02 * entrada_03

print()
print("A soma das entradas {}+{}+{} é: {}.".format(entrada_01, entrada_02, entrada_03,soma))
print("A multiplicação das três primeiras entradas {}X{}X{} é: {}.".format(entrada_01, entrada_02, entrada_03, multiplicacao))
