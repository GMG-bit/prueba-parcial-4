nombres_compra_F =[]
nombres_compra_I = []
N_Entradas_F = 2
N_Entradas_I = 2
Cont_G_F = 0
Cont_V_F = 0
Cont_PAL_I = 0
Cont_CV_I = 0
reservas_F = {}
reservas_I = {}

def Validacion_Codigo_Confirmacion_F (codigo_con):
    #global
    errores = []
    del errores[:]
    if len(codigo_con) < 6:
        errores.append("Tamaño Contraseña insuficiente, minimo 6 caracteres")
    contador_mayusculas = 0
    contador_spacios = 0
    contador_numeros = 0
    for x in codigo_con:
        if x.isupper():
            contador_mayusculas += 1
        if x.isspace():
            contador_spacios += 1
        if x.isdigit():
            contador_numeros += 1
    if contador_mayusculas < 1 :
        errores.append("No tiene Mayuscula")
    if contador_numeros < 1:
        errores.append("No tiene Numero, Debe terner al menos 1") 
    if contador_spacios >= 1 :
        errores.append("Tiene Espacios en Blanco")
    return errores

def Validacion_Codigo_Confirmacion_I (codigo_con):
    errores = []
    del errores[:]
    if len(codigo_con) < 5:
        errores.append("Tamaño Contraseña insuficiente, minimo 5 caracteres")
    contador_mayusculas = sum(1 for x in codigo_con if x.isupper())
    contador_numeros = sum(1 for x in codigo_con if x.isdigit())
    if contador_mayusculas < 1 :
        errores.append("No tiene Mayuscula")
    if contador_numeros < 1:
        errores.append("No tiene Numero, Debe terner al menos 1") 
    if " " in codigo_con:
        errores.append("No debe Tiene Espacios en Blanco")
    return errores


def OP1(comprador):
    global N_Entradas_F,Cont_G_F,Cont_V_F,reservas_F
    if comprador in nombres_compra_F:
        print ("\n\nNombre de comprador repetido. Reintente\n\n")
        return False
    if N_Entradas_F == 0:
        print ("No quedan entradas disponibles para los Fortifiacados")
        return False
    while True:
        tipo_entrada = input("Ingrese tipo de entrada, Galeria o Vip (G/V): ").strip().upper()
        if tipo_entrada not in ("G", "V"):
            print("Tipo de entra no valida, Reintente ---> Ingrese G o V")
            continue
        else:
            break
    if (tipo_entrada == "G"):
        while True:
            codigo_cof = input ("Ingrese el codigo de confirmacion: \n(*)Debe tener un minimo de 6 caracteres\n(*)Debetener una Mayuscula y Un Numero : ")
            errores = Validacion_Codigo_Confirmacion_F(codigo_cof)
            if len(errores) == 0:
                print (45*"="+"\n\nCodigo Validado, Reservando Galeria\n")
                #para verificar reservas descomentar
                #print("Numeor entrada F ", N_Entradas_F)
                N_Entradas_F -= 1
                #print("Numeor entrada F despues:", N_Entradas_F)
                #print("Contador Galeria F", Cont_G_F)
                Cont_G_F += 1
                #print("Contador Galeria F despues",Cont_G_F)                
                print (45*"="+"\n\n!Entrada Validada con Exito!")
                reservas_F.update({comprador: "G"})
                nombres_compra_F.append(comprador) 
                return True
            else:
                print("La contraseña no cumple con los siguientes requisitos:")
                for error in errores:
                    print("-", error)
    if (tipo_entrada == "V"):
        while True:
            codigo_cof = input ("Ingrese el codigo de confirmacion: \n Debe tener un minimo de 6 caracteres, \n Debetener una Mayuscula y Un Numero : ")
            Validacion_Codigo_Confirmacion_F(codigo_cof)
            if len(errores == 0):
                print ("Codigo Validado,  Descontando Vip")
                N_Entradas_F -= 1
                Cont_V_F += 1
                print (45*"="+"\n!Entrada Validada con Exito !")
                reservas_F.update({comprador: "V"}) 
                nombres_compra_F.append(comprador) 
                return True
            else:
                print("La contraseña no cumple con los siguientes requisitos:")
                for error in errores:
                    print("-", error)
