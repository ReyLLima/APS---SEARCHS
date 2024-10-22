class BuscaBinaria:
    def __init__(self, ids):
        self.ids = ids  # Lista de IDs a ser usada na busca

    def buscar(self, id_imagem):
        print(f"Buscando imagem com ID (Busca Binária): {id_imagem}")
        # Realiza a busca binária
        esquerda = 0
        direita = len(self.ids) - 1

        while esquerda <= direita:
            meio = (esquerda + direita) // 2
            if self.ids[meio] == id_imagem:
                return self.buscar_imagem_no_bd(id_imagem)  # Retorna a imagem do banco de dados
            elif self.ids[meio] < id_imagem:
                esquerda = meio + 1
            else:
                direita = meio - 1

        return None  # Retorna None se não encontrar

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
