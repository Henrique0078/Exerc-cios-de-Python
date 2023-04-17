def maxminstring (x,min,max):
    if (len(x) >= min) and (len(x) <= max):
        print("Verdadeiro")

    else:
        print("False")
    print(len(x))
while True:
    x = input("OI: ")
    if x == "parar" :
        break
    min = int(input("Min: "))
    max = int(input("Max: "))

    maxminstring(x,min,max)