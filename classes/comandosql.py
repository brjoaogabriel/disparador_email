class ComandoSQL:

    def __init__(self):
        self.Parametro = "";
        self.__tabela = "tab_pessoas";
        self.__comandosql = [
            f" nome =",
            f" sobrenome =",
            f" email =",
            f" data_nascimento ="
            ];

    @property
    def getTabela(self):
        return self.__tabela;

    @property
    def getComandoSQL(self):
        return self.__comandosql;

    @getTabela.setter
    def setTabela(self, Tabela):
        self.__tabela = Tabela;

    @getComandoSQL.setter
    def setComandoSQL(self, ComandoSQL):
        self.__comandosql = ComandoSQL;

    def GeraSQL(self, Parametro, Filtro):
        return f"{self.getComandoSQL[Filtro]} '{Parametro}'";