#Escreva um programa que pergunte o depósito inicial e a taxa de
#juros de uma poupança. Exiba os valores mês a mês para os 24 primeiros meses.
#Escreva o total ganho com juros no período

#Entrada de dados
deposito_inicial = float(input("Valor do depósito inicial:  "))
taxa_juros = float(input("Taxa de juros da poupança:  "))
deposito_mensal = float(input("Valor depositado mensalmente:  "))

#Calculadora para transformar anos em meses
a = int(input("Valor em anos:  "))
print(a * 12, "meses")

#variaveis mutaveis
tempo = int(input("Quanto tempo deseja deixar o dinheiro rendendo:  "))
resultado = deposito_inicial
mes = 0
taxa_juros = taxa_juros / 100
deposito = deposito_inicial

#Estrutura de repetição
while mes <= tempo:
    print("O valor no mes %d é de R$%5.2f" % (mes, resultado))
    resultado = resultado + deposito_mensal + (resultado * taxa_juros)
    mes = mes + 1

#Exibição do valor final
deposito = deposito + (deposito_mensal * (mes - 1))
total = resultado - deposito
print("O valor que voce depositou foi R$%5.2f, retirando esse valor do liquido da conta fica R$%5.2f de rendimento nos ultimos %d meses" % (deposito, total, tempo))
