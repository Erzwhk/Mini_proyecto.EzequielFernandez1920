from Clases import *

#Función para validar el nombre:
def validar_nombre():
        VerNombre = True
        while VerNombre:
            nombre = input("Indique el nombre completo (sin espacios, sin mayúsculas y sin comas): ")
            nombre1 = nombre.isalpha()
            nombre2 = nombre.islower()
            if nombre1 == True and nombre2 == True and "'" not in nombre:
                VerNombre = False
            else:
                VerNombre = True
        return nombre

#Función para validar la edad:
def validar_edad():
        VerEdad = True
        edad2 = -1
        while VerEdad or edad2 < 0 or edad2 > 100:
            edad = input("Indique su edad (Hasta 100 años): ")
            edad1 = edad.isdigit()
            if edad1 == True:
                edad2 = int(edad)
            if edad1 == True:
                VerEdad = False
            elif edad1 == False:
                VerEdad = True
            else:
                VerEdad = True
        return edad

#Función para validar el telefono:
def validar_telefono():
    VerTelefono = True
    tel = 0
    while VerTelefono or tel != 11:
        telefono = input("Indique su número de teléfono: ")
        telefono1 = telefono.isdigit()
        tel = len(telefono)
        if telefono1 == True:
            VerTelefono = False
        elif telefono1 == False:
            VerTelefono = True
        else:
            VerTelefono = True
    return telefono

#Función para validar la direccion:
def validar_direccion():
    agua = True
    while agua:
        direccion = input("Ingrese su direccion (Use la barra espaciadora en vez de comas): ")
        if len(direccion) < 15:
            print("Direccion poco detallada")
            agua = True
        elif len(direccion) >= 15 and " " in direccion and "," not in direccion:
            agua = False
        else:
            agua = True

    return direccion

#Función para validar la ciudad y el estado:
def validar_ciudad(ciudades):
    agua = True
    while agua:
        ciudad = input("Ingrese la ciudad en la cual reside: ")
        estado = input("Ingrese el estado: ")
        ciudad = ciudad.lower()
        estado = estado.lower()
        listaDeCiudades = ciudades.keys()
        if ciudad in listaDeCiudades:
            x = ciudades[ciudad]
            if x != estado:
                print("La ciudad no coincide con el estado")
                agua = True
            elif x == estado:
                agua = False
        else:
            print("Ciudad o estado inválido")
            agua = True

    ciudad_estado = { "ciudad" : ciudad, "estado" : estado}
    return ciudad_estado

#Validar respuestas:
def validar_resp():
    respuestas = 0
    agua = True
    while agua:
        pre1 = True
        while pre1:
            print("¿Tiene secreciones nasales?")
            p1 = input("Ingrese 1 para SI o 2 para NO: ")
            if p1 == "1":
                respuestas = respuestas + 1
                pre1 = False
            elif p1 == "2":
                pre1 = False
            else:
                pre1 = True

        pre2 = True
        while pre2:
            print("¿Tiene dolor de garganta?")
            p2 = input("Ingrese 1 para SI o 2 para NO: ")
            if p2 == "1":
                respuestas = respuestas + 1
                pre2 = False
            elif p2 == "2":
                pre2 = False
            else:
                pre2 = True

        pre3 = True
        while pre3:
            print("¿Tiene tos?")
            p3 = input("Ingrese 1 para SI o 2 para NO: ")
            if p3 == "1":
                respuestas = respuestas + 1
                pre3 = False
            elif p3 == "2":
                pre3 = False
            else:
                pre3 = True

        pre4 = True
        while pre4:
            print("¿Tienes fiebre?")
            p4 = input("Ingrese 1 para SI o 2 para NO: ")
            if p4 == "1":
                respuestas = respuestas + 1
                pre4 = False
            elif p4 == "2":
                pre4 = False
            else:
                pre4 = True

        pre5 = True
        while pre5:
            print("¿Dificultad para respirar?")
            p5 = input("Ingrese 1 para SI o 2 para NO: ")
            if p5 == "1":
                respuestas = respuestas + 1
                pre5 = False
                agua = False
            elif p5 == "2":
                pre5 = False
                agua = False
            else:
                pre5 = True
    return respuestas

