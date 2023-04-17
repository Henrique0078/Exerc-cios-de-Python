#Escreva um programa que pergunte a velocidade do carro de um
#usuário. Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário
#foi multado. Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de
#80 km/h.

vel = int(input("Qual a velocidade do seu carro?:  "))

if vel > 80:
     print("Voce foi multado em R$", ((vel-80)*5), " por dirigir acima da velocidade maxima permitida, que é 80 km/h")

if vel <= 80:
     print("Voce esta dentro do limite de velocidade permitida")
