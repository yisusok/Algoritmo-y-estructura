def lista_inversa(lista):
    if not lista:
        return []
    else:
        return [lista[-1]] + lista_inversa(lista[:-1])


mi_lista = [1, 2, 3, 4, 5]
print(lista_inversa(mi_lista))