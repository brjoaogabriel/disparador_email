from functions.caracteres_proibidos import *;
from functions.abrevia_sobrenomes import *;
from log.log_funções import *;

class Interessado:

    def __init__(self, Nome, Sobrenome, NomeCompleto, Email, DataNascimento, ID):
        self.__nome = Nome;
        self.__sobrenome = Sobrenome;
        self.__nomecompleto = NomeCompleto;
        self.__email = Email;
        self.__datanascimento = DataNascimento;
        self.__id = ID;
        self.__EndereçoClasse = "disparador_email.class.interessado.py";

    @property
    def getNome(self):
        return self.__nome;

    @property
    def getSobrenome(self):
        return self.__sobrenome;

    @property
    def getNomeCompleto(self):
        return self.__nomecompleto;

    @property
    def getEmail(self):
        return self.__email;

    @property
    def getDataNascimento(self):
        return self.__datanascimento;

    @property
    def getID(self):
        return self.__id;

    @getNome.setter
    def setNome(self, Nome):
        self.__nome = Nome;

    @getSobrenome.setter
    def setSobrenome(self, Sobrenome):
        self.__sobrenome = Sobrenome;

    @getNomeCompleto.setter
    def setNomeCompleto(self, nomecompleto):
        self.__nomecompleto = nomecompleto;

    @getEmail.setter
    def setEmail(self, email):
        self.__email

    def TrataNome(self):
        try:
            self.setNome = TrataLetrasPermitidas(self.getNome);
            self.setNome = self.getNome.title();
            PrintarLogFunção(True, f"{self.__EndereçoClasse}", "Método TrataNome");
            return True;

        except:
            PrintarLogFunção(False, f"{self.__EndereçoClasse}", "Método TrataNome");
            return False;

    def TrataSobrenome(self):
        try:
            self.setSobreome = TrataLetrasPermitidas(self.getSobreome);
            self.setSobreome = self.getSobreome.title();
            PrintarLogFunção(True, f"{self.__EndereçoClasse}", "Método TrataSobrenome");
            return True;

        except:
            PrintarLogFunção(False, f"{self.__EndereçoClasse}", "Método TrataSobrenome");
            return False

    def TrataNomeCompleto(self):
        try:
            self.setNomeCompleto(self.getNomeCompleto.title());
            if len(self.getNomeCompleto) > 60:
                self.setNomeCompleto = AbreviarSobrenomes(self.getNomeCompleto, self.getSobrenome);

            PrintarLogFunção(True, f"{self.__EndereçoClasse}", "Método TrataNomeCompleto");
            return True;

        except:
            PrintarLogFunção(False, f"{self.__EndereçoClasse}", "Método TrataNomeCompleto");
            return False;

    def ValidaDataNascimento(self):
        try:
            return True;

        except:
            return False;