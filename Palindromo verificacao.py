print("----------Verifique se o numero é um palindromo----------")
x = input("Entre com o numero a ser verificado:  ")
a = 0
b = len(x) - 1

while b > a and x[a] == x[b]:
    b -= 1
    a += 1

if x[a] == x[b]:
    print("Esse numero é um palindromo")

else:
    print("Esse numero não é um palindromo")

