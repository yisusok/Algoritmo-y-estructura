def hash_tipo(tipo):
    return tipo

def hash_numero(numero):
    return int(str(numero)[-1])

def hash_nivel(nivel):
    return nivel // 10

tabla_tipos = {}
tabla_numeros = {}
tabla_niveles = {}

def insertar_en_tabla(tabla, clave, pokemon):
    if clave not in tabla:
        tabla[clave] = []
    tabla[clave].append(pokemon)

def cargar_pokemon(numero, nombre, tipos, nivel):
    pokemon = {'numero': numero, 'nombre': nombre, 'tipos': tipos, 'nivel': nivel}
    
    for tipo in tipos:
        insertar_en_tabla(tabla_tipos, hash_tipo(tipo), pokemon)
    
    insertar_en_tabla(tabla_numeros, hash_numero(numero), pokemon)
    
    insertar_en_tabla(tabla_niveles, hash_nivel(nivel), pokemon)

def mostrar_por_numero():
    numeros_interes = [3, 7, 9]
    resultado = []
    for numero in numeros_interes:
        if numero in tabla_numeros:
            resultado.extend(tabla_numeros[numero])
    return resultado

def mostrar_por_nivel():
    niveles_interes = [2, 5, 10]
    resultado = []
    for key in tabla_niveles:
        for nivel in niveles_interes:
            if key % nivel == 0:
                resultado.extend(tabla_niveles[key])
    return resultado

def mostrar_por_tipo():
    tipos_interes = ['Acero', 'Fuego', 'Eléctrico', 'Hielo']
    resultado = []
    for tipo in tipos_interes:
        if tipo in tabla_tipos:
            resultado.extend(tabla_tipos[tipo])
    return resultado


cargar_pokemon(123, 'Charmander', ['Fuego'], 12)
cargar_pokemon(456, 'Pikachu', ['Eléctrico'], 15)
cargar_pokemon(789, 'Articuno', ['Hielo', 'Volador'], 20)
cargar_pokemon(370, 'Magnemite', ['Eléctrico', 'Acero'], 30)

print("Pokémons cuyos números terminan en 3, 7 y 9:")
print(mostrar_por_numero())
print("\nPokémons cuyos niveles son múltiplos de 2, 5 y 10:")
print(mostrar_por_nivel())
print("\nPokémons de tipos Acero, Fuego, Eléctrico, Hielo:")
print(mostrar_por_tipo())