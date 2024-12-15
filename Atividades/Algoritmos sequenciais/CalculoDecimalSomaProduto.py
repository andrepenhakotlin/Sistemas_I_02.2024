#19 - Elabore um algoritmo que lê dois valores decimais e mostra a soma e o produto dos valores.

print()
print("** Mostrar a soma de dois decimais e o produto **")
print()
entrada_01 = float(input("Digite o primeiro número decimal: "))
entrada_02 = float(input("Digite o segundo número decimal: "))
print()

soma = entrada_01 + entrada_02
produto = (entrada_01 + entrada_02)*soma
print()
print("A soma dos valores {} e {} é = {} e o produto é = {}.".format(entrada_01, entrada_02, soma, produto))