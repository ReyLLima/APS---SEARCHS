class ArvoreBinaria:
    def __init__(self):
        self.lista_ids = self.carregar_ids_do_bd()  # Carrega os IDs diretamente do banco de dados
        self.raiz = None
        self.construir_arvore_balanceada(self.lista_ids)

    class No:
        def __init__(self, chave):
            self.chave = chave
            self.esquerda = None
            self.direita = None

    def carregar_ids_do_bd(self):
        # Função para carregar os IDs das imagens existentes no banco de dados
        import mysql.connector
        try:
            conexao = mysql.connector.connect(
                host="localhost",
                user="root",
                password="admin",
                database="aps"
            )
            cursor = conexao.cursor()
            query = "SELECT id FROM tabela_imagens"
            cursor.execute(query)
            resultado = cursor.fetchall()
            return [row[0] for row in resultado]  # Retorna uma lista de IDs
        except mysql.connector.Error as err:
            print(f"Erro ao carregar IDs do banco de dados: {err}")
            return []
        finally:
            if conexao.is_connected():
                cursor.close()
                conexao.close()

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

    def construir_arvore_balanceada(self, lista_ids):
        if not lista_ids:
            return None
        meio = len(lista_ids) // 2
        self.inserir(lista_ids[meio])
        self.construir_arvore_balanceada(lista_ids[:meio])  # Insere à esquerda
        self.construir_arvore_balanceada(lista_ids[meio+1:])  # Insere à direita

    def buscar(self, id_imagem):
        # Verificar se a entrada é um número e convertê-la
        try:
            id_imagem = int(id_imagem)  # Converte a entrada do usuário para inteiro
        except ValueError:
            raise ValueError("O ID da imagem deve ser um número inteiro válido.")

        print(f"Buscando imagem com ID (Árvore Binária): {id_imagem}")
        return self._buscar_recursivo(self.raiz, id_imagem)

    def _buscar_recursivo(self, no, chave):
        if no is None:
            return None

        if chave == no.chave:
            print(f"ID {chave} encontrado na árvore binária. Buscando no banco de dados...")
            return self.buscar_imagem_no_bd(chave)  # Busca a imagem no banco de dados
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
            if resultado:
                print(f"Imagem com ID {id_imagem} encontrada no banco de dados.")
                return resultado[0]  # Retorna a imagem como BLOB
            else:
                print(f"Imagem com ID {id_imagem} não encontrada no banco de dados.")
                return None
        except mysql.connector.Error as err:
            print(f"Erro de conexão ao banco de dados: {err}")
            return None
        finally:
            if conexao.is_connected():
                cursor.close()
                conexao.close()
