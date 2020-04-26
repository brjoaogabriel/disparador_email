from classes.comandosql import *;
from log_paste.log_funções import PrintarLogFunção;

EndereçoFunção = "disparador_email.application.requisicao_filtros.py"
InformacaoFiltros = """
1. Nome exato           (Nome igual ao nome informado)
2. Sobrenome exato      (Sobrenome igual ao sobrenome informado)
3. Email exato          (Email igual ao email informado)
4. Data de nascimento   (Data de nascimento igual a data de nascimento informada)
"""

def Requisita_Filtros(Filtros_Disponiveis):
    Continua:        bool=False;
    Confirmacao:     str;
    Entrada:         int;
    Filtros = [];

    print(InformacaoFiltros);
    while Continua != True:

        try:
            Entrada = int(input(f"Por favor, insira o filtro (entre {min(Filtros_Disponiveis) + 1} e {max(Filtros_Disponiveis) + 1}): "));
            if Entrada not in Filtros:
                if Entrada - 1 in Filtros_Disponiveis:
                    Filtros.append(Entrada - 1);
                    print(f"Filtro {Entrada} adicionado com sucesso.");

                else:
                    print(f"Esse filtro não se encontra disponível! Por favor, selecione entre {min(Filtros_Disponiveis) + 1} e {max(Filtros_Disponiveis) + 1}");

            else:
                print(f"Você já inseriu esse filtro... Filtros solicitados: {Filtros}");

            Confirmacao = str(input("Digite 'OK' caso queira continuar ou '+' caso queira inserir mais filtros"));
            if Confirmacao == "+":
                Continua = False;

            elif Confirmacao == "OK":
                Continua = True;

            else:
                print("ERRO NA ENTRADA DOS DADOS.");

        except:
            print("Erro na solicitação do filtro... por favor, insera um número.");

        print();

    Continua = None;
    Confirmacao = None;
    Entrada = None;

    PrintarLogFunção(True, EndereçoFunção, "Função Requisita_Filtros");
    print(Filtros);
    return Filtros;

def Trata_Filtros():
    SQL_info = ComandoSQL();
    Filtros_Disponiveis = range(0, len(SQL_info.getComandoSQL));
    SelecaoSQL: str = f"SELECT * FROM {SQL_info.getTabela}";

    FiltrosRequisitados = Requisita_Filtros(Filtros_Disponiveis);

    Entrada:    str = "";

    for Filtro in FiltrosRequisitados:
        while Entrada == "":
            Entrada = str(input(f"Por favor, insira o valor do filtro {Filtro + 1}!"));

            if Entrada == "" or len(Entrada) == 0:
                print(f"O valor '{Entrada}' é inválido para a operação");
            else:
                if "WHERE" in SelecaoSQL:
                    SelecaoSQL += " AND";
                else:
                    SelecaoSQL += " WHERE";

                SelecaoSQL += SQL_info.GeraSQL(Entrada, Filtro);

        Entrada = "";

    PrintarLogFunção(True, EndereçoFunção, "Função Trata_Filtros");
    SQL_info = None;
    return SelecaoSQL;