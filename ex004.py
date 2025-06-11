print("{:-^50}".format(" MÉDIA ARITMÉTICA "))
nota1 = float(input("Digite o valor da primeira nota: "))
nota2 = float(input("Digite o valor da segunda nota: "))

media = (nota1 + nota2) / 2;

print("A média aritmética das notas {:.1f} e {:.1f} é: {:.1f}".format(nota1, nota2, media))

print("{:-^50}".format(" CONVERSOR DE MEDIDAS DE ESPAÇO "))

metros = float(input("Digite uma distância em metros: "))
cm = metros * 100
mm = cm * 10

print('{:.2f} metros é equivalente a: {:.0f}cm'.format(metros, cm))
print('{:.2f} metros é equivalente a: {:.0f}mm'.format(metros, mm))

