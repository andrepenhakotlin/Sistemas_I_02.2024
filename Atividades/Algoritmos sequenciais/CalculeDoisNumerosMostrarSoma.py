#29. Lê dois números e mostra soma. Antes do resultado, deverá aparecer a mensagem: SOMA.

print()
print("** Calcule dois números e mostrar a mensagem SOMA. **")
print()
entrada_01 = int(input("Digite o primeiro número: "))
entrada_02 = int(input("Digite o segundo número: "))
print()

soma = entrada_01 + entrada_02

print()
print("A SOMA das entradas {}+{} é: {}.".format(entrada_01, entrada_02, soma))

