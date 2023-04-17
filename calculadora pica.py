#Escreva um programa que leia dois números e que pergunte qual
#operação você deseja realizar. Você deve poder calcular a soma (+), subtração (-),
#multiplicação (*) e divisão (/). Exiba o resultado da operação solicitada.

n1 = float(input("Primeiro numero:  "))
n2 = float(input("Segundo numero:  "))
op = input("Operação desejada:  ")

if op == "+" :
    print(n1 + n2)

elif op == "-" :
    print(n1-n2)

elif op == "*" :
    print(n1 * n2)

elif op == "/" :
    print(n1 / n2)

else :
    print("Selecione um operador valido EX: +, -, *, /.")