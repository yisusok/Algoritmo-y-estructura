from info_3 import jedis

# 3. Se dispone de una lista de todos los Jedi, de cada uno de estos se conoce su nombre, maestros, colores de sable de luz usados y especie. implementar las funciones
# necesarias para resolver las actividades enumeradas a continuación:
# a) listado ordenado por nombre y por especie;
# b) mostrar toda la información de Ahsoka Tano y Kit Fisto;
# c) mostrar todos los padawan de Yoda y Luke Skywalker, es decir sus aprendices;
# d) mostrar los Jedi de especie humana y twi'lek;
# e) listar todos los Jedi que comienzan con A;
# f) mostrar los Jedi que usaron sable de luz de más de un color;
# g) indicar los Jedi que utilizaron sable de luz amarillo o violeta;
# h) indicar los nombre de los padawans de Qui-Gon Jin y Mace Windu, si los tuvieron.
# i) Mostrar todos los Jedi que tengan el ranking de Grand Master.

Jedis=jedis



def ordenar_jedi_por_nombre_y_especie(jedi_list):
    
    def key_function(jedi):
        return (jedi["name"], jedi["species"])
    
    return sorted(jedi_list, key=key_function)


def encontrar_padawan(master_name, jedi_list):
    padawan_list = []
    for jedi in jedi_list:
        if master_name in jedi.get("maestros", []):
            padawan_list.append(jedi)
    return padawan_list


def encontrar_jedi_por_especie(especies, jedi_list):
    jedi_especie = []
    for jedi in jedi_list:
        if jedi["species"] in especies:
            jedi_especie.append(jedi)
    return jedi_especie
especies_a_buscar = ["Human", "Twi'lek"]







ordenados=ordenar_jedi_por_nombre_y_especie(Jedis)
for jedi in Jedis:
    print(Jedis)
    
    
for jedi in Jedis:
    if jedi["name"]=="Ahsoka Tano" and jedi["name"]=="Kit Fisto":
        print(jedi)
        
        
        
padawan_yoda = encontrar_padawan("Yoda", Jedis)
for jedi in padawan_yoda:
    print(jedi)
    
    
padawan_luke = encontrar_padawan("Luke Skywalker", Jedis)
for jedi in padawan_yoda:
    print(jedi)


jedi_especie_mostrar = encontrar_jedi_por_especie(especies_a_buscar, Jedis)
for jedi in jedi_especie_mostrar:
    print(jedi)


jedi_con_a=[]
for jedi in Jedis:
        if jedi["name"].startswith("A"):
            jedi_con_a.append(jedi)
            

for jedi in Jedis:
    lightsaber_color = jedi.get("lightsaber_color") 
    if lightsaber_color is not None and "/" in lightsaber_color:
        print(jedi)
            


for jedi in Jedis:
        if jedi["lightsaber_color"]=="purple" and jedi["lightsaber_color"]=="yellow":
            print(jedi)
            
            


for jedi in Jedis:
    if jedi["master"]=="Qui-Gon Jin" and jedi["master"]==" Mace Windu":
        (jedi["name"])
        
        
for jedi in Jedis:
        if jedi["rank"] == "Grand Master":
            print(jedi)
