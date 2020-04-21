from log.log_funções import PrintarLogFunção;

#Para cada nome que estiver dentro de sobrenomes, abrevia.
#Exemplo: "João Gabriel Maciel" se torna "João Gabriel M."

Caminho = "disparador_email.functions.abrevia_sobrenomes.py";

def AbreviarSobrenomes(NomeCompleto, Sobrenomes):
    try:
        Nome:   str;
        for Nome in NomeCompleto:
            if Nome in Sobrenomes and len(Nome) >= 3:
                Nome = upper(Nome[:1]) + ".";

        for Palavra in Nome:
            Nomes += Palavra;

        Palavra = None;
        Nome = None;

        PrintarLogFunção(True, Caminho, "Função AbreviarSobrenomes");
        return Nomes;

    except:
        PrintarLogFunção(False, Caminho, "Função AbreviarSobrenomes");
        return f"ERRO - {Caminho}";