T = [-10, -8, 0, 1, 2, 5, -2, -4]
maior = T[0]
menor = T[0]
soma = 0
x = 0
for e in T:
    if e > maior:
        maior = e

    elif e < menor:
        menor = e

    soma += e
    x += 1

media = (soma / x)

print(f"Maior temperatura foi {maior}º e a menor foi {menor}º, já a média foi de {media:.2f}º")
