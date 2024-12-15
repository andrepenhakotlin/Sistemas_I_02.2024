#Função: Valor a pagar em uma padaria
#Autor: André Penha
#Data: 24/09/2023

#44. A padaria HotBread vende uma certa quantidade de pães franceses e uma quantidade de broas a cada dia. Cada pãozinho
# custa R$ 0,12 e a broa custa R$ 1,50. Ao final do dia, o dono quer saber quanto arrecadou com a venda dos pães e broas
# (juntos), e quanto deve guardar numa conta de poupança (10% do total arrecadado). Você foi contratado para fazer os
# cálculos para o dono. Com base nestes fatos, faca um algoritmo para ler as quantidades de pães e de broas, e depois
# calcular os dados solicitados.

print()
print("** Controle de vendas de pães e broas ***")
print()
paes = int(input("Digite a quantidade de pães: "))
broas = int(input("Digite a quantidade de broas: "))

valor_vendas = 0.12 * paes + 1.50 * broas
valor_poupanca = 0.10 * valor_vendas

print("-----------------------------")
print("PADARIA HOT-PÃO")
print("-----------------------------")
print("*** VENDAS DO DIA ***")
print("-----------------------------")
print("QTDE. DE PÃES ....: R$ {:.2f}".format(paes))
print("QTDE. DE BROAS ....: R$ {:.2f}".format(broas))
print()
print("TOTAL DE VENDAS ..: R$ {:.2f}".format(valor_vendas))
print("VALOR POUPADO ....: R$ {:.2f}".format(valor_poupanca))