#Leer registro de pacientes:
def leerRegistro(traductorDeRegistro):
    try:
        registro = []
        archivo = open("Registro.txt", "r")
        for linea in archivo.readlines():
            listaDeValores = linea.split(",")
            if listaDeValores[traductorDeRegistro["Tipo"]] == "No_infectado":
                registro.append(No_infectado(listaDeValores[traductorDeRegistro["nombre"]],listaDeValores[traductorDeRegistro["edad"]],listaDeValores[traductorDeRegistro["telefono"]]))
            elif listaDeValores[traductorDeRegistro["Tipo"]] == "Posible_infectado":
                registro.append(Posible_infectado(listaDeValores[traductorDeRegistro["nombre"]],listaDeValores[traductorDeRegistro["edad"]],listaDeValores[traductorDeRegistro["direccion"]],listaDeValores[traductorDeRegistro["ciudad"]],listaDeValores[traductorDeRegistro["estado"]]))
            elif listaDeValores[traductorDeRegistro["Tipo"]] == "Infectado":
                registro.append(Infectado(listaDeValores[traductorDeRegistro["nombre"]],listaDeValores[traductorDeRegistro["edad"]],listaDeValores[traductorDeRegistro["direccion"]],listaDeValores[traductorDeRegistro["ciudad"]],listaDeValores[traductorDeRegistro["estado"]],listaDeValores[traductorDeRegistro["medico"]]))
        archivo.close()
        return registro

    except FileNotFoundError:
        return registro

#Nuevo paciente:
def nuevo_paciente(respuestas,nombre,edad,ciudades):
    if respuestas >= 1:
        print("-----------")
        print("En revisión")

        if respuestas > 2 and respuestas < 5:
            print("-----------------")
            print("Posible infectado")
            print("-----------------")
            direccion = validar_direccion()
            ciudad_estado = validar_ciudad(ciudades)
            ciudad = ciudad_estado["ciudad"]
            estado = ciudad_estado["estado"]
            archivo = open("Registro.txt", "+a")
            archivo.write(Posible_infectado(nombre,edad,direccion,ciudad,estado).string() + '\n')
            archivo.close() 
            print("".center(150,"="))
            Posible_infectado(nombre,edad,direccion,ciudad,estado).datos()
            print("".center(150,"="))
            
        elif respuestas == 5:
            print("--------------------")
            print("Usted esta infectado")
            print("--------------------")
            direccion = validar_direccion()
            ciudad_estado = validar_ciudad(ciudades)
            ciudad = ciudad_estado["ciudad"]
            estado = ciudad_estado["estado"]
            VerNombre = True
            while VerNombre:
                medico = input("Indique el nombre de su medico (sin espacios, sin mayúsculas y sin comas): ")
                nombre1 = medico.isalpha()
                nombre2 = medico.islower()
                if nombre1 == True and nombre2 == True and "," not in medico:
                    VerNombre = False
                else:
                    VerNombre = True
            archivo = open("Registro.txt", "+a")
            archivo.write(Infectado(nombre,edad,direccion,ciudad,estado,medico).string() + '\n')
            archivo.close() 
            print("".center(150,"="))
            Infectado(nombre,edad,direccion,ciudad,estado,medico).datos()
            print("".center(150,"="))
            
    elif respuestas == 0:
        print("-----------------------")
        print("Usted no esta infectado")
        print("-----------------------")
        telefono = validar_telefono()
        archivo = open("Registro.txt", "+a")
        archivo.write(No_infectado(nombre, edad, telefono).string() + '\n')
        archivo.close()
        print("".center(100,"="))
        No_infectado(nombre, edad, telefono).datos()
        print("".center(100,"="))
        
    return True

#Leer historial de paises en base de datos
def leerPaises():
    listaDePaises = []
    archivo = open("Paises.txt", "r")
    for linea in archivo.readlines():
        listaDeValores = linea.split(",")
        listaDePaises.append(listaDeValores)
        archivo.close()
    return listaDePaises

#Buscar TOP 10 por Infectados
def buscarTop10Infectados():
    listaDePaises = []
    archivo = open("Top10Infectados.txt", "r")
    for linea in archivo.readlines():
        listaDeValores = linea.split(",")
        listaDePaises.append(listaDeValores)
        archivo.close()
    return listaDePaises

#Buscar TOP 10 por muertos
def buscarTop10Muertos():
    listaDePaises = []
    archivo = open("Top10Muertos.txt", "r")
    for linea in archivo.readlines():
        listaDeValores = linea.split(",")
        listaDePaises.append(listaDeValores)
        archivo.close()
    return listaDePaises

#Buscar TOP 10 por recuperados
def buscarTop10Recuperados():
    listaDePaises = []
    archivo = open("Top10Recuperados.txt", "r")
    for linea in archivo.readlines():
        listaDeValores = linea.split(",")
        listaDePaises.append(listaDeValores)
        archivo.close()
    return listaDePaises