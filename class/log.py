from log.log_funções import PrintarLogFunção;

class Log(Dispositivo, Ambiente):

    def __init__(self):
        Dispositivo.__init__();
        Ambiente.__init__();
        self.__EndereçoClasse = "disparador_email.class.log.py";

    def RegistraLogTXT(self):
        try:
            with open("C:\Users\João\Documents\Projetos\disparador_email\log\logs_reg", 'a') as log_file:
                log_file.write(f"{Dispositivo.getSistemaOperacional},"
                               f"{Dispositivo.getLoginMaquina},"
                               f"{Dispositivo.getNomeMaquina},"
                               f"{Ambiente.getHorario},"
                               f"{Ambiente.getData}");
            PrintarLogFunção(True, self.__EndereçoClasse, "Método RegistraLogTXT");
            return True;

        except:
            PrintarLogFunção(False, self.__EndereçoClasse, "Método RegistraLogTXT");
            return False;