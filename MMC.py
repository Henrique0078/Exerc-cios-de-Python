def mmc(a,b):
    x = 2
    while True:
        if (a % x) == (b % x):
            print (x)
            break
        else:
            x += 1

mmc(6,9)