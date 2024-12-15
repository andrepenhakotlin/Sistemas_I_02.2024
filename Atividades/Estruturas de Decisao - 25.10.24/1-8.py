#Lista de Exercícios — Estruturas de decisão
#Questão 8. Faça um algoritmo que leia três valores e indica quantos são pares e quantos são ímpares.

#Autor: André L. B. Penha
#Data: 25.10.2024

def contar_pares_impares():
    pares = 0
    impares = 0
    
    for i in range(3):
        valor = int(input(f"Digite o {i + 1}º valor: "))
        
        if valor % 2 == 0:
            pares += 1
        else:
            impares += 1
    
    print(f"Números pares: {pares}")
    print(f"Números ímpares: {impares}")

contar_pares_impares()
