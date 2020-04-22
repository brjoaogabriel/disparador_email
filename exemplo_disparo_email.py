import smtplib;

from email.mime.multipart import MIMEMultipart;
from email.mime.text import MIMEText;
from email.mime.base import MIMEBase;
from email import encoders;

#Instanciando a classe MIME que é responsável por elaborar a requisição do disparo do email
OutlookApp = MIMEMultipart()

#Informando quem é a origem do e-mail
OutlookApp['From'] = "contato_joaogabriel@outlook.com"

#Informando quem é o destinatário do e-mail
OutlookApp['To'] = "contato_joaogabriel@outlook.com"

#Informando qual é o assunto do e-mail
OutlookApp['Subject'] = "Titulo do e-mail"

#Construindo o corpo do e-mail
CorpoEmail = """
<!DOCTYPE html>
<html lang="pt-br">
    <head>
        <h1>
            Fernanda cabeçuda
        </h1>
    </head>
    
    <body>
        <font color=red>
            texto vermelho
        </font>    
    </body>
</html>
"""

#Instanciando o corpo do e-mail em formato HTML
OutlookApp.attach(MIMEText(CorpoEmail, 'html'));

#Incluindo anexo
#NomeArquivo = 'teste.pdf'                                                       #Nome no arquivo a adicionar
#Anexo = open(NomeArquivo,'rb')                                                  #Abrindo arquivo

#Realizando conversão para o tipo 64
#part = MIMEBase('application', 'octet-stream')
#part.set_payload((Anexo).read())
#encoders.encode_base64(part)
#part.add_header("Content-Disposition", F"attachment; filename= {NomeArquivo}")
#OutlookApp.attach(part)

#Fechando o arquivo
#Anexo.close()

#Declarando variáveis da biblioteca SMTP
server = smtplib.SMTP('smtp.outlook.com', 587)          #informando servidor e porta SMTP
server.starttls()                                       #Informando tipo de validação
server.login("contato_joaogabriel@outlook.com",
             "123qwe321ewq!@#QWE#@!EWQ")                #Passando Login e Senha
Texto = OutlookApp.as_string()                          #Informando mensagem do e-mail
server.sendmail("contato_joaogabriel@outlook.com",
                "contato_joaogabriel@outlook.com",
                Texto)                                  #Enviando o email
server.quit()                                           #Fechando conexão com o servidor