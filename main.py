import io
from PIL import Image, ImageTk
import mysql.connector
import tkinter as tk
import time

# Importando as classes de busca dos arquivos apropriados
from binary import BuscaBinaria  # Ajuste o caminho conforme necessário
from linear import BuscaLinear    # Ajuste o caminho conforme necessário
from btree import ArvoreBinaria   # Ajuste o caminho conforme necessário

class JanelaPrincipal:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("APS")
        self.window.attributes('-fullscreen', True)
        self.window.configure(bg="lightblue")

        self.label = tk.Label(self.window, text="Digite a ID da imagem a ser buscada abaixo:", font=("Arial", 24), bg="lightblue")
        self.label.pack(pady=40)

        # Entrada de ID
        self.entry = tk.Entry(self.window, font=("Arial", 20))
        self.entry.insert(0, "")  # Texto padrão
        self.entry.pack(pady=10)

        # Frame para alinhar os botões
        botao_frame = tk.Frame(self.window, bg="lightblue")
        botao_frame.pack(pady=20)

        self.botao_tela1 = tk.Button(botao_frame, text="Busca binária", font=("Arial", 14), command=self.abrir_tela_1)
        self.botao_tela1.grid(row=0, column=0, padx=10)

        self.botao_tela2 = tk.Button(botao_frame, text="Busca linear", font=("Arial", 14), command=self.abrir_tela_2)
        self.botao_tela2.grid(row=0, column=1, padx=10)

        self.botao_tela3 = tk.Button(botao_frame, text="Busca por árvore", font=("Arial", 14), command=self.abrir_tela_3)
        self.botao_tela3.grid(row=0, column=2, padx=10)

    def buscar_imagem(self, busca_func):
        # Função para buscar a imagem no banco de dados
        id_imagem = self.entry.get()
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

    def abrir_tela(self, busca_class):
        njanela = tk.Toplevel(self.window)
        njanela.title("Resultado da Busca")
        njanela.geometry("800x600")
        njanela.configure(bg="lightgrey")

        # Tempo inicial da busca
        start_time = time.time()

        # Criar a instância da classe de busca
        busca = busca_class()

        # Executar a busca
        imagem_blob = busca.buscar(self.entry.get())  # Aqui você deve garantir que a função 'buscar' exista na sua classe

        # Tempo final da busca
        end_time = time.time()
        tempo_total = end_time - start_time

        # Exibir o tempo da busca
        tempo_label = tk.Label(njanela, text=f"Tempo da busca: {tempo_total:.4f} segundos", font=("Arial", 14), bg="lightgrey")
        tempo_label.pack(pady=10)

        # Exibir a imagem
        if imagem_blob:
            # Criar um objeto BytesIO a partir do BLOB
            imagem_bytes = io.BytesIO(imagem_blob)
            image = Image.open(imagem_bytes)  # Abrir a imagem a partir do objeto BytesIO
            image = image.resize((400, 400))  # Redimensionar conforme necessário
            photo = ImageTk.PhotoImage(image)

            img_label = tk.Label(njanela, image=photo)
            img_label.image = photo  # Manter referência para evitar garbage collection
            img_label.pack(pady=10)
        else:
            tk.Label(njanela, text="Imagem não encontrada.", font=("Arial", 14), bg="lightgrey").pack(pady=10)

    def abrir_tela_1(self):
        self.abrir_tela(BuscaBinaria)  # Chama a classe de busca binária

    def abrir_tela_2(self):
        self.abrir_tela(BuscaLinear)  # Chama a classe de busca linear

    def abrir_tela_3(self):
        self.abrir_tela(ArvoreBinaria)  # Chama a classe de busca por árvore

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    janela_principal = JanelaPrincipal()
    janela_principal.run()
