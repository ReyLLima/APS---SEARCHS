import io
from PIL import Image, ImageTk
import mysql.connector
import tkinter as tk
from tkinter import filedialog, messagebox
import time

# Importando as classes de busca dos arquivos apropriados
from binary import BuscaBinaria  # Ajuste o caminho conforme necessário
from sort import OrdenacaoSelecao    # Ajuste o caminho conforme necessário
from btree import ArvoreBinaria   # Ajuste o caminho conforme necessário

class JanelaPrincipal:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("APS")
        self.window.attributes('-fullscreen', True)
        self.window.configure(bg="lightblue")

        self.label = tk.Label(self.window, text="Digite a ID da imagem a ser buscada abaixo:", font=("Arial", 24), bg="lightblue")
        self.label.pack(pady=40)

        # Entrada de ID para busca
        self.entry_busca = tk.Entry(self.window, font=("Arial", 20))
        self.entry_busca.insert(0, "")  # Texto padrão
        self.entry_busca.pack(pady=10)

        # Botão para carregar nova imagem
        self.botao_carregar = tk.Button(self.window, text="Carregar Nova Imagem", font=("Arial", 14), command=self.carregar_imagem)
        self.botao_carregar.pack(pady=10)

        # Botão para atualizar imagem
        self.botao_update = tk.Button(self.window, text="Atualizar Imagem", font=("Arial", 14), command=self.atualizar_imagem)
        self.botao_update.pack(pady=10)

        # Botão para deletar imagem
        self.botao_deletar = tk.Button(self.window, text="Deletar Imagem", font=("Arial", 14), command=self.deletar_imagem)
        self.botao_deletar.pack(pady=10)

        # Frame para alinhar os botões de busca e ordenação
        botao_frame = tk.Frame(self.window, bg="lightblue")
        botao_frame.pack(pady=20)

        self.botao_tela1 = tk.Button(botao_frame, text="Busca binária", font=("Arial", 14), command=self.abrir_tela_1)
        self.botao_tela1.grid(row=0, column=0, padx=10)

        self.botao_tela2 = tk.Button(botao_frame, text="Ordenação por seleção", font=("Arial", 14), command=self.abrir_tela_2)
        self.botao_tela2.grid(row=0, column=1, padx=10)

        self.botao_tela3 = tk.Button(botao_frame, text="Busca por árvore", font=("Arial", 14), command=self.abrir_tela_3)
        self.botao_tela3.grid(row=0, column=2, padx=10)

    def carregar_imagem(self):
        # Função para carregar uma nova imagem no banco de dados
        caminho_imagem = filedialog.askopenfilename(title="Escolha uma imagem", filetypes=[("Imagens", "*.jpg;*.jpeg;*.png")])
        if not caminho_imagem:
            return
        try:
            with open(caminho_imagem, "rb") as file:
                imagem_blob = file.read()
            conexao = mysql.connector.connect(
                host="localhost",
                user="root",
                password="admin",
                database="aps"
            )
            cursor = conexao.cursor()
            query = "INSERT INTO tabela_imagens (imagem_blob) VALUES (%s)"
            cursor.execute(query, (imagem_blob,))
            conexao.commit()
            messagebox.showinfo("Sucesso", "Imagem carregada com sucesso!")
        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro ao inserir imagem no banco de dados: {err}")
        finally:
            if conexao.is_connected():
                cursor.close()
                conexao.close()

    def atualizar_imagem(self):
        # Função para atualizar a imagem de um ID específico
        id_imagem = self.entry_busca.get()
        caminho_imagem = filedialog.askopenfilename(title="Escolha uma nova imagem", filetypes=[("Imagens", "*.jpg;*.jpeg;*.png")])
        if not caminho_imagem:
            return
        try:
            with open(caminho_imagem, "rb") as file:
                imagem_blob = file.read()
            conexao = mysql.connector.connect(
                host="localhost",
                user="root",
                password="admin",
                database="aps"
            )
            cursor = conexao.cursor()
            query = "UPDATE tabela_imagens SET imagem_blob = %s WHERE id = %s"
            cursor.execute(query, (imagem_blob, id_imagem))
            conexao.commit()
            if cursor.rowcount > 0:
                messagebox.showinfo("Sucesso", f"Imagem do ID {id_imagem} atualizada com sucesso!")
            else:
                messagebox.showwarning("Aviso", f"ID {id_imagem} não encontrado.")
        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro ao atualizar imagem no banco de dados: {err}")
        finally:
            if conexao.is_connected():
                cursor.close()
                conexao.close()

    def deletar_imagem(self):
        # Função para deletar a imagem de um ID específico
        id_imagem = self.entry_busca.get()
        try:
            conexao = mysql.connector.connect(
                host="localhost",
                user="root",
                password="admin",
                database="aps"
            )
            cursor = conexao.cursor()
            query = "DELETE FROM tabela_imagens WHERE id = %s"
            cursor.execute(query, (id_imagem,))
            conexao.commit()
            if cursor.rowcount > 0:
                messagebox.showinfo("Sucesso", f"Imagem do ID {id_imagem} deletada com sucesso!")
            else:
                messagebox.showwarning("Aviso", f"ID {id_imagem} não encontrado.")
        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro ao deletar imagem no banco de dados: {err}")
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
        imagem_blob = busca.buscar(self.entry_busca.get())  # Agora usamos a entrada para busca

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
        njanela = tk.Toplevel(self.window)
        njanela.title("Ordenação por Seleção")
        njanela.geometry("800x600")
        njanela.configure(bg="lightgrey")

        # Criar a instância da classe de ordenação por seleção
        ordenacao = OrdenacaoSelecao()
        
        # Medir o tempo de ordenação e obter IDs ordenados
        tempo_total, ids_ordenados = ordenacao.executar()

        # Exibir o tempo da ordenação
        tempo_label = tk.Label(njanela, text=f"Tempo da ordenação: {tempo_total:.4f} segundos", font=("Arial", 14), bg="lightgrey")
        tempo_label.pack(pady=10)

        # Criar um widget Text para exibir os IDs
        text_widget = tk.Text(njanela, font=("Arial", 8), wrap=tk.WORD, bg="lightgrey")
        text_widget.pack(expand=True, fill='both', padx=10, pady=10)

        # Inserir os IDs ordenados no widget Text
        text_widget.insert(tk.END, "IDs ordenados:\n")
        text_widget.insert(tk.END, ', '.join(map(str, ids_ordenados)))

        # Desabilitar edição no widget Text
        text_widget.config(state=tk.DISABLED)

    def abrir_tela_3(self):
        self.abrir_tela(ArvoreBinaria)  # Chama a classe de busca por árvore

    def run(self):
        self.window.mainloop()

# Executar a interface gráfica
app = JanelaPrincipal()
app.run()
