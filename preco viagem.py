#Escreva um programa que pergunte a distância que um passageiro
#deseja percorrer em km. Calcule o preço da passagem, cobrando R$ 0,50 por km
#para viagens de até de 200 km, e R$ 0,45 para viagens mais longas.

distancia = float(input("Qual a distancia que voce deseja percorrer:  "))

if distancia <= 200:
    print("O preço a ser pago é:", distancia * 0.50)

else:
    print("O preço a ser pago é:", distancia * 0.45)