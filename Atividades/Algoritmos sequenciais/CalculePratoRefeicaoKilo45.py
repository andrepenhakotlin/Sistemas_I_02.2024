#45. O restaurante a quilo Bem-Bao cobra R$12,00 por cada quilo de refeição. Escreva um algoritmo que leia o peso do
# prato montado pelo cliente (em quilos) e imprima o valor a pagar. Assuma que a balança ja desconte o peso do prato.

#Autor: André Penha
#Data: 24/09/2023

print()
print("** Controle de vendas de refeições ***")
print()
refeicao = float(input("Informe o peso do prato da refeição: "))

prato = 100 #gramas
valorefeicaocomprato = (12.00 * refeicao)
valorefeicaosemprato = valorefeicaocomprato - 0.100
semprato = refeicao - 0.100

print("-----------------------------")
print("RESTAURANTE BEM-BÃO")
print("-----------------------------")

print("O peso da refeição é {:.3f} gramas totalizando R$ {:.2f}".format(refeicao,valorefeicaocomprato))
print("O peso da refeição sem o peso do prato é {:.3f} gramas totalizando R$ {}".format(semprato,valorefeicaosemprato))
print("O peso do prato é {} gramas".format(prato))



