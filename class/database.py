from log_paste.log_funções import PrintarLogFunção;
import pymysql.cursors;

class Database:

    def __init__(self):
        self.__porta = 3306;
        self.__host = 'localhost';
        self.__user = 'root';
        self.__password = '';
        self.__database = 'info_pessoas';
        self.__cursorclass = pymysql.cursors.DictCursor;
        self.__charset = 'utf8mb4';
        self.__conexao = None;
        self.__cursor = None;

    @property
    def getPorta(self):
        return self.__porta;

    @property
    def getHost(self):
        return self.__host;
    @property
    def getUser(self):
        return self.__user;

    @property
    def getPassword(self):
        return self.__password;

    @property
    def getDatabase(self):
        return self.__database;

    @property
    def getCursorClass(self):
        return self.__cursorclass;

    @property
    def getCharset(self):
        return self.__charset;

    @property
    def getConexao(self):
        return self.__conexao;

    @property
    def getCursor(self):
        return self.__cursor;

    @getConexao.setter
    def setConexao(self, Conexao):
        self.__conexao = Conexao;

    @getCursor.setter
    def setCursor(self, Cursor):
        self.__cursor = Cursor;

    def ConectarBase(self):
        self.setConexao = pymysql.connect(
            port=self.getPorta,
            host=self.getHost,
            user=self.getUser,
            password=self.getPassword,
            db=self.getDatabase,
            charset=self.getCharset,
            cursorclass=self.getCursorClass
        );

    def DesconectarBase(self):
        self.setConexao.close();
        self.setConexao = None;

    def ConectarCursor(self):
        self.setCursor = self.getConexao.cursor;

    def DesconectarCursor(self):
        self.setCursor.close();

    def BuscaRegistro(self):
        self.ConectarBase();
        self.ConectarCursor();

        self.DesconectarCursor();
        self.DesconectarBase()