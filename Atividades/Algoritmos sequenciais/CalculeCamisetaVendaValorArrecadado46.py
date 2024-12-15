#46. Uma fabrica de camisetas produz os tamanhos pequeno, médio e grande, cada uma sendo vendida respectivamente por
# 10, 12 e 15 reais. Construa um algoritmo em que o usuário forneça a quantidade de camisetas pequenas, medias e grandes
# referentes a uma venda, e a maquina informe quanto será o valor arrecadado.

print()
print("** Calcule o valor arrecadado de três tamanhos de camisetas **")
print()
pequenas = int(input("Digite a quantidade de camisetas pequenas: "))
medias = int(input("Digite a quantidade de camisetas médias:  "))
grandes = int(input("Digite a quantidade de camisetas grandes:  "))
print()

valorpequenas = 10.00
valormedias = 12.00
valorgrandes = 15.00

valorarrecadadopequenas = pequenas * valorpequenas
valorarrecadadomedias = medias * valormedias
valorarrecadadograndes = grandes * valorgrandes
totalvalorarrecadado = valorarrecadadopequenas + valorarrecadadomedias + valorarrecadadograndes

print()
print("A quantidade de camisetas pequenas é {}, a um custo de R$ {:.2f} cada uma. Valor total da compra é R$ {:.2f}.".format(pequenas, valorpequenas, valorarrecadadopequenas))
print("A quantidade de camisetas médias é {}, a um custo de R$ {:.2f} cada uma. Valor total da compra é R$ {:.2f}.".format(medias, valormedias, valorarrecadadomedias))
print("A quantidade de camisetas grandes é {}, a um custo de R$ {:.2f} cada uma. Valor total da compra é R$ {:.2f}.".format(grandes, valorgrandes, valorarrecadadograndes))
print()
print("=========================================================================================================")
print("O valor total arrecadado das camisetas vendidas foi de R$ {:.2f}.".format(totalvalorarrecadado))
print("=========================================================================================================")
