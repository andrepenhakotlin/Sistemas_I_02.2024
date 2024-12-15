#57 - Escreva um algoritmo para ler o número de eleitores de um município, o número de votos brancos, nulos e
# válidos. Calcular e escrever o percentual que cada um representa em relação ao total de eleitores.

#[Exemplo de dados de entrada]
#200 (quantidade de eleitores)
#10 (quantidade de votos brancos)
#20 (quantidade de votos nulos)
#160 (quantidade de votos válidos)

#[Saída para os dados de entrada acima]
#5 (percentual de votos brancos)
#10 (percentual de votos nulos)
#80 (percentual de votos válidos)

print()
print("** Calcule o número de eleitores de um município, o número de votos brancos, nulos e válidos **")

print()
numeroEleitores = float(input("Insira o números de eleitores: "))
votosBrancos = float(input("Insira quantidade de votos brancos: "))
votosNulos = float(input("Insira quantidade de votos nulos: "))
votosValidos = float(input("Insira quantidade de votos válidos: "))
print()

votosBrancos  = (votosBrancos*100)/numeroEleitores
votosNulos  = (votosNulos*100)/numeroEleitores
votosValidos  = (votosValidos*100)/numeroEleitores

print()
print("Percentual de votos brancos: {:.0f}%.".format(votosBrancos))
print("Percentual de votos nulos: {:.0f}%.".format(votosNulos))
print("Percentual de votos válidos: {:.0f}%".format(votosValidos))
