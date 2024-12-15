#25 - Lê três números e mostra a soma dos dois primeiros números lidos, a subtração dos dois últimos números lidos
# e a multiplicação dos 3 números.

print()
print("** Calcule a soma, subtração e a Multiplicação    **")
print()
entrada_01 = int(input("Digite o primeiro número: "))
entrada_02 = int(input("Digite o segundo número: "))
entrada_03 = int(input("Digite o terceiro número: "))
print()

soma = entrada_01 + entrada_02
subtracao = entrada_02 - entrada_03
multiplicacao = entrada_01 * entrada_02 * entrada_03

print()
print("A soma das duas entradas é: {}.".format(soma))
print("A subtração da segunda entrada {} e a terceira {} é: {}.".format(entrada_02, entrada_03, subtracao))
print("A multiplicação das três primeiras entradas {},{} e {} é: {}.".format(entrada_01, entrada_02, entrada_03, multiplicacao))
