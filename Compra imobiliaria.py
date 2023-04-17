#Escreva um programa para aprovar o empréstimo bancário para
#compra de uma casa. O programa deve perguntar o valor da casa a comprar, o
#salário e a quantidade de anos a pagar. O valor da prestação mensal não pode ser
#superior a 30% do salário. Calcule o valor da prestação como sendo o valor da
#casa a comprar dividido pelo número de meses a pagar.

valor = int(input("Qual o valor do imovel desejado?:  "))
salario = float(input("Qual o seu salario liquido?:  "))
anos = float(input("Quantos anos voce planeja pagar a casa?:  "))

anos = (anos * 12)
prestacao = (valor / anos)


if prestacao > (salario * 0.3):
    print(f"O valor da prestação é {prestacao} maior do que 30% do seu salario, por isso a compra do imovel nao foi aprovada.")

else:
    print(f"Voce vai pagar R${prestacao} por mês, o que é menor que 30% do seu salario, assim aprovada a compra do imovel.")