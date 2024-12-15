# 67. Faça um algoritmo que lê o público total de um jogo de futebol e fornece a renda do jogo, sabendo que havia
# 4 tipos de ingressos assim distribuídos: popular - 10% a R$1,00, geral - 50% a R$5,00, arquibancada - 30% a R$10,00 e
# cadeiras - 10% a R$20,00.

print()
print("** Calcule a renda de um jogo de 4 tipos de ingressos **")
print()

ingressoPopular = float(input("Insira a quantidade de ingressos popular vendidos: "))
ingressoGeral = float(input("Insira a quantidade de ingressos da geral vendidos: "))
ingressoArquibancada = float(input("Insira a quantidade de ingressos arquibancada vendidos: "))
ingressoCadeiras = float(input("Insira a quantidade de ingressos cadeiras vendidos: "))

totalTorcedoresPopular = ingressoPopular
totalTorcedoresGeral = ingressoGeral
totalTorcedoresArquibancada = ingressoArquibancada
totalTorcedoresCadeiras = ingressoCadeiras

totalPopular = ingressoPopular * (10/100)
totalGeral = ingressoGeral * (50/100)
totalArquibancada = ingressoArquibancada * (30/100)
totalCadeiras = ingressoCadeiras * (10/100)

ingressoPopular = ingressoPopular * 1.00
ingressoGeral = ingressoGeral * 5.00
ingressoArquibancada = ingressoArquibancada * 10.00
ingressoCadeiras = ingressoCadeiras * 20.00

publicoTotal = totalTorcedoresPopular + totalTorcedoresGeral + totalTorcedoresArquibancada + totalTorcedoresCadeiras
rendaDoJogo = ingressoPopular + ingressoGeral + ingressoArquibancada + ingressoCadeiras

print()
print(" Total de torcedores da arquibanca popular: {:2.0f}.".format(totalTorcedoresPopular))
print(" Total de torcedores da geral : {:2.0f}.".format(totalTorcedoresGeral))
print(" Total de torcedores da arquibancada: {:2.0f}.".format(totalTorcedoresArquibancada))
print(" Total de torcedores das cadeiras: {:2.0f}.".format(totalTorcedoresCadeiras))
print()
print(" Valor total de ingressos vendidos para popular: {:2.2f}.".format(ingressoPopular))
print(" Valor total de ingressos vendidos para geral: {:2.2f}.".format(ingressoGeral))
print(" Valor total de ingressos vendidos para as arquibanca: {:2.2f}.".format(ingressoArquibancada))
print(" Valor total de ingressos vendidos para as cadeiras: {:2.2f}.".format(ingressoCadeiras))
print()
print(" Público total:: {:2.2f}.".format(publicoTotal))
print(" Renda do jogo:: {:2.2f}.".format(rendaDoJogo))

