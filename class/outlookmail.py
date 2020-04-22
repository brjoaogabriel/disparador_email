from log_paste.log_funções import *;
import smtplib;
from email.mime.multipart import MIMEMultipart;
from email.mime.text import MIMEText;
from email.mime.base import MIMEBase;
from email import encoders;

class OutlookMail:

    def __init__(self, Origem, Destinatario, Assunto, Corpo):
        self.__origem = Origem;
        self.__destinatario = Destinatario;
        self.__assunto = Assunto;
        self.__corpo = Corpo;
        self.__smtpserver = "smtp.outlook.com";
        self.__smtpport = 587;
        self.__EndereçoClasse = "disparador_email.class.outlookmail.py";

    @property
    def getOrigem(self):
        return self.__origem;

    @property
    def getDestinatario(self):
        return self.__destinatario;

    @property
    def getAssunto(self):
        return self.__assunto;

    @property
    def getCorpo(self):
        return self.__corpo;

    @property
    def getSMTPServer(self):
        return self.__smtpserver;

    @property
    def getSMTPPort(self):
        return self.__smtpport;

    @getOrigem.setter
    def setOrigem(self, Origem):
        self.__origem = Origem;

    @getDestinatario.setter
    def setDestinatario(self, Destinatario):
        self.__destinatario;

    @getAssunto.setter
    def setAssunto(self, Assunto):
        self.__assunto = Assunto;

    def EnviarEmail(self, password):
        OutlookApp = MIMEMultipart();

        OutlookApp['From'] = self.getOrigem;
        OutlookApp['To'] = self.getDestinatario;
        OutlookApp['Subject'] = self.getAssunto;
        OutlookApp.attach(MIMETEXT(self.getCorpo, 'html'));

        ServidorConexao = smtplib.SMTP(self.getSMTPServer, self.getSMTPPort);
        ServidorConexao.starttls();
        ServidorConexao.login(self.getOrigem, password);
        Texto = OutlookApp.as_string();
        ServidorConexao.sendmail(self.getOrigem, self.getDestinatario, Texto);
        ServidorConexao.close();

        OutlookApp = None;
        ServidorConexao = None;
        Texto = None;