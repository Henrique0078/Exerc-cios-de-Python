#Escreva um programa que leia três números e que imprima o maior
#e o menor.

primeiro = int(input("Primeiro valor:  "))
segundo = int(input("Segundo valor:  "))
terceiro = int(input("Terceiro valor:  "))

maior = primeiro
if segundo > maior:
     maior = segundo

if terceiro > maior:
     maior = terceiro

print("O maior numero é", maior)

menor = primeiro
if segundo < menor:
     menor = segundo

if terceiro < menor:
     menor = terceiro

print("O menor numero é", menor)