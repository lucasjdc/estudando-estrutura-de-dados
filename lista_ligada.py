class Celula:
    def __init__(self, conteudo):
        """
        Inicializa uma célula da lista encadeada.

        Args:
            conteudo: O conteúdo a ser armazenado na célula.
        """
        self.conteudo = conteudo
        self.proximo = None

class ListaLigada:
    def __init__(self):
        """
        Inicializa uma lista encadeada vazia.
        """
        self._inicio = None
        self._quantidade = 0

    @property
    def inicio(self):
        """
        Retorna o início da lista encadeada.
        """
        return self._inicio
    
    @property
    def quantidade(self):
        """
        Retorna a quantidade de elementos na lista encadeada.
        """
        return self._quantidade
    
    def inserir_no_inicio(self, conteudo):
        """
        Insere um novo elemento no início da lista encadeada.

        Args:
            conteudo: O conteúdo do novo elemento a ser inserido.
        """
        celula = Celula(conteudo)
        celula.proximo = self._inicio
        self._inicio = celula
        self._quantidade += 1
    
    def inserir(self, posicao, conteudo):
        """
        Insere um novo elemento na posição especificada da lista encadeada.

        Args:
            posicao: A posição na lista onde o elemento será inserido.
            conteudo: O conteúdo do novo elemento a ser inserido.
        """
        if posicao == 0:
            self.inserir_no_inicio(conteudo)
            return
        celula = Celula(conteudo)
        esquerda = self._celula(posicao-1)
        celula.proximo = esquerda.proximo
        esquerda.proximo = celula
        self._quantidade += 1

    def _celula(self, posicao):
        """
        Retorna a célula na posição especificada.

        Args:
            posicao: A posição da célula na lista encadeada.
        
        Returns:
            A célula na posição especificada.
        """
        self._validar_posicao(posicao)
        atual = self.inicio
        for i in range(0, posicao):
            atual = atual.proximo
        return atual
    
    def _validar_posicao(self, posicao):
        """
        Valida se a posição está dentro dos limites da lista encadeada.

        Args:
            posicao: A posição a ser validada.
        
        Raises:
            IndexError: Se a posição estiver fora dos limites da lista encadeada.
        """
        if 0 <= posicao < self.quantidade:
            return True
        raise IndexError("Posição inválida {}".format(posicao))

    def imprimir(self):
        """
        Imprime o conteúdo de cada elemento na lista encadeada.
        """
        atual = self.inicio
        for i in range(0, self.quantidade):
            print(atual.conteudo)
            atual = atual.proximo
    
    def remover_do_inicio(self):
        """
        Remove o primeiro elemento da lista encadeada.

        Returns:
            O conteúdo do elemento removido.
        """
        removido = self.inicio
        self._inicio = removido.proximo
        removido.proximo = None
        self._quantidade -= 1
        return removido.conteudo

    def remover(self, posicao):
        """
        Remove o elemento na posição especificada da lista encadeada.

        Args:
            posicao: A posição do elemento a ser removido.
        
        Returns:
            O conteúdo do elemento removido.
        """
        if posicao == 0:
            return self.remover_do_inicio()
        esquerda = self._celula(posicao - 1)
        removido = esquerda.proximo
        esquerda.proximo = removido.proximo
        removido.proximo = None
        self._quantidade -= 1
        return removido.conteudo
    
    def item(self, posicao):
        """
        Retorna o conteúdo do elemento na posição especificada.

        Args:
            posicao: A posição do elemento a ser retornado.
        
        Returns:
            O conteúdo do elemento na posição especificada.
        """
        self._validar_posicao(posicao)
        celula = self._celula(posicao)
        return celula.conteudo
