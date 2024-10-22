import tkinter as tk
from buscascreen import AbrirJanela



class JanelaPrincipal:
    def __init__(self):
        # Criando a janela principal
        self.window = tk.Tk()
        self.window.title("APS")
        self.window.geometry("1920x1080")
        self.window.configure(bg="lightblue")

        # Adicionando um rótulo (label)
        self.label = tk.Label(self.window, text="Bem-vindo ao Testador de Buscas!", font=("Arial", 16), bg="lightblue")
        self.label.pack(pady=20)  # O pack() posiciona o widget na janela

        # Criando uma instância da classe AbrirJanela
        self.abrir_janela = AbrirJanela(self.window)

        # Botão que leva á tela das buscas 
        self.botao_abrir = tk.Button(self.window, text="Abrir Nova Janela", font=("Arial", 12), command=self.abrir_janela.abrir_nova_janela)
        self.botao_abrir.pack(pady=20)

        # Adicionando um segundo botão
        self.button = tk.Button(self.window, text="Clique Aqui", font=("Arial", 12), command=lambda: print("Botão clicado!"))
        self.button.pack(pady=10)

        # Adicionando um segundo campo de entrada de texto
        self.entry = tk.Entry(self.window, font=("Arial", 12))
        self.entry.pack(pady=10)

    def run(self):
        # Mantendo a janela aberta
        self.window.mainloop()

if __name__ == "__main__":
    janela_principal = JanelaPrincipal()
    janela_principal.run()