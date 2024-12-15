# 3. Faça um Programa que peça dois números e imprima a soma.

print()
print("** Mostre a soma entre dois números  **")
print()
entrada_01 = int(input("Digite o primeiro número: "))
entrada_02 = int(input("Digite o segundo número: "))
print()
resultado = entrada_01 + entrada_02
print("A SOMA entre os números {} e {} fornecidos pelo usuário é: {:.0f}.".format(entrada_01,entrada_02,resultado))