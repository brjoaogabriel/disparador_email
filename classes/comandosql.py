class ComandoSQL:

    def __init__(self):
        self.__tabela = "tab_pessoas";


    def GerarSQL(self, Filtro):
        return self.ComandosSQL[Filtro];