def func (string,string2,lista):
    quico = 0
    while (quico < len(lista)):
        if lista[quico] == string:
            print(f"Encontrou '{lista[quico].upper()}' na posição {quico} da lista")

        elif lista[quico] == string2:
            print(f"Encontrou '{lista[quico].upper()}' na posição {quico} da lista")

        elif lista[quico] != string:
            print(f"Não encontrado na posição {quico} da lista")

        quico += 1


lista = ["oi","tchau","feliz","natal"]
string = input("Entre com a string")
string2 = input("Entre com a string")

func(string,string2,lista)