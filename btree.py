class ArvoreBinaria:
    def __init__(self, lista_ids):
        self.raiz = None  # Inicializa a raiz como None
        for id_imagem in lista_ids:
            self.inserir(id_imagem)

    # Classe interna para representar cada nó da árvore
    class No:
        def __init__(self, id_imagem):
            self.id = id_imagem  # ID da imagem
            self.esquerda = None  # Ponteiro para o filho da esquerda
            self.direita = None   # Ponteiro para o filho da direita

    # Método para inserir um ID na árvore
    def inserir(self, id_imagem):
        if self.raiz is None:
            self.raiz = self.No(id_imagem)  # Cria a raiz se não existir
        else:
            self._inserir_recursivo(self.raiz, id_imagem)

    # Método recursivo para inserir um ID
    def _inserir_recursivo(self, no, id_imagem):
        if id_imagem < no.id:
            if no.esquerda is None:
                no.esquerda = self.No(id_imagem)  # Insere à esquerda
            else:
                self._inserir_recursivo(no.esquerda, id_imagem)  # Continua a inserção
        else:
            if no.direita is None:
                no.direita = self.No(id_imagem)  # Insere à direita
            else:
                self._inserir_recursivo(no.direita, id_imagem)  # Continua a inserção

    # Método para buscar um ID na árvore
    def buscar(self, id_imagem):
        return self._buscar_recursivo(self.raiz, id_imagem)

    # Método recursivo para buscar um ID
    def _buscar_recursivo(self, no, id_imagem):
        if no is None:
            return None  # Retorna None se não encontrar
        if no.id == id_imagem:
            return no.id  # Retorna o ID encontrado
        elif id_imagem < no.id:
            return self._buscar_recursivo(no.esquerda, id_imagem)  # Busca à esquerda
        else:
            return self._buscar_recursivo(no.direita, id_imagem)  # Busca à direita
