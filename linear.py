class BuscaLinear:
    def busca_linear(self, id_imagem):
        for i in range(len(self.ids)):
            if self.ids[i] == id_imagem:
                return self.ids[i]  # Retorna o ID encontrado
        return None  # Retorna None se não encontrar
