from math import pow, floor

catetoOp = int(input("Digite o valor do cateto oposto: "))
catetoAd = int(input("Digite o valor do cateto adjacente: "))

hipotenusa = pow(catetoOp, 2) + pow(catetoAd, 2)

print("O comprimento da hipotenusa é: {}".format(floor(hipotenusa)))