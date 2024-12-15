#6. 34. Elabore um algoritmo que lê dois números e mostre os seguintes resultados: Dividendo, Divisor, Quociente, Resto.
#d. Resto (para calcular o resto de uma divisão, utilize o operador MOD

print()
print("** Mostrar dividendo, divisor, quociente e resto do número inserido **")
print()

dividendo = int(input("Digite o primeiro número: "))
divisor = int(input("Digite o segundo número: "))

quociente = dividendo/divisor
resto = dividendo % divisor
print()
print("Dividendo {} ** divisor {} ** quociente {} ** resto {} ".format(dividendo, divisor, quociente, resto))