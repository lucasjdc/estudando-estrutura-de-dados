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

    
    def item(self, posicao):
        """
        Retorna o conteúdo do elemento na posição especificada na lista.

        Args:
            posicao: A posição do elemento na lista.

        Retorno:
            O conteúdo do elemento na posição especificada.
        """
        celula = self._celula(posicao)
        return celula.conteudo

    def _validar_posicao(self, posicao):
        if 0 <= posicao < self.quantidade:
            return True
        raise IndexError(f"Posição inválida: {posicao}")
    
    def _celula(self, posicao):
        """
        Retorna a célula na posição especificana na lista.

        Args:
            posicao: A posição da célula na lista.

        Retorno:
            A célula na posição especificada
        """
        self._validar_posicao(posicao)
        atual = self.inicio
        for i in range(0, posicao):
            atual = atual.proximo
        return atual
    
    def imprimir(self):
        atual = self.inicio
        for i in range(0, self.quantidade):
            print(atual.conteudo)
            atual = atual.proximo

