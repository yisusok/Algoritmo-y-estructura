def cuenta_Atras(numero):
    numero-=1
    if numero > 0:
        print(numero)
        cuenta_Atras(numero)
    else:
        print("boom")
    print("orden de liberacion", numero)
    
cuenta_Atras(5)


#ejercicios desde la pag 24