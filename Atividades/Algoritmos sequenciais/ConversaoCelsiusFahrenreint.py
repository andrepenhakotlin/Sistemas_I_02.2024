#33. Elabore um algoritmo que leia uma temperatura em graus centígrados e mostre-a convertida em graus Fahrenheit.
# A fórmula de conversão é: F = (9 * C + 160) / 5 onde F é a temperatura em Fahrenheit e C é a temperatura em centígrados.

print()
print("** Conversão de Celsius para Fahrenheit **")
print()

celsius = float(input("Digite a temperatura em graus Celsius: "))
fahrenreint = (9 * celsius + 160) / 5
print()
print("A temperatura de {} graus Celsius equivale a {} graus fahrenreint.".format(celsius,fahrenreint))



