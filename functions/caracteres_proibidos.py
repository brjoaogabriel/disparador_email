from log_paste.log_funções import PrintarLogFunção;

Permissões = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ç', 'á', 'é', 'í', 'ó', 'ú', 'ã', 'õ', ' '];

Caminho = "disparador_email.functions.caracteres_proibidos.py";

#Exclui caracteres proibidos
def TrataLetrasPermitidas(Palavra):
    try:
        for Letra in Palavra:
            if Letra not in Permissões:
                Palavra = Palavra.replace(Letra, "");

        PrintarLogFunção(True, Caminho, "Função TrataLetrasPermitidas");
        return Palavra;

    except:
        PrintarLogFunção(False, Caminho, "Função TrataLetrasPermitidas");
        return f"ERRO - {Caminho}";