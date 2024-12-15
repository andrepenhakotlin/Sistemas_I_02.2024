#64. Considerando uma eleição com 2 candidatos, elabore um algoritmo que lê o número total de eleitores, o número de
# votos do 1o candidato e o número de votos do 2o candidato. O algoritmo deverá apresentar o percentual de votos de
# cada um dos candidatos e o percentual de votos nulos.

print()
print("** Calcule o percentual de votos de cada candidato **")
print()

totalEleitores = float(input("Insira o número total de eleitores em uma eleição: "))
votosPrimeiroCandidato = float(input("Insira o número de votos do Primeiro candidato: "))
votosSegundoCandidato = float(input("Insira o número de votos do segundo candidato: "))


totalVotosNulos = totalEleitores - (votosPrimeiroCandidato + votosSegundoCandidato)

percentualPrimeiroCandidato = votosPrimeiroCandidato/totalEleitores*100
percentualSegundoCandidato = votosSegundoCandidato/totalEleitores*100
percentualtotalVotosNulos = (totalEleitores - votosPrimeiroCandidato - votosSegundoCandidato) / totalEleitores * 100

print()
print(" Percentual de votos do primeiro candidato: {:2.0f}%.".format(percentualPrimeiroCandidato))
print(" Percentual de votos do segundo candidato: {:2.0f}%.".format(percentualSegundoCandidato))
print(" Percentual de votos do nulos: {:2.0f}%.".format(percentualtotalVotosNulos))

