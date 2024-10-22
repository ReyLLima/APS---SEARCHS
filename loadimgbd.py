import mysql.connector
import os

# Função para ler a imagem em binário
def ler_imagem(filepath):
    with open(filepath, 'rb') as arquivo:
        imagem_binaria = arquivo.read()
    return imagem_binaria

# Função para inserir a imagem no banco de dados 5000 vezes
def inserir_imagens_banco(filepath):
    try:
        # Conectar ao banco de dados
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="admin",
            database="aps"
        )
        cursor = conexao.cursor()

        # Ler a imagem como binário
        imagem_binaria = ler_imagem(filepath)

        # Preparar a query de inserção
        query = "INSERT INTO tabela_imagens (imagem_blob) VALUES (%s)"
        
        # Inserir a imagem 5000 vezes
        for i in range(5000):
            cursor.execute(query, (imagem_binaria,))
            conexao.commit()  # Confirma a inserção no banco de dados
            print(f"Imagem {i + 1} inserida com sucesso!")

    except mysql.connector.Error as err:
        print(f"Erro ao conectar ao banco de dados: {err}")
    finally:
        if conexao.is_connected():
            cursor.close()
            conexao.close()

if __name__ == "__main__":
    caminho_imagem = "C:\\Users\\RLima\\OneDrive\\Documentos\\cerrado.jpeg"

    # Verifica se o arquivo existe
    if os.path.exists(caminho_imagem):
        inserir_imagens_banco(caminho_imagem)
    else:
        print("O arquivo de imagem não foi encontrado.")
