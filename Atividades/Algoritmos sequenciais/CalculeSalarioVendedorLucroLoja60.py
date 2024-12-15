#60. Uma loja vende bicicletas com um acréscimo de 50% sobre o seu preço de custo. Ela paga a cada vendedor 2 salários
# mínimos mensais, mais uma comissão de 15% sobre o preço de custo de cada bicicleta vendida, dividida igualmente entre
# eles. Escreva um algoritmo que leia o número de empregados da loja, o valor do salário mínimo, o preço de custo de
# cada bicicleta, o número de bicicletas vendidas, calcule e escreva: O salário final de cada empregado e o lucro
# (líquido) da loja.
#
# [Exemplo de dados de entrada]
# 4 (quantidade de empregados da loja)
# 300 (valor do salário mínimo)
# 150 (preço de custo de cada bicicleta)
# 200 (quantidade de bicicletas vendidas)

#[Saída para os dados de entrada acima]
# 1725 (salário final de cada empregado)
# 8100 (lucro da loja)

print()
print("** Calcule o salário final e o lucro da loja **")

valorBicicleta = 150
bicicletasVendidas = 200
quantidadeVendedores = 4

valorBicicletaAcrescimo = valorBicicleta * (50/100)
comissaoCadaBicicleta = valorBicicleta * (15/100)
comissãoDivididaEntreVendedores = comissaoCadaBicicleta/quantidadeVendedores

ValorSalarioMinimo = 300
doisSalariosMinimos = 300 * 2

salarioFinalEmpregado  = doisSalariosMinimos + comissãoDivididaEntreVendedores
lucroBrutoLoja  = (valorBicicleta * bicicletasVendidas) + valorBicicletaAcrescimo
lucroLiquidoLoja  = lucroBrutoLoja - salarioFinalEmpregado

print()
print("O valor do salário mínimo é : {:.2f}.".format(ValorSalarioMinimo))
print("O valor da bicicleta é: {:.2f}.".format(valorBicicleta ))
print("Total de biciletas vendidas: : {:.2f}.".format(bicicletasVendidas))
print("Quantidade de vendedores: {:.0f}.".format(quantidadeVendedores))
print()
print("O salário do vendedor é de dois salários mínimos : {:.2f}.".format(doisSalariosMinimos))
print("O valor da bicicleta com acréscimo de 50% é : {:.2f}.".format(valorBicicletaAcrescimo))
print("Comissão de 15% cada bicicleta é: : {:.2f}.".format(comissaoCadaBicicleta))
print("A comissão dividida entre 4 vendedores é de : {:.2f}.".format(comissãoDivididaEntreVendedores))
print("O salário final do empregado é de : {:.0f}.".format(salarioFinalEmpregado))
print("Lucro bruto que a loja obteve é de : {:.0f}.".format(lucroBrutoLoja))
print("Lucro líquido que a loja obteve é de : {:.0f}.".format(lucroLiquidoLoja))

