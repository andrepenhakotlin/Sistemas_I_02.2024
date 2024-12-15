#53. Joao recebeu seu salário de R$ 1200,00 e precisa pagar duas contas (C1=R$ 200,00 e C2=R$120,00) que estão atrasadas.
# Como as contas estão atrasadas, Joao terá de pagar multa de 2% sobre cada conta. Faca um algoritmo que calcule e
# mostre quanto restara do salário do Joao.

print()
print("** Calcule o salário aplicando os devidos descontos e multas de 2% por conta atrasada **")

print()
salarioBruto = float(input("Digite o salário: "))
primeiraConta = float(input("Digite a primeira conta: "))
segundaConta = float(input("Digite a segunda conta: "))
print()

primeiraContaComMulta = primeiraConta + primeiraConta * (2/100)
segundaContaComMulta = segundaConta + segundaConta * (2/100)

salarioLiquido = salarioBruto - (primeiraContaComMulta + segundaContaComMulta)

print()
print("O valor da primeira conta com multa é: {}.".format(primeiraContaComMulta))
print("O valor da segunda conta com multa é: {}.".format(segundaContaComMulta))
print("O salário líquido é: {}.".format(salarioLiquido))
