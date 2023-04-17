ultimo = 10
lista = list(range(1, ultimo+1))
while True:
    print(f"Fila:", lista)
    add = input("A para adicionar e R para remover:  ").upper()
    if add == "A":
        ultimo += 1
        lista.append(ultimo)
    elif add == "R":
        if len(lista) > 1:
            lista.pop(0)
        else:
            print("Fila vazia")
    elif add == "S":
        break
    else:
        print("Comando invalido")
