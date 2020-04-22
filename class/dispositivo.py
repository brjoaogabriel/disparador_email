import os;
import platform;
from log_paste.log_funções import *;

class Dispositivo:

    def __init__(self):
        self.__nomemaquina = platform.uname().node;
        self.__sistemaoperacional = platform.uname().system;
        self.__loginmaquina = os.environ['Username'];

    @property
    def getNomeMaquina(self):
        return self.__nomemaquina;

    @property
    def getSistemaOperacional(self):
        return self.__sistemaoperacional;

    @property
    def getLoginMaquina(self):
        return self.__loginmaquina;