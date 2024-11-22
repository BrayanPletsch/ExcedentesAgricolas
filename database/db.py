class Database:
    def __init__(self):
        # Dados fictícios para teste
        self.ongs = [
            {"name": "Moradia e Cidadania", 
             "description": "ONG que promove moradia digna, inclusão social e combate à desigualdade.", 
             "category": "Habitação"},
             
            {"name": "Banco de Alimentos (ONG)", 
             "description": "A Banco de Alimentos coleta e distribui alimentos para pessoas vulneráveis.", 
             "category": "Segurança Alimentar"},
             
            {"name": "Banco de Alimentos (Governo do DF)", 
             "description": "O Banco de Alimentos do GDF combate o desperdício e promove segurança alimentar.", 
             "category": "Governo"},
             
            {"name": "SESC Mesa Brasil", 
             "description": "Mesa Brasil conecta doadores a instituições que combatem a insegurança alimentar.", 
             "category": "Segurança Alimentar"},
             
            {"name": "IPEAS-Brasil", 
             "description": "O IPEAS-Brasil realiza pesquisas para combater fome, desperdício e promover segurança alimentar.", 
             "category": "Pesquisa"},
             
            {"name": "Cereal Cerebral", 
             "description": "A Cereal Cerebral oferece atendimento nutricional e doações para comunidades carentes.", 
             "category": "Nutrição"},
             
            {"name": "Cidades sem Fome", 
             "description": "A Cidades sem Fome desenvolve projetos de agricultura urbana e segurança alimentar.", 
             "category": "Agricultura Urbana"},
             
            {"name": "Fundação Banco do Brasil (FBB)", 
             "description": "Atuamos na transformação social e sustentável com parcerias e programas sociais.", 
             "category": "Transformação Social"},
             
            {"name": "Cozinha Solidária", 
             "description": "Cozinhas solidárias oferecem refeições e educação alimentar para vulneráveis.", 
             "category": "Alimentação Solidária"},
             
            {"name": "Ação da Cidadania", 
             "description": "Mobiliza a sociedade para combater a fome e promover direitos sociais.", 
             "category": "Direitos Sociais"}
        ]

    def get_ongs(self):
        """
        Retorna todas as ONGs do banco de dados.
        :return: Lista de ONGs
        """
        return self.ongs
