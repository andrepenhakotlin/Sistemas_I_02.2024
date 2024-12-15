#31. Elabore um algoritmo que lê 6 números decimais e mostra a soma e a subtração dos valores digitados.

print()
print("** Calcule seis números decimais e mostre a soma e a subtração **")
print()
entrada_01 = float(input("Digite o primeiro número: "))
entrada_02 = float(input("Digite o segundo número: "))
entrada_03 = float(input("Digite o terceiro número: "))
entrada_04 = float(input("Digite o quarto número: "))
entrada_05 = float(input("Digite o quinto número: "))
entrada_06 = float(input("Digite o sexto número: "))
print()

soma = entrada_01 + entrada_02 + entrada_03 + entrada_04 + entrada_05 + entrada_06
subtracao = (entrada_01 - entrada_02) - (entrada_03 - entrada_04) - (entrada_05 - entrada_06)

print()
print("A soma das seis entradas é: {}.".format(soma))
print("A subtração das seis entradas é: {}.".format(subtracao))
