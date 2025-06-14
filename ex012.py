nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
ativo = True

pessoa = (nome, idade, ativo)

print(pessoa)

if pessoa[1] > 17:
    print("Maior De idade")
else:
    print("Menor de idade")
    print("Menor de idade")