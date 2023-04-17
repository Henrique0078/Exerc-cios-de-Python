def bubble(lista):
    if len(lista) > 1:
        for vertical in range(0, len(lista)):
            for horizontal in range(0, len(lista)-1):
                if lista[horizontal] > lista[horizontal+1]:
                    salvo = lista[horizontal+1]
                    lista[horizontal+1] = lista[horizontal]
                    lista[horizontal] = salvo
            print(lista)

lista = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
bubble(lista)
