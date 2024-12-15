# 69. Em épocas de pouco dinheiro, os comerciantes estão procurando aumentar suas vendas oferecendo desconto.
# Faça um algoritmo que possa entrar com o valor de um produto e imprima o novo valor tendo em vista que o
# desconto foi de 9%.

print()
print("** Calcule um produto com desconto de 9% **")
print()

produto = float(input("Insira o valor do produto: "))

valorProduto = produto
produtoComDesconto = produto * (9/100)
novoValorComDesconto = valorProduto - produtoComDesconto

print()
print(" O valor do produto é de R$: {:2.2f}.".format(valorProduto))
print(" O desconto foi de R$: {:2.2f}.".format(produtoComDesconto))
print(" O novo valor a ser pago pelo produto incluindo desconto é de R$ : {:2.2f}.".format(novoValorComDesconto))



