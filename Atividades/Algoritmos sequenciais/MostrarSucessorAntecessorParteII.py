#28. Lê um número e mostra seu sucessor e seu antecessor na tela.

print()
print("** Mostrar o seu sucessor e seu antecessor do número inserido **")
print()

entrada = 0
antecessor = 0
sucessor = 0

entrada = int(input("Digite um número: "))

antecessor = entrada-1
sucessor = entrada+1

print("O número inserido é {}.".format(entrada))
print("O seu antecessor é {}.".format(antecessor))
print("O seu sucessor é {}.".format(sucessor))
