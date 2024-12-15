#22 - Um colega pediu dinheiro emprestado, você aceitou emprestar com a condição de que ele irá devolver o valor
# emprestado com juros de 15%. Qual o valor que o colega pediu e quanto ele irá devolver depois?

print()
print("** Mostrar a soma, subtração, multiplicação, média e equação **")
print()

c = int(input("Valor do empréstimo: "))
j = c * 0.15
valorcorrigido = j + c
#J = juros simples; C = capital inicial

print()

print()
print("O valor emprestado foi de: {:.2f}.".format(c))
print("O valor do juros de 15% é de: {:.2f}.".format(j))
print("O valor a ser devolvido com juros de 15% é de: {:.2f}.".format(valorcorrigido ))
