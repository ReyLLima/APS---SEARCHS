class BuscaLinear:
    def buscar(self, id_imagem):
        print(f"Buscando imagem com ID (Busca Linear): {id_imagem}")
        # Realiza a busca linear
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
