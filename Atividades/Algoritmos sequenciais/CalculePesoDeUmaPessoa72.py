#72. Faça um algoritmo que lê o peso (só a parte inteira) e calcula:

#• o peso da pessoa em gramas
#• novo peso, considerando que a pessoa pode engordar 12%
#• novo peso, onde a pessoa passará o valor em % do que engordou

print()
print("** Calcule o peso de uma pessoa **")
print()

peso = int(input('Insira o peso de uma pessoa a ser convertido: '))

print()
pesoEmGramas = peso*1000
pesoAte12PorCento =  peso + ((peso * 12)/100)

print("O peso {} em gramas é: {}.".format(peso, pesoEmGramas))
print("Considerando que engordou 12% o novo peso é {}.".format(pesoAte12PorCento))



