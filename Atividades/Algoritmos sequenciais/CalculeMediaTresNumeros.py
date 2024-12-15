#27 - Mostrar a média aritmética entre 3 números informados pelo usuário.



print()
print("** Calcule a média de 3 números **")
print()
entrada_01 = int(input("Digite o primeiro número: "))
entrada_02 = int(input("Digite o segundo número: "))
entrada_03 = int(input("Digite o terceiro número: "))
print()

media = (entrada_01 + entrada_02 + entrada_03)/3

print()

print("A média aritmética de {},{},{} é: {}.".format(entrada_01, entrada_02, entrada_03, media))

