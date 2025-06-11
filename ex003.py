nome = input('Qual é o seu nome?')
print('Prazer em te conhecer {:->30} '.format(nome))

num = float(input("Digite um valor:"))
num2 = float(input("Digite outro valor:"))

sum = num + num2
sub = num - num2
mul = num * num2
div = num / num2
mod = num % num2
divInteira = num // num2
pot = num ** num2

print("O valor {:.2f} + {:.2f} é: {:.2f}".format(num, num2, sum))
print("O valor {:.2f} - {:.2f} é: {:.2f}".format(num, num2, sub))
print("O valor {:.2f} x {:.2f} é: {:.2f}".format(num, num2, mul))
print("O valor {:.2f} divido por {:.2f} é: {:.2f}".format(num, num2, div))
print("O módula da divisão de {:.2f} por {:.2f} é: {:.2f}".format(num, num2, mod))
print("O valor {:.2f} // {:.2f} é: {:.2f}".format(num, num2, divInteira))
print("O valor de {:.2f} sob {:.2f} é: {:.2f}".format(num, num2, pot))