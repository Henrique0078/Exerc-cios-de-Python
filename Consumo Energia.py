#Escreva um programa que calcule o preço a pagar pelo fornecimento
#de energia elétrica. Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residências, I para indústrias e C para comércios. Calcule o preço a
#pagar de acordo com a tabela a seguir

qnt = float(input("Quantidade de Kwh consumidas por mês:  "))
print("As instalações são respectivamente: R para residências, I para indústrias e C para comércios.")
tpi = input("Tipo de instalação:  ")
total = 0

if tpi == "R":
    if qnt <= 500:
        total = (qnt * 0.40)
        print(f"O valor da conta de luz deste mês é R${total}")

    else:
        total = (qnt * 0.65)
        print(f"O valor da conta de luz deste mês é R${total}")

elif tpi == "C":
    if qnt <= 1000:
        total = (qnt * 0.55)
        print(f"O valor da conta de luz deste mês é R${total}")

    else:
        total = (qnt * 0.60)
        print(f"O valor da conta de luz deste mês é R${total}")

elif tpi == "I":
    if qnt <= 5000:
        total = (qnt * 0.55)
        print(f"O valor da conta de luz deste mês é R${total}")

    else:
        total = (qnt * 0.60)
        print(f"O valor da conta de luz deste mês é R${total}")

else:
    print("Digite a instalação na grafia certa, que é em maiusculo e somente a primeira letra do tipo de instalação.")