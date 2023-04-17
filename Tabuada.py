#Modifique o programa anterior de forma que o usuário também
#digite o início e o fim da tabuada, em vez de começar com 1 e 10.

n = int(input("Tabuada de:  "))
x = int(input("Multiplicado até quantos:  "))
c = int(input("Começa multiplicando com quanto:  "))


while c <= x:
    print(n * c)
    c = c + 1