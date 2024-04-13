class Celula:
    """
    Representa um elemento em uma lista duplamente ligada.

    Atributos:
        conteudo: O conteúdo armazenado na célula
        proximo: Referência para a próxima célula na lista.
        anterior: Referência para a célula anterior na lista.
    """
    def __init__(self, conteudo):
        self.conteudo = conteudo
        self.proximo = None
        self.proximo = None

class ListaDuplamenteLigada:
    """
    Representa uma lista duplamente ligada.

    Atributos:
        _inicio: Referência para o primeiro elemento da lista.
        _fim: Referência para o último elemento da lista.
        _quantidade: Quantidade de elementos na lista.
    """
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