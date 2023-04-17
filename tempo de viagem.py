#Escreva um programa que calcule o tempo de uma viagem de carro.
#Pergunte a distância a percorrer e a velocidade média esperada para a viagem.

distancia =  float(input("distancia do inicio da rota até o final em km:  "))
vm = int(input("velocidade media  em km/h:  "))
tempo = (distancia / vm)

print(f"O tempo esperado para a viagem é de {tempo} horas")
