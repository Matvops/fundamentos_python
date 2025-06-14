print("{:=^30}".format("CLASSIFICAR IDADE"))

def classificar_idade(idade):
    if idade < 12:
        print("Criança")
    elif idade < 17:
        print("Adolescente")
    else:
        print("Adulto")

def somar_list(lista):
    soma = 0
    for i, nome in enumerate(lista):
        soma += nome
    return soma

classificar_idade(int(input("Digite uma idade: ")))

lista = []
for i in range(5):
    lista.append(int(input("Digite um número: ")))

print(somar_list(lista))
