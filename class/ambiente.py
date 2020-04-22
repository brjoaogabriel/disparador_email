import datetime as date;
from log_paste.log_funções import PrintarLogFunção;

class Ambiente:

    def __init__(self):
        self.__data = date.datetime.now().date();
        self.__horario = date.datetime.now().time();

    @property
    def getData(self):
        return self.__data;

    @property
    def getHorario(self):
        return self.__horario;