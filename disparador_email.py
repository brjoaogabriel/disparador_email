from log_paste.log_funções import *;
import smtplib;

from email.mime.multipart import MIMEMultipart;
from email.mime.text import MIMEText;
from email.mime.base import MIMEBase;
from email import encoders;

Caminho = "disparador_email.disparador_email.py";

#Para chamar essa função, passe como parametro um objeto da classe outlookmail e a senha de acesso do email

def Procedimento_Enviar_Email(Classe, Password):
    OutlookApp = MIMEMultipart();

    OutlookApp['From'] = Classe.getOrigem;
    OutlookApp['To'] = Classe.getDestinatario;
    OutlookApp['Subject'] = Classe.getAssunto;
    OutlookApp.attach(MIMEText(Classe.getCorpo, 'html'));

    ServidorConexao = smtplib.SMTP(Classe.getSMTPServer, Classe.getSMTPPort);
    ServidorConexao.starttls();
    ServidorConexao.login(Classe.getOrigem, Password);
    Texto = OutlookApp.as_string();
    ServidorConexao.sendmail(Classe.getOrigem, Classe.getDestinatario, Texto);
    ServidorConexao.close();

    PrintarLogFunção(True, Caminho, "Função Enviar_Email");
    OutlookApp = None;
    ServidorConexao = None;
    Texto = None;