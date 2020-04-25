def GeraComandosSQL(ListaRequisicos):
    for Item in ListaRequisicos:
        if "WHERE" in SQL:
            SQL += f" AND {Filtros[ListaRequisicos]}";
        else:
            SQL += f" WHERE {Filtros[ListaRequisicos]}"