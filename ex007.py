import random

def conta(a, b):
    if b > a:
        return a + b
    else:
        return a - b

resultado = 1
while resultado != 0:
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    resultado = conta(a, b)
    print("{} +/- {}: {}".format(a, b, resultado))

