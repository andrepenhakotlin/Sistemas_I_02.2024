#24 - Calcula a média das notas de Algoritmos e Lógica de Programação. Assuma que serão fornecidas 4 diferentes
# notas (2 trabalhos e 2 provas). Observe que as provas equivalem a 60% da nota final, enquanto que os trabalhos
# equivalem a 40% da nota final. Nota final = (Prova 1 + Prova 2) * 0,60 + (Trabalho 1 + Trabalho 2) * 0,40.

print()
print("** Mostrar as notas de trabalho e provas **")
print()

# digita as notas e os pesos
trabalho1 = float(input("Digite a nota do primeiro trabalho: "))

trabalho2 = float(input("Digite a nota do segundo trabalho: "))

prova1 = float(input("Digite a nota da primeira prova: "))

prova2 = float(input("Digite a nota da segunda prova: "))


provafinal = (prova1+prova2)*0.60
trabalhos = (trabalho1+trabalho2)*0.40
mediafinal = (provafinal+trabalhos)/2
print()
# imprime a média
print(f'Média final: {mediafinal}')
