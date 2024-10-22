class BuscaBinaria:
    def __init__(self, dados):
        """
        Inicializa a classe com uma lista ordenada de dados.
        :param dados: lista de números ordenados
        """
        self.dados = sorted(dados)  # Certifica-se de que os dados estão ordenados

    def buscar(self, X):
        """
        Executa a busca binária para encontrar o valor X.
        :param X: valor a ser procurado
        :return: índice do valor encontrado ou -1 se não encontrado
        """
        inicio = 0
        fim = len(self.dados) - 1

        while inicio <= fim:
            meio = (inicio + fim) // 2  # Calcula o meio da lista

            if self.dados[meio] == X:
                return meio  # Retorna o índice se X for encontrado
            elif self.dados[meio] < X:
                inicio = meio + 1  # Busca na metade direita
            else:
                fim = meio - 1  # Busca na metade esquerda

        return -1  # Retorna -1 se X não for encontrado

# Exemplo de uso:
dados = [1, 3, 5, 7, 9, 11, 13, 15]
busca = BuscaBinaria(dados)
resultado = busca.buscar(7)  # Deve retornar o índice 3, já que 7 está na posição 3
print(f"Resultado da busca: {resultado}")