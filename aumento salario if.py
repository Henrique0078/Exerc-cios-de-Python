#Escreva um programa que pergunte o salário do funcionário e calcule
#o valor do aumento. Para salários superiores a R$ 1.250,00, calcule um aumento de
#10%. Para os inferiores ou iguais, de 15%.

salario = float(input("Qual o valor do seu salario?:  "))

if salario > 1250:
     salario = (salario * 0.10 + salario)
     print(salario)

if salario <= 1250:
     salario = (salario * 0.15 + salario)
     print(salario)