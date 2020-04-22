from log_paste.log_funções import PrintarLogFunção;
from classes.dispositivo import *;
from classes.ambiente import *;

class Log(Dispositivo, Ambiente):

    def __init__(self):
        Dispositivo.__init__();
        Ambiente.__init__();
        self.__EndereçoClasse = "disparador_email.classes.log.py";

    def RegistraLogTXT(self):
        try:
            with open(f"C:\\Users\\João\\Documents\\Projetos\\disparador_email\\log_paste\\log_{Ambiente.getData.month}_{Ambiente.getData.year}.csv", 'a') as log_file:
                if len(log_file.read()) == 0:
                    log_file.write("sistema_operacional,login_maquina,nome_maquina,horario,data");

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