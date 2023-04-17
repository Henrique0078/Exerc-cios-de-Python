salario = float(input("Qual o valor do seu salario?:   "))
aumento = float(input("Qual o valor do aumento do seu salario em porcentagem?:   "))

print((salario * aumento / 100), "este é o valor do aumento, totalizando assim", ((salario * aumento / 100)+ salario), "reais")