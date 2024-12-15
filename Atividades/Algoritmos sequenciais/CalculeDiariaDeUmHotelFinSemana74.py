#74. Um hotel com 42 apartamentos resolveu fazer promoções para os fins de semana fora da alta temporada, isto é, nos
# meses de abril, maio, junho, agosto, setembro, outubro e novembro. A taxa da promoção é de 22% da diária normal.
# A ocupação média do hotel sem promoção é de 40%. A expectativa é aumentar a taxa de ocupação para 70%.
# Supondo que as expectativas se confirmem, faça um algoritmo que lê o valor da diária normal, calcula e mostra as
# informações:

#• O valor da diária no período da promoção;
#• O valor médio arrecadado sem a promoção, durante um mês; o valor médio arrecadado
#com a promoção, durante um mês;
#• O lucro ou prejuízo mensal com a promoção.

print()
print("** Calcule a diária de um hotel em fim de semana  **")

print()
valorDiaria = float(input("Insira o valor da diária: "))
numeroApartamentos = float(input("Insira o número de apartamentos para o fim de semana: "))

print()

diariapromocional = 0.22 * valorDiaria

valorDiariaComPromocao = valorDiaria * 8 * (42/0.4)
valorDiariaSemPromocao = diariapromocional * 8 * (42/0.7)
lucroOuPrejuizo = valorDiariaComPromocao - valorDiariaSemPromocao

print()
print("O valor da diária no período da promoção é: {:.2f}.".format(diariapromocional))
print("O valor médio arrecadado sem a promoção é: {:.2f}.".format(valorDiariaSemPromocao))
print("O valor médio arrecadado com a promoção é: {:.2f}.".format(valorDiariaComPromocao))
print()
print("Lucro ou Prejuízo é de: {:.2f}.".format(lucroOuPrejuizo))

