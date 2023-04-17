#Exercício 5.14 Escreva um programa que leia números inteiros do teclado. O programa deve ler os números até que
#o usuário digite 0 (zero). No final da execução,
#exiba a quantidade de números digitados, assim como a soma e a média aritmética.

n = 0
x = 0

while True:
 n1 = int(input("Digite numeros para fazer a média, ou 0 para encerrar:  "))
 if n1 != 0:
  x += 1
  n += n1

 else:
  break

media = n / x
soma = n
qnt = x

print(f"Você digitou {qnt} numeros, e a soma deles deu {soma}, já a media aritmética dos mesmos deram {media}")