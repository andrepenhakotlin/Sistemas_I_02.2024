#38. Elabore um algoritmo que calcula e mostra a média das notas de todos os alunos de Algoritmos e Lógica de Programação.

print()
print("** Mostrar a média de 2 notas **")
print()

nota1 = float(input("Digite a primeira nota de algoritmo: "))

nota2 = float(input("Digite a segunda nota de lógica de programação: "))

# calcula média
media = (nota1 + nota2) / 2
print()
# imprime a média
print(f'Média final: {media}')