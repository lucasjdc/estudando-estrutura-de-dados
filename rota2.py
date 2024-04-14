from ed.lista_duplamente_ligada import ListaDuplamenteLigada, Celula

class Loja:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

    def __repr__(self):
        return "{} - {}".format(self.nome, self.endereco)
    
def main():
    loja1 = Loja("Minimercado", "Rua das Flores, 12")
    loja2 = Loja("Hortifruti", "Av das Borboletas, 23")
    loja3 = Loja("Padaria Pão Quente", "Praça da Árvore")

    lista = ListaDuplamenteLigada()
    print(f"Quantidade: {lista.quantidade}")

    lista.inserir_no_inicio(loja1)

    print(f"Quantidade: {lista.quantidade}")
    print(lista.item(0))

    lista.inserir_no_inicio(loja2)
    print(f"Quantidade: {lista.quantidade}")
    print(lista.item(0))

    lista.inserir_no_inicio(loja3)
    print(f"Quantidade: {lista.quantidade}")    

    lista.imprimir()
    



main()