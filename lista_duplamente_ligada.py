class Celula:    
    def __init__(self, conteudo):
        self.conteudo = conteudo
        self.proximo = None
        self.proximo = None

class ListaDuplamenteLigada:    
    def __init__(self):
        self._inicio = None
        self._fim = None
        self._quantidade = 0

    @property
    def inicio(self):
        return self._inicio
    
    @property
    def fim(self):
        return self._fim
    
    @property
    def quantidade(self):
        return self._quantidade
    
    def _inserir_em_lista_vazia(self, conteudo):
        celula = Celula(conteudo)
        self._inicio = celula
        self._fim = celula
        self._quantidade += 1
    
    def inserir_no_inicio(self, conteudo):
        if self.quantidade == 0:
            return self._inserir_em_lista_vazia(conteudo)
        celula = Celula(conteudo)
        celula.proximo = self.inicio
        self._inicio.anterior = celula
        self._inicio = celula
        self._quantidade += 1

    
    def inserir(self, posicao, conteudo):
        if posicao == 0:
            return self.inserir_no_inicio(conteudo)
        if posicao == self.quantidade:
            return self.inserir_no_fim(conteudo)
        esquerda = self._celula(posicao-1)
        direita = esquerda.proximo
        celula = Celula(conteudo)
        celula.proximo = direita
        celula.anterior = esquerda
        esquerda.proximo = celula
        direita.anterior = celula
        self._quantidade += 1

    def item(self, posicao):        
        celula = self._celula(posicao)
        return celula.conteudo

    def _validar_posicao(self, posicao):
        if 0 <= posicao < self.quantidade:
            return True
        raise IndexError(f"Posição inválida: {posicao}")
    
    def _celula(self, posicao):      
        self._validar_posicao(posicao)
        metade = self.quantidade // 2 # // o resultado da divisão é um número inteiro
        if posicao < metade:
            atual = self.inicio
            for i in range(0, posicao):
                atual = atual.proximo
            return atual
        atual = self.fim
        for i in range(posicao+1, self.quantidade)[::-1]:
            atual = atual.anterior
        return atual
    
    def imprimir(self):
        atual = self.inicio
        for i in range(0, self.quantidade):
            print(atual.conteudo)
            atual = atual.proximo

    def inserir_no_fim(self, conteudo):
        if self.quantidade == 0:
            return self._inserir_em_lista_vazia(conteudo)
        celula = Celula(conteudo)
        celula.anterior = self.fim
        self.fim.proximo = celula
        self._fim = celula
        self._quantidade += 1

# range(0, metate)
# range(metade, quantidade)[::-1]
# [::-1] reverte o intervalo
# range(0, posicao)
# range(posicao+1, quantidade)[::-1]
# metate = quantidade / 2

    