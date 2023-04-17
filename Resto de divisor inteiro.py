#Escreva um programa que calcule o resto da divisão inteira entre dois
#números. Utilize apenas as operações de soma e subtração para calcular o resultado.

divisor = int(input("Entre com o divisor:  "))
dividendo = int(input("Entre com o dividendo:  "))
quociente = 0
x = dividendo

while divisor > x:
    x += dividendo
    quociente += 1

print(f"O resto de divisão inteira de {divisor} por {dividendo} é {quociente}")
