#16. Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em
#metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada
#6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em
#galões de 3,6 litros, que custam R$ 25,00.
#! Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços
#em 3 situações:

# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e
# sempre arredonde os valores para cima, isto é, considere latas cheias.
print()
print("** Calculo de metros quadrados a ser pintada entre galões e latas ***")
print()
area_para_pintar = int(input("Qual o tamanho em metros quadrados da area a ser pintada? ")) #120 metros

litro = area_para_pintar/6 #120/6 = 20 litros
galoes = litro/6         #20/6 = 3.33 galões
latas = litro/18         #20/18 = 1.11
preco_lata = 80
preco_galao = 25

if area_para_pintar < 18:
    print(" Você não pode comprar uma lata.")
    print(" Comprando galões de 3,6l, gastará R$ ", round(galoes) * preco_galao, ".")

else:
    print(" Se você comprar apenas latas de 18l, gastará R$ ", round(latas)*preco_lata, ".")
    print(" Se você comprar apenas galões de 3,6l, gastará R$ ", round(galoes)*preco_galao, ".")

## a partir daqui não está completo

mistura_lata = int(latas)
mistura_galao = int(galoes)

if area_para_pintar > mistura_lata:
    total_galao = area_para_pintar * mistura_galao
    print("Você utilizará", total_galao, "galões.")
else:
    total_misto = area_para_pintar


#print("O tamanho é de {} metros quadrados  e a quantidade de latas a serem utilizadas é de {:.2f} latas totalizando o preço de R$ {:.2f}.".format(area_para_pintar, latas,total_latas))

