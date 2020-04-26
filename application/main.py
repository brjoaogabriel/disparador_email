###################################
from classes.ambiente import *
from classes.comandosql import *
from classes.database import *
from classes.dispositivo import *
from classes.email import *
from classes.interessado import *
from classes.log import *
from classes.outlookmail import *
###################################
from log_paste.log_funções import *
from log_paste.logs_reg import *
###################################
from functions.caracteres_proibidos import *
from functions.abrevia_sobrenomes import *
###################################
from application.requisicao_filtros import *
from application.gera_comandos import *
###################################
import disparador_email
###################################

CaminhoMain = "disparador_email.application.main.py";

def Captura_Dados(DatabaseObject):
    Retorna:    bool=False;

    while Retorna != True:
        try:
            PrintarLogFunção(True, CaminhoMain, "Função Captura_Dados");
            return DatabaseObject.getCursor.fetchall();

        except:
            PrintarLogFunção(False, CaminhoMain, "Função Captura_Dados");
            return "ERRO";

def VerificaCerteza():
    Entrada = str(input("Se você tem certeza que deseja continuar, digite SIM "));
    return Entrada == "SIM";

Continua:   bool;

DatabaseObject = Database();
DatabaseObject.BuscaRegistro(Trata_Filtros());

Dados = Captura_Dados(DatabaseObject);

if Dados == "ERRO":
    print("Finalizando execução...");
    exit();

if VerificaCerteza() == False:
    print("Usuário não deseja continuar, sendo assim, estamos encerrando a operação");
    exit();

LoopingDisparo(Dados);


DatabaseObject = None;

print(len(Dados));
