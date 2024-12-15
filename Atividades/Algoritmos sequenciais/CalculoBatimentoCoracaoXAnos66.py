#66. O coração humano bate em média uma vez por segundo. Desenvolva um algoritmo para calcular e mostrar quantas vezes
# o coração de uma pessoa baterá se viver X anos. Considere como dado de entrada a idade da pessoa.

# Considerações: 1 ano = 365,25 dias, 1 dia = 24 horas, 1 hora = 60 minutos e 1 minuto = 60 segundos

print()
print("** Calcule o batimento do coração de X anos **")
print()

idadeDoHumano = float(input("Insira a idade para cálculo dos batimentos: "))

quantidadeBatimentosMinuto = 60
quantidadeBatimentosHora = 60*60
quantidadeBatimentosAno = 60*60*24*365.25

print()
print(" Batimentos do coração por minuto: {:2.0f}.".format(quantidadeBatimentosMinuto))
print(" Batimentos do coração por hora: {:2.0f}.".format(quantidadeBatimentosHora))
print(" Batimentos do coração por dia: {:2.0f}.".format(quantidadeBatimentosDia))
print(" Batimentos do coração por ano: {:2.0f}.".format(quantidadeBatimentosAno))

