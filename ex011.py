from operator import truediv

nomes = ["Ana", "João", "Maria"]
nomes.append("Matheus")
nomes.pop()
nomes.remove("João")
print(nomes[1])

lista = []
for i in range(5):
    lista.append(input("Digite um produto: "))

print("{:=^30}".format('COMPRAS'))

for i, nome in enumerate(lista):
    print("{} - {}".format(i, nome))

lista.pop(3)
lista.sort()
print(lista)