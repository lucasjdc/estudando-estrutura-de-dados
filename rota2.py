from ed.lista_duplamente_ligada import ListaDuplamenteLigada, Celula

class Loja:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

    def __repr__(self):
        return "{} - {}".format(self.nome, self.endereco)
    
def situacao(lista):
    print(f"Quantidade: {lista.quantidade}")
    lista.imprimir()

def main():
    loja1 = Loja("Minimercado", "Rua das Flores, 12")
    loja2 = Loja("Hortifruti", "Av das Borboletas, 23")
    loja3 = Loja("Padaria Pão Quente", "Rua das Árvores, 3")
    loja4 = Loja("Supermecado", "Rua do Pomar, 23")
    loja5 = Loja("Mercado", "Rua das Flores, 98")
    loja6 = Loja("Quitanda", "Rua da Fazenda, 899")

    lista = ListaDuplamenteLigada()
    lista.inserir_no_inicio(loja1)
    lista.inserir_no_inicio(loja2)
    lista.inserir_no_inicio(loja3)
    lista.inserir_no_fim(loja4)
    lista.inserir_no_fim(loja5)
    lista.inserir_no_fim(loja6)

    situacao(lista)
    



main()