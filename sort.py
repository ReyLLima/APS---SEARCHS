import mysql.connector
import random
import time

class OrdenacaoSelecao:
    def __init__(self):
        self.ids = self.buscar_ids_do_banco()

    def buscar_ids_do_banco(self):
        # Função que busca os IDs do banco de dados
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
            ids = [item[0] for item in resultado]
            return ids
        except mysql.connector.Error as err:
            print(f"Erro ao conectar ao banco de dados: {err}")
            return []
        finally:
            if conexao.is_connected():
                cursor.close()
                conexao.close()

    def embaralhar_lista(self):
        # Função que embaralha a lista de IDs
        random.shuffle(self.ids)
        print("Lista embaralhada:", self.ids)

    def ordenar_selecao(self):
        # Função de ordenação por seleção
        for i in range(len(self.ids)):
            min_idx = i
            for j in range(i + 1, len(self.ids)):
                if self.ids[j] < self.ids[min_idx]:
                    min_idx = j
            # Troca o valor mínimo encontrado com o valor na posição i
            self.ids[i], self.ids[min_idx] = self.ids[min_idx], self.ids[i]

    def executar(self):
        # Função principal que controla a execução
        self.embaralhar_lista()

        # Medir o tempo de ordenação
        inicio = time.time()
        self.ordenar_selecao()
        fim = time.time()
        tempo_total = fim - inicio

        return tempo_total, self.ids  # Retornar o tempo e os IDs ordenados
