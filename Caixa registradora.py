#Escreva um programa para controlar uma pequena máquina registradora.
#Você deve solicitar ao usuário que digite o código do produto e a quantidade
#comprada. Utilize a tabela de códigos abaixo para obter o preço de cada produto:

x = 0
y = 0
z = 0
total = 0

while True:
 codigo = int(input("Digite o código do produto ou 0 para encerrar o programa:  "))

 if (codigo == 1):
  qnt = int(input("Quantos produtos vai querer:  "))
  total += (qnt * 0.50)
  x += 1

 elif (codigo == 2):
   qnt = int(input("Quantos produtos vai querer:  "))
   total += (qnt * 1.00)
   x += 1

 elif (codigo == 3):
  qnt = int(input("Quantos produtos vai querer:  "))
  total += (qnt * 4.00)
  x += 1

 elif (codigo == 5):
  qnt = int(input("Quantos produtos vai querer:  "))
  total += (qnt * 7.00)
  x += 1

 elif (codigo == 9):
   qnt = int(input("Quantos produtos vai querer:  "))
   total += (qnt * 8.00)
   x += 1

 elif (codigo == 0):
  break

 else:
  print("Código invalido")

print(f"Voce comprou {x} produtos diferentes totalizando {total:.2f}")
