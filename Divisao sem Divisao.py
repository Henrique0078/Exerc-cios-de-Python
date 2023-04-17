#Escreva um programa que leia dois números. Imprima a divisão
#inteira do primeiro pelo segundo, assim como o resto da divisão. Utilize apenas
#os operadores de soma e subtração para calcular o resultado. Lembre-se de que
#podemos entender o quociente da divisão de dois números como a quantidade
#de vezes que podemos retirar o divisor do dividendo. Logo, 20 ÷ 4 = 5, uma vez
#que podemos subtrair 4 cinco vezes de 20.

n1 = int(input("Primeiro Numero:  "))
n2 = int(input("Segundo Numero:  "))
a = 0

while n1 >= n2:
    n1 = n1 - n2
    a = a + 1

resto = n1

print(f"{n1} / {n2} = {a} e o resto desta divisão é {resto}")