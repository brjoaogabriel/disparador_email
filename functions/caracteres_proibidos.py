from log.log_funções import PrintarLogFunção;

Permissões = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ç', 'á', 'é', 'í', 'ó', 'ú', 'ã', 'õ', ' '];

#Exclui caracteres proibidos
def TrataLetrasPermitidas(Palavra):
    try:
        for Letra in Palavra:
            if Letra not in Permissões:
                Palavra = Palavra.replace(Letra, "");

        PrintarLogFunção(True, "disparador_email.function.caracteres_proibidos.py - Função TrataLetrasPermitidas");
        return Palavra;

    except:
        PrintarLogFunção(False, "disparador_email.function.caracteres_proibidos.py - Função TrataLetrasPermitidas");
        return "ERRO - disparador_email.function.caracteres_proibidos.py";