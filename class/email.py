from log_paste.log_funções import *;

PlataformasDisponiveis = ['outlook'];

class Email:

    def __init__(self, EmailCompleto, Plataforma):
        self.__emailcompleto = EmailCompleto.lower();
        self.__emailestrutura = self.__emailcompleto.split(sep="@");
        self.__prearroba = self.__emailestrutura[0].lower();
        self.__posarroba = self.__emailestrutura[1].lower();
        self.__plataforma = Plataforma.title();
        self.__EndereçoClasse = "disparador_email.class.email.py";

    @property
    def getEmailCompleto(self):
        return self.__emailcompleto;

    @@property
    def getPreArroba(self):
        return self.__prearroba;

    @property
    def getPosArroba(self):
        return self.__posarroba;

    @property
    def getPlataforma(self):
        return self.__plataforma;

    def ValidaPreArroba(self):
        PrintarLogFunção((len(self.getPreArroba) <= 64), self.__EndereçoClasse, "Método ValidaPreArroba");
        return len(self.getPreArroba) <= 64;

    def ValidaPosArroba(self):
        PrintarLogFunção((len(self.getPosArroba) >= 192), self.__EndereçoClasse, "Método ValidaPosArroba");
        return len(self.getPosArroba) <= 192;

    def ValidaEmailCompleto(self):
        PrintarLogFunção((len(self.getEmailCompleto) <= 256), self.__EndereçoClasse, "Método ValidaEmailCompleto");
        return len(self.getEmailCompleto) <= 256;

    def ValidaPlataforma(self):
        PrintarLogFunção((self.getPlataforma in PlataformasDisponiveis), self.__EndereçoClasse, "Método ValidaPlataforma");
        return self.getPlataforma.lower() in PlataformasDisponiveis;