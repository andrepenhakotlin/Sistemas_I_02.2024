#73. Um hotel deseja fazer uma promoção especial de final de semana, concedendo um desconto de 25% na diária.
# O usuário informará o número de apartamentos do hotel e o valor da diária por apartamento por final de semana.
# Elabore um algoritmo para calcular:

#• Valor promocional da diária;
#• Valor total a ser arrecadado caso a ocupação total seja (100%) seja atingida;
#• Valor total a ser arrecadado caso a ocupação seja de 70%.
#• Valor que o hotel deixará de arrecadar em virtude da promoção, caso a ocupação atinja 100%.

print()
print("** Calcule a diária de um hotel em fim de semana  **")

print()
valorDiaria = float(input("Insira o valor da diária: "))
numeroApartamentos = float(input("Insira o número de apartamentos para o fim de semana: "))

print()

valorArrecadado100Ocupacao = numeroApartamentos * valorDiaria
valorDiariaDesconto = valorDiaria - (25/100)
valorDiariaTotalDesconto = numeroApartamentos * valorDiariaDesconto * 2
valorDiariaTotalSemDesconto = numeroApartamentos * valorDiaria * 2
valorTotalArrecadado100 = numeroApartamentos * valorDiariaTotalDesconto
totalPerdaDeixouArrecadarComDesconto = valorTotalArrecadado100 - valorDiariaTotalSemDesconto

print()
print("O valor da diária promocional é: {:.2f}.".format(valorDiariaDesconto))
print("O total arrecadado com 100% de ocupação é: {:.2f}.".format(valorDiariaTotalDesconto))
print("O total de perda que deixou de arrecadar com o desconto fornecido é de R$: {:.2f}.".format(totalPerdaDeixouArrecadarComDesconto))

