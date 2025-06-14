class Pilha:
    def __init__(self):
        self.items = []

    def empilha(self, item):
        self.items.append(item)

    def desempilha(self):
        if not self.vazia():
            self.items.pop()
        return None

    def vazia(self):
         return len(self.items) == 0

    def topo(self):
        if not self.vazia():
            return self.items[-1]
        return None

p = Pilha()

for i in range(5):
    p.empilha(int(input("Digite um número: ")))

for i in range(len(p.items)):
    print(p.topo())
    p.desempilha()