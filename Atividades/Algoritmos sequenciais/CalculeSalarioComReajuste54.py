#54. Escreva um algoritmo para ler o salário mensal e o percentual de reajuste. Calcular e
#escrever o valor do novo salário.

print()
print("** Calcule o salário com novo reajuste **")

print()
salarioNormal = float(input("Digite o salário: "))
percentualReajuste = float(input("Digite um percentual de reajuste: "))
print()

salarioReajuste  = salarioNormal + salarioNormal * (percentualReajuste/100)

print()
print("Percentual de reajuste: {:2.0f}%.".format(percentualReajuste))
print("Salário sem reajuste: {:2.2f}.".format(salarioNormal))
print("Salário com reajuste: : {:2.2f}.".format(salarioReajuste))


