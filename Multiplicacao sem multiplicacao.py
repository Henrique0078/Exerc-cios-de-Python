#Escreva um programa que leia dois números. Imprima o resultado da
#multiplicação do primeiro pelo segundo. Utilize apenas os operadores de soma e
#subtração para calcular o resultado. Lembre-se de que podemos entender a multiplicação de dois números como somas sucessivas de um deles. Assim, 4 × 5 = 5
#+ 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4.

n1 = int(input("Primeiro Numero:  "))
n2 = int(input("Segundo Numero:  "))
a = 1
b = 0

while a <= n2 :
    b = b + n1
    a = a + 1

print(f"{n1} x {n2} = {b}")