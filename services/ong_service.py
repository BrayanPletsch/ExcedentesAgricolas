from database.db import Database

class OngService:
    def __init__(self):
        self.db = Database()

    def search_ongs(self, query):
        """
        Realiza a pesquisa das ONGs com base no termo fornecido.
        :param query: String de busca
        :return: Lista de ONGs correspondentes
        """
        query = query.lower().strip()  # Normaliza o termo de busca
        return [
            ong for ong in self.db.get_ongs()
            if query in ong['name'].lower()  # Compara nomes em letras minúsculas
        ]
