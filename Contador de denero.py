valor = float(input("Digite o valor a pagar:"))
cédulas = 0
atual = 200
apagar = valor

while True:

 if atual <= apagar:
  apagar -= atual
  cédulas += 1

 else:
  print("%d cédula(s) de R$%5.2f" % (cédulas, atual))
  if apagar and atual == 0:
   break

  elif atual == 200:
   atual = 100
   cédulas = 0

  elif atual == 100:
   atual = 50
   cédulas = 0

  elif atual == 50:
   atual = 20
   cédulas = 0

  elif atual == 20:
   atual = 10
   cédulas = 0

  elif atual == 10:
   atual = 5
   cédulas = 0

  elif atual == 5:
   atual = 1
   cédulas = 0

  elif atual == 1:
   atual = 0.50
   cédulas = 0

  elif atual == 0.50:
   atual = 0.25
   cédulas = 0

  elif atual == 0.25:
   atual = 0.10
   cédulas = 0

  elif atual == 0.10:
   atual = 0.05
   cédulas = 0

  elif atual == 0.05:
   atual = 0.01
   cédulas = 0

  elif atual == 0.01:
   atual = 0
   cédulas = 0
