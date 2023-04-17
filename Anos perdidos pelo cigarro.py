#Escreva um programa para calcular a redução do tempo de vida de
#um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos
#ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro,
#calcule quantos dias de vida um fumante perderá. Exiba o total em dias.

qnt_cigas = int(input("Quantos cigarros voce fuma por dia:  "))
anos = float(input("Há quantos anos voce fuma:  "))

perde_vida =  (((qnt_cigas * 10) * (anos * 365) /60)/24)

print(f"Voce perdeu {perde_vida} dias de vida")