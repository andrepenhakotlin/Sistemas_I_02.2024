#17 - Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet
# (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

print()
print("** Calculo de tempo aproximado para download **")
print()

arquivo = float(input("Informe do tamanho do arquivo em MegaByte: "))
print()
link = float(input("Informe a velocidade do link em Mbps: "))
print()
tempo = ((arquivo * 8) / link) / 60
print ("O tempo aproximado de download é de %.2f minutos" %tempo)