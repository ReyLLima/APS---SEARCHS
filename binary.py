class BuscaBinaria:
       def busca_binaria(self, id_imagem):
        # A lista deve estar ordenada
        sorted_ids = sorted(self.ids)  # Ordena a lista de IDs
        left, right = 0, len(sorted_ids) - 1

        while left <= right:
            mid = (left + right) // 2
            if sorted_ids[mid] == id_imagem:
                return sorted_ids[mid]  # Retorna o ID encontrado
            elif sorted_ids[mid] < id_imagem:
                left = mid + 1
            else:
                right = mid - 1
        return None  # Retorna None se não encontrar
