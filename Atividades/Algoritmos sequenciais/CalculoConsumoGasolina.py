#23 - Um carro gasta 10 litros de gasolina para andar 130 km. Sabendo que o tanque do carro comporta 60 litros,
# quantos quilômetros você conseguirá andar com o carro? Faça um algoritmo que calcula o valor e mostra na tela.


print()
print("** Calcule o consumo de combustível de um automóvel **")
print()
consumo = int(input("Digite o consumo em litros: "))
distanciapercorrida = consumo*13
#litro = 130/10 #valor do litro = 13km por litro
print()

print()
print("A distância percorrida com {} litros é: {}.".format(consumo, distanciapercorrida))
