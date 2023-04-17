#Escreva um programa que leia um número e verifique se é ou não
#um número primo. Para fazer essa verificação, calcule o resto da divisão do número
#por 2 e depois por todos os números ímpares até o número lido. Se o resto de uma
#dessas divisões for igual a zero, o número não é primo. Observe que 0 e 1 não são
#primos e que 2 é o único número primo que é par.

while True:
    print("------------------------------Digite 1000 para sair------------------------------")
    n = int(input("Digite um número:"))
    if n < 0:
        print("Número inválido. Digite apenas valores positivos")
    elif n == 0 or n == 1:
        print(f"{n} é um caso especial.")
    elif n == 1000:
        break
    else:
        if n == 2:
            print("2 é primo")
        elif n % 2 == 0:
            print(f"{n} não é primo, pois 2 é o único número par primo.")
        else:
            x = 3
            while (x < n):
                if n % x == 0:
                    break
                x = x + 2
            if x == n:
                print(f"{n} é primo")
            else:
                print(f"{n} não é primo, pois é divisível por {x}")