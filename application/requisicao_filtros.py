"""

Aqui o usuário deve informar quais vão ser os tipos de filtros e de acordo com isso uma
consulta sql será formulada

SQLString = Select * from info_pessoas;

Se não for escolhido nenhum filtro, então a consulta deve ser essa, a cada filtro que o usuário escolha, um filtro
novo deve ser aplicado

Filtros...
id_pessoa:
    IN  (lista)

nome:
    IN (lista)

sobrenome:
    IN (lista)

email:
    IN (lista)

data_nascimento:
    = hoje
    = mes de hoje

"""

def Requisita_Filtros():
    Continua:        bool=False;
    Confirmacao:     str;
    Entrada:         int;
    Filtros = [];

    while Continua != True:
        try:
            Entrada = int(input(f"Por favor, insira o filtro (entre {min(Filtros_Disponiveis)} e {max(Filtros_Disponiveis)}): "));
            if Entrada not in Filtros:
                if Entrada in Filtros_Disponiveis:
                    Filtros.append(Entrada);
                    print(f"Filtro {Entrada} adicionado com sucesso.");

                else:
                    print(f"Esse filtro não se encontra disponível! Por favor, selecione um desses filros: {Filtros_Disponiveis}");

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

    return Filtros;

Filtros_Disponiveis = [1,2,3,4,5,6];
print(Requisita_Filtros());