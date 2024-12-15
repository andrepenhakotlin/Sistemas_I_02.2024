#11 - Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que
#calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) – 58

print()
print("** Calcule do peso ideal **")
print()

peso = float(input('Informe seu peso: '))
h = float(input('Informe sua altura: '))

peso_ideal = (72.7*h) - 58

if peso < peso_ideal:
	print()
	print('Abaixo do peso ideal!')
elif peso == peso_ideal:
	print()
	print('Dentro do peso ideal!')
else:
	print()
	print('Acima do peso ideal!')
	print()
print ('Peso: %.2f ' %(peso))
print ('Peso ideal: %.2f <==' %(peso_ideal))