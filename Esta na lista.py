#Escreva um programa que pesquise elementos dentro de uma lista, verificando do primeiro ao ultimo
#elemento se o valor procurado esta presente.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
entrada = int(input("Entre com o numero"))

for x, y in enumerate(lista):
    if entrada == y:
        print(f"O numero {entrada} está na posição {x}")
    else:
        print(f"O numero {entrada} não esta na posição {x}")
