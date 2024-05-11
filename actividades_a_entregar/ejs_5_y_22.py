# 5. Desarrollar una función que permita convertir un número romano en un número decimal.


def romano_a_decimal(romano):
    numero_romano = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    if len(romano) == 0:
        return 0
    elif len(romano) == 1:
        return numero_romano[romano]
    else:
        if numero_romano[romano[0]] < numero_romano[romano[1]]:
            return numero_romano[romano[1]] - numero_romano[romano[0]] + romano_a_decimal(romano[2:])
        else:
            return numero_romano[romano[0]] + romano_a_decimal(romano[1:])


numero_romano = "MXVLCD"
print("Número romano:", numero_romano)
print("Número decimal:", romano_a_decimal(numero_romano))





# 22. El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u
# otro, el que más le guste) está atrapado, pero muy cerca está su mochila que contiene muchos
# objetos. Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con
# ayuda de la fuerza” realizar las siguientes actividades:
# a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no
# queden más objetos en la mochila;

# b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sa-
# car para encontrarlo;

# c. Utilizar un vector para representar la mochila.


def usar_la_fuerza(mochila, posicion=0, objetos_sacados=0):
    
    if posicion >= len(mochila):
        return False, objetos_sacados  
    
    if mochila[posicion] == "sable_de_luz":
        return True, objetos_sacados + 1  
    
    
    return usar_la_fuerza(mochila, posicion + 1, objetos_sacados + 1)


mochila = ["comida", "ropa", "sable_de_luz", "botiquín", "mapa"]
encontrado, objetos_necesarios = usar_la_fuerza(mochila)
if encontrado:
    print("Se encontró el sable de luz sacando", objetos_necesarios, "objetos de la mochila.")
else:
    print("No se encontró ningún sable de luz en la mochila.")
