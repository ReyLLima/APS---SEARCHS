import tkinter as tk
from PIL import Image, ImageTk
import time
import mysql.connector  # Supondo que seu banco seja MySQL

class JanelaPrincipal:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("APS")
        self.window.attributes('-fullscreen', True)
        self.window.configure(bg="lightblue")

        self.label = tk.Label(self.window, text="Bem-vindo ao Testador de Buscas!", font=("Arial", 24), bg="lightblue")
        self.label.pack(pady=40)

        # Entrada de ID
        self.entry = tk.Entry(self.window, font=("Arial", 20))
        self.entry.insert(0, "Entre com a ID:")  # Texto padrão
        self.entry.pack(pady=10)

        # Frame para alinhar os botões
        botao_frame = tk.Frame(self.window, bg="lightblue")
        botao_frame.pack(pady=20)

        self.botao_tela1 = tk.Button(botao_frame, text="Abrir Tela 1", font=("Arial", 14), command=self.abrir_tela_1)
        self.botao_tela1.grid(row=0, column=0, padx=10)

        self.botao_tela2 = tk.Button(botao_frame, text="Abrir Tela 2", font=("Arial", 14), command=self.abrir_tela_2)
        self.botao_tela2.grid(row=0, column=1, padx=10)

        self.botao_tela3 = tk.Button(botao_frame, text="Abrir Tela 3", font=("Arial", 14), command=self.abrir_tela_3)
        self.botao_tela3.grid(row=0, column=2, padx=10)

    def buscar_imagem_no_bd(self, id_imagem):
        # Exemplo de função de conexão com o banco de dados e busca
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
                return resultado[0]  # Retorna o blob da imagem
            else:
                print("Imagem não encontrada.")
                return None
        except mysql.connector.Error as err:
            print(f"Erro: {err}")
        finally:
            if conexao.is_connected():
                cursor.close()
                conexao.close()

    def abrir_tela(self, busca_func):
        njanela = tk.Toplevel(self.window)
        njanela.title("Resultado da Busca")
        njanela.geometry("800x600")
        njanela.configure(bg="lightgrey")

        # Obter a ID da entrada
        id_imagem = self.entry.get()

        # Tempo inicial da busca
        start_time = time.time()

        # Executar a função de busca
        imagem_blob = busca_func(id_imagem)

        # Tempo final da busca
        end_time = time.time()
        tempo_total = end_time - start_time

        # Exibir o tempo da busca
        tempo_label = tk.Label(njanela, text=f"Tempo da busca: {tempo_total:.4f} segundos", font=("Arial", 14), bg="lightgrey")
        tempo_label.pack(pady=10)

        # Exibir a imagem
        if imagem_blob:
            image = Image.open(imagem_blob)
            image = image.resize((300, 300))  # Redimensionar conforme necessário
            photo = ImageTk.PhotoImage(image)

            img_label = tk.Label(njanela, image=photo)
            img_label.image = photo  # Manter referência para evitar garbage collection
            img_label.pack(pady=10)
        else:
            tk.Label(njanela, text="Imagem não encontrada.", font=("Arial", 14), bg="lightgrey").pack(pady=10)

    def abrir_tela_1(self):
        self.abrir_tela(self.buscar_imagem_no_bd)  # Assumindo que é a função de busca binária

    def abrir_tela_2(self):
        self.abrir_tela(self.buscar_imagem_no_bd)  # Assumindo que é a função de busca linear

    def abrir_tela_3(self):
        self.abrir_tela(self.buscar_imagem_no_bd)  # Outra função de busca que você definir

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    janela_principal = JanelaPrincipal()
    janela_principal.run()
