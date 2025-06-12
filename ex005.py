from math import sqrt
from math import trunc
import emoji

num = int(input('Digite um número: '))

raiz = sqrt(num)

print("A raiz quadrada de {} é: {}".format(num, trunc(raiz)))
print("valeu" + emoji.emojize("Olá mundo :rosto_chorando_de_rir:", language='pt'))