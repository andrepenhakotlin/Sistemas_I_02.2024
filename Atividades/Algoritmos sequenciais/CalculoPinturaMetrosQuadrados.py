#15. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em
#metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada
#3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao
#usuário a quantidades de latas de tinta a serem compradas e o preço total.

print()
print("** Calculo de metros quadrados a ser pintada ***")
print()
area_para_pintar = int(input("Qual o tamanho em metros quadrados da area a ser pintada? ")) #120 metros

litro = area_para_pintar/3 #120/3 = 40 litros
latas = litro/18           #40/18 = 2,22 latas
preco_lata = 80
total_latas = latas * preco_lata
print()
print("O tamanho é de {} metros quadrados  e a quantidade de latas a serem utilizadas é de {:.2f} latas totalizando o preço de R$ {:.2f}.".format(area_para_pintar, latas,total_latas))

