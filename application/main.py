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

DatabaseObject = Database();
DatabaseObject.BuscaRegistro(Trata_Filtros());
Dados = DatabaseObject.getCursor.fetchall();
DatabaseObject = None;

print(Dados[0]['email']);
