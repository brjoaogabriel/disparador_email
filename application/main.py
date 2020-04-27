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
from disparador_email import Procedimento_Enviar_Email
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
    Entrada = str(input("\nSe você tem certeza que deseja continuar, digite SIM "));
    PrintarLogFunção(True, CaminhoMain, "Função VerificaCerteza");
    return Entrada == "SIM";

def VerificaEmail(Email):
    Email.append(str(input("\nDigite o seu e-mail duas vezes\n")));
    Email.append(str(input()));

    PrintarLogFunção(True, CaminhoMain, "Função VerificaEmail");
    return not (Email[0] != Email[1]);

def VerificaSenha(Senha):
    Senha.append(str(input("\nDigite o sua senha duas vezes\n")));
    Senha.append(str(input()));

    PrintarLogFunção(True, CaminhoMain, "Função VerificaSenha");
    return not (Senha[0] != Senha[1]);

def Executa_Principal():
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

    EmailInformado = [];
    SenhaInformada = [];

    if VerificaEmail(EmailInformado) != True:
        print("Finalizando execução... emails não conferem");
        exit();

    else:
        print("Verificação de e-mail aprovada");

    if VerificaSenha(SenhaInformada) != True:
        print("Finalizando execução... senhas não conferem");
        exit();

    if VerificaCerteza() == False:
        print("Usuário não deseja continuar, sendo assim, estamos encerrando a operação");
        exit();

    else:
        print("Verificação de senha aprovada");

    print(f"Iniciando o disparo de e-mails...");
    Contador:   int=0;
    for i in range(0, len(Dados), 1):
        EmailInteressado = Email(Dados[i]['email'], 'outlook');
        if EmailInteressado.ValidacaoCompleta() == True:
            InfoInteressado = Interessado(
                Dados[i]['nome'],
                Dados[i]['sobrenome'],
                Dados[i]['nome'] + " " + Dados[i]['sobrenome'],
                EmailInteressado.getEmailCompleto,
                Dados[i]['data_nascimento'],
                Dados[i]['id_pessoa']
            );

            print();
            print(f"Nome:                  {Dados[i]['nome']}");
            print(f"Sobrenome:             {Dados[i]['sobrenome']}");
            print(f"Email:                 {InfoInteressado.getEmail}");
            print(f"Data Nascimento:       {Dados[i]['data_nascimento']}");
            print(f"ID Pessoa:             {Dados[i]['id_pessoa']}");


            strHTML = f"<b>Amo voce</b>";

            EmailOut = OutlookMail(EmailInformado[0], InfoInteressado.getEmail, f"Olá, {InfoInteressado.getNomeCompleto}", strHTML);

            Procedimento_Enviar_Email(EmailOut, SenhaInformada[0]);

            InfoInteressado = None;
            Contador += 1;

        else:
            print(f"Email inválido! {EmailInteressado.getEmailCompleto}");


        print(EmailInteressado.getEmailCompleto);

        EmailInteressado = None;


    DatabaseObject = None;
    print(f"Disparo de email finalizo... \nEmails enviados: {Contador}");
    Contador = None;
    PrintarLogFunção(True, CaminhoMain, "Procedimento main.py");
    return True;

Executa_Principal();