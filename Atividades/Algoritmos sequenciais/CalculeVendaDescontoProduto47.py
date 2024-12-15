#47. Em época de pouco investimento e poucas vendas, os comerciantes estão buscando aumentar a venda de seus produtos
# oferencendo descontos. Faça um algoritmo que possa receber o valor de um produto e que mostre: o valor do produto,
# o novo valor do produto considerando um desconto de 9% e qual foi o desconto dado. Por exemplo, o valor do produto é
# R$10,00, com o desconto de 9% o valor do produto fica R$ 9,10, e o desconto foi de R$0,90

#Autor: André Penha
#Data: 24/09/2023

print()
print("** Calcule a venda de produtos com descontos ***")
print()
produto = float(input("Informe o valor do produto: "))

produtocomdesconto = produto - 0.9
valorfinal = produtocomdesconto - produto
desconto = produtocomdesconto - produto

print("O valor do produto é R$ {:.2f} com desconto de {:.2f}, o valor final é R$ {:.2f}".format(produto,desconto,produtocomdesconto))


