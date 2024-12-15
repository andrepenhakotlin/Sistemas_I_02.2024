#56. Para vários tributos, a base de cálculo é o salário mínimo. Faça um programa que leia o valor do salário mínimo
# e o valor do salário de uma pessoa. Calcule e mostre quantos salários mínimos a pessoa ganha.

print()
print("** Calcule quantos salários mínimos você ganha **")

print()
salarioFuncionario = float(input("Digite seu salário: "))

print()

quantidadeSalariosMinimos = salarioFuncionario/1320


print("Seu salário {:2.2f}.".format(salarioFuncionario))
print("Você ganha: {:2.0f} salários mínimos.".format(quantidadeSalariosMinimos))