def OP2(nombre_I):
    global N_Entradas_I,Cont_PAL_I,Cont_CV_I,reservas_I
    if N_Entradas_I == 0:
        print ("No quedan entradas disponibles para los Iluminados")
        return False    
    if nombre_I in nombres_compra_I:
        print ("\n\nNombre  de comprador repetido. Reintente\n\n")
        return False
    while True:
        #strip() para limpiar espacios accidentales en input().
        #.upper() para permitir que el usuario escriba "g", "v", "G", "V" y lo tomes como válido.
        tipo_entrada = input("Ingrese tipo de entrada (PAL/CV): ").strip().upper()
        if tipo_entrada not in ("PAL", "CV"):
            print("Tipo de entra no valida, Reintente ---> Ingrese PAL o CV")
            continue
        else:
            break        
    if (tipo_entrada == "PAL"):
        while True:
            codigo_cof = input ("Ingrese el codigo de confirmacion: \n(*)Debe tener un minimo de 6 caracteres\n(*)Debetener una Mayuscula y Un Numero : ")
            errores = Validacion_Codigo_Confirmacion_F(codigo_cof)
            if len(errores) == 0:
                print (45*"="+"\n\nCodigo Validado, Reservando Palco\n")
                N_Entradas_I -= 1
                Cont_PAL_I += 1
                print (45*"="+"\n\n!Entrada Validada con Exito!\n")
                reservas_I.update({nombre_I: "PAL"})
                nombres_compra_I.append(comprador) 
                return True
            else:
                print("La contraseña no cumple con los siguientes requisitos:")
                for error in errores:
                    print("-", error)
    if (tipo_entrada == "CV"):
        while True:
            codigo_cof = input ("Ingrese el codigo de confirmacion: \n Debe tener un minimo de 6 caracteres, \n Debetener una Mayuscula y Un Numero : ")
            errores = Validacion_Codigo_Confirmacion_F(codigo_cof)
            if len(errores) == 0:
                print ("Codigo Validado,  Descontando Cancha Vip")
                N_Entradas_I -= 1
                Cont_CV_I += 1
                print (45*"="+"\n!Entrada Validada con Exito !")
                reservas_I.update({nombre_I: "CV"})
                nombres_compra_I.append(comprador) 
                return True
            else:
                print("La contraseña no cumple con los siguientes requisitos:")
                for error in errores:
                    print("-", error)
    else:
        print("Opcion no Valida Reintente")
def OP3():
        print(47*"=")
        print(f"Entradas Disponibles para los Fortificados: {N_Entradas_F}")
        print(47*"=")
        print(f"Entadas Vendidas\nGaleria : {Cont_G_F}\nVip : {Cont_V_F}\nTotal: {Cont_V_F+Cont_G_F}")
        print(45*"=")
        print(f"Entradas Disponibles para los Iluminados: {N_Entradas_I}")
        print(f"Entadas Vendidad\nPalco: {Cont_PAL_I}\nCancha Vip: {Cont_CV_I}\nTotal: {Cont_CV_I+Cont_PAL_I}")
        return None

while True:
    try:
        print("===========================================")
        print("TOTEM AUTOSERVICIO CONCIERTO ROCK AND CHILE")
        print("===========================================")
        print("1. Comprar Entrada a los Fortificados.")
        print("2. Comprar Entrada a los Iluminados.")
        print("3. Stock de entradas para ambos conciertos.")
        print("4. Visualizar reserva concierto Fortificados")
        print("5. Visualizar reserva concierto Iluminados")        
        print("6. Salir.")
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            while True:
                print(43*"="+"\nFortificados Compra de Entradas\n")
                comprador =input("Ingrese el nombre del comprador: ")
                compra_exitosa=OP1(comprador)
                if compra_exitosa == True :
                    break
                else:
                    print ("No se pudo realizar la compra")
                    break                
        elif opcion == 2:
            while True:
                print(43*"="+"\nIluminados Compra de Entradas\n")
                if N_Entradas_I == 0:
                    print("ENTRADAS AGOTADAS para Los Iluminados")
                    break
                comprador = input("Ingrese el nombre del comprador: ")
                compra_exitosa = OP2(comprador)
                if compra_exitosa:
                    break
                else:
                    print ("No se pudo realizar la compra")
                    break
        elif opcion == 3:
            OP3()
        elif opcion == 6:
            print("Programa terminado...")
            break
        elif opcion == 4:
            print(reservas_F)
        elif opcion == 5:
            print(reservas_I)
        else:
            print("Opcion invalida")
    except ValueError:
            print("Error: dato inválido") 