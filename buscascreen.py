import tkinter as tk

class AbrirJanela:
    def __init__(self, window):
        self.window = window

    def abrir_nova_janela(self):
        # Criando a nova janela
        nova_janela = tk.Toplevel(self.window)
        nova_janela.title("Nova Janela")
        nova_janela.geometry("300x200")
        nova_janela.configure(bg="lightgreen")

        # Adicionando um rótulo na nova janela
        label = tk.Label(nova_janela, text="Bem-vindo à nova janela!", font=("Arial", 14), bg="lightgreen")
        label.pack(pady=20)

        # Adicionando um botão de fechar
        fechar_button = tk.Button(nova_janela, text="Fechar", command=nova_janela.destroy)
        fechar_button.pack(pady=10)

        