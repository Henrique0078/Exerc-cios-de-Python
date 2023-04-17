L = [3,7,2,4,1]
minimo = L[0]
for e in L:
    if e < minimo:
        minimo = e
    print(f"{minimo} é o menor valor")