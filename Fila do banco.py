ultimo = 10
fila = list(range(1,ultimo+1))
while True:
    print("\nExistem %d clientes na fila" % len(fila))
    print("Fila atual:", fila)
    print("Digite F para adicionar um cliente ao fim da fila,")
    print("ou A e B para realizar o atendimento.\nS para sair.")
    operacao = input("Operação (F, A, B ou S):")
    if operacao == "A" or operacao == "a":
     if(len(fila))>0:
        atendido = fila.pop(0)
        print("Cliente %d atendido" % atendido)
     else:
        print("\nFila vazia! Ninguém para atender.")
    elif operacao == "B" or operacao == "b":
     if(len(fila))>0:
        atendido = fila.pop(0)
        print("Cliente %d atendido" % atendido)
     else:
        print("\nFila vazia! Ninguém para atender.")
    elif operacao == "F" or operacao == "f":
       ultimo+=1 # Incrementa o ticket do novo cliente
       fila.append(ultimo)
    elif operacao == "S" or operacao == "s":
        break
    else:
       print("Operação inválida! Digite apenas F, A ou S!")
