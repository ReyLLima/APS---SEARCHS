class BuscaLinear:
    def __init__(self, dados):
        """
        Inicializa a classe com uma lista de dados.
        :param dados: lista de números
        """
        self.dados = dados

    def buscar(self, X):
        """
        Executa a busca linear para encontrar o valor X.
        :param X: valor a ser procurado
        :return: índice do valor encontrado ou -1 se não encontrado
        """
        for i in range(len(self.dados)):
            if self.dados[i] == X:
                return i  # Retorna o índice se X for encontrado
        return -1  # Retorna -1 se X não for encontrado

# Exemplo de uso:
dados = [10, 23, 45, 70, 11, 15]
busca = BuscaLinear(dados)
resultado = busca.buscar(45)  # Deve retornar o índice 2, já que 45 está na posição 2
print(f"Resultado da busca: {resultado}")
