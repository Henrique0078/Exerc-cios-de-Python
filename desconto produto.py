produto = float(input("Qual o valor do produto?:   "))
desconto = float(input("Qual o valor do desconto do produto?:   "))

print((produto * desconto / 100), " é o valor do desconto do produto, totalizando assim o preço de ", (produto - (produto * desconto / 100)), "reais pelo produto.")