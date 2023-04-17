matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = 0
somatotal = 0
produto = 1
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f"Posição [{linha+1}, {coluna+1}]:  "))

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f"[{matriz[linha][coluna]:^5}]", end="")
        if coluna == 0:
            soma += matriz[linha][coluna]
            produto *= matriz[linha][coluna]
        diag = matriz[1][1] + matriz[2][2] + matriz[0][0]
        somatotal += matriz[linha][coluna]
    print()

print(f"Soma da primeira coluna: {soma}")
print(f"Produto da primeira coluna: {produto}")
print(f"Soma da diagonal principal: {diag}")
print(f"Soma total da matriz: {somatotal}")
