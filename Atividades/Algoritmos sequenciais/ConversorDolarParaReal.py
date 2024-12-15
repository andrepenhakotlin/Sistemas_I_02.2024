#35. Elabore um algoritmo que converta um valor em dólar (U$) para real (R$). O algoritmo deverá solicitar o valor da
# cotação do dólar e também a quantidade de dólares a ser convertida.

print()
print("** Conversão de dolar para real **")
print()

dolar = float(input("Informe a quantidade de dólar para conversão: US$ "))
cotacao = float(input ("Informe o valor da cotação do dólar: R$ "))
conversao = dolar*cotacao
print()
print('A quantidade de dólar convertido em real é: {:.2f} R$'.format(conversao))