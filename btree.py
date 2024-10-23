class ArvoreBinaria:
    def __init__(self):
        self.lista_ids = list(range(1, 5001))
        self.raiz = None
        self.construir_arvore()

    class No:
        def __init__(self, chave):
            self.chave = chave
            self.esquerda = None
            self.direita = None

    def inserir(self, chave):
        if not isinstance(chave, int):
            raise ValueError("A chave deve ser um inteiro.")
        if self.raiz is None:
            self.raiz = self.No(chave)
        else:
            self._inserir_recursivo(self.raiz, chave)

    def _inserir_recursivo(self, no, chave):
        if chave < no.chave:
            if no.esquerda is None:
                no.esquerda = self.No(chave)
            else:
                self._inserir_recursivo(no.esquerda, chave)
        elif chave > no.chave:  # Evita duplicatas
            if no.direita is None:
                no.direita = self.No(chave)
            else:
                self._inserir_recursivo(no.direita, chave)
        # Se a chave for igual, não faz nada

    def construir_arvore(self):
        for id_imagem in self.lista_ids:
            self.inserir(id_imagem)

    def buscar(self, id_imagem):
        if not isinstance(id_imagem, int):
            raise ValueError("O ID da imagem deve ser um inteiro.")
        print(f"Buscando imagem com ID (Árvore Binária): {id_imagem}")
        return self._buscar_recursivo(self.raiz, id_imagem)

    def _buscar_recursivo(self, no, chave):
        if no is None:
            return None

        if chave == no.chave:
            return self.buscar_imagem_no_bd(chave)  # Retorna a imagem do banco de dados
        elif chave < no.chave:
            return self._buscar_recursivo(no.esquerda, chave)
        else:
            return self._buscar_recursivo(no.direita, chave)

    def buscar_imagem_no_bd(self, id_imagem):
        import mysql.connector
        try:
            conexao = mysql.connector.connect(
                host="localhost",
                user="root",
                password="admin",
                database="aps"
            )
            cursor = conexao.cursor()
            query = "SELECT imagem_blob FROM tabela_imagens WHERE id = %s"
            cursor.execute(query, (id_imagem,))
            resultado = cursor.fetchone()
            return resultado[0] if resultado else None
        except mysql.connector.Error as err:
            print(f"Erro: {err}")
            return None
        finally:
            if conexao.is_connected():
                cursor.close()
                conexao.close()
