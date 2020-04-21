import datetime

def PrintarLogFunção(status, caminho, descricao):
    print(f"{datetime.datetime.now().time()} - {status}... {caminho} - {descricao}");