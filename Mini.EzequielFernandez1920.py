import funciones 
from Clases import *
import requests

#Bienvenida
print("".center(50,"="))
print('''COVID-19 Tracker'''.center(50,"="))
print("".center(50,"="))

#Comienzo modulo 1:
traductorDeRegistro = {
    "Tipo": 0,
    "nombre": 1,
    "edad": 2,
    "telefono": 3,
    "direccion": 4,
    "ciudad": 5,
    "estado": 6,
    "medico": 7
}

#Principales ciudades y estados de Venezuela:
ciudades = {"acarigua":"portuguesa", "anaco":"anzoategui", "araure":"portuguesa", "barcelona":"anzoategui", "barinas":"barinas", "barquisimeto":"lara", "baruta":"miranda", "cabimas":"zulia",
"cagua":"aragua", "calabozo":"guarico", "caracas":"distrito capital", "carupano":"sucre", "ciudad bolivar":"bolivar", "ciudad ojeda":"zulia", "cua":"miranda", "cumana":"sucre",
"el limon":"aragua", "el tigre":"anzoategui", "el vigia":"merida", "guacara":"carabobo", "guanare":"Portuguesa", "guarenas":"miranda", "guatire":"miranda", "la victoria":"aragua",
"maracaibo":"zulia", "maracay":"aragua", "maturin":"monagas", "merida":"merida", "naguanagua":"carabobo", "puerto cabello":"carabobo", "puerto la cruz":"anzoategui", "san cristobal":"tachira",
"san diego":"carabobo", "san fernando de apure":"apure", "turmero":"aragua", "upata":"bolivar", "valencia":"carabobo"}

#Menu principal
agua = True
while agua:
    inicio = input('''Indique una de las siguientes opciones:
1) Realizar test
2) Estadísticas
3) Salir
''')

    #Inicio modulo 1
    if inicio == "1":
        nombre = funciones.validar_nombre()
        edad = funciones.validar_edad()
        registro = funciones.leerRegistro(traductorDeRegistro)

        if len(registro) != 0:
            for Paciente in registro:
                if Paciente.nombre == nombre:
                    print("\tUsuario existente\t")
                    print()
                    agua = True
                elif Paciente.nombre != nombre:
                    respuestas = funciones.validar_resp()
                    break
            funciones.nuevo_paciente(respuestas,nombre,edad,ciudades)
            agua = True

        elif len(registro) == 0:
            respuestas = funciones.validar_resp()
            funciones.nuevo_paciente(respuestas,nombre,edad,ciudades)
            agua = True

    #Inicio modulo 2
    elif inicio == "2":
        #API usada para formar el registro de paises
        url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/stats"
        headers = {
            'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com",
            'x-rapidapi-key': "da7ac0bd27msh90c7f44e79628ddp13a4a3jsn5e4b7b86c96c"
            }
        fuego = True
        while fuego:
            pais = input("Ingrese el nombre del pais en ingles (Respete las mayúsculas): ")
            paises = funciones.leerPaises()
            for x in range(len(paises)):
                if pais == paises[x][1]:
                    querystring = {"country": pais}
                    fuego = False

        response = requests.request("GET", url, headers=headers, params=querystring)
        virus = response.json()
        print("------------")
        print("Provincias: ")
        print("------------")
        print(virus["data"]["covid19Stats"])
        print("".center(200,"-"))

        #Ver TOPS10
        tierra = True
        while tierra:
            opcion = input('''Indique una de las siguientes opcciones: 
1) Ver Top10 de paises con mas infectados por coronavirus
2) Ver Top10 de paises con mas muertos por coronavirus
3) Ver Top10 de paises con mas recuperados de coronavirus
4) Regresar al menu principal
''')

            #Top 10 por Infectados
            if opcion == "1":
                print("".center(50,"="))
                print('''TOP 10/Infectados'''.center(50,"="))
                print("".center(50,"="))
                Paises = funciones.leerPaises()
                archivo = open("Top10Infectados.txt", "w")
                if len(Paises) >= 9:
                    for x in range(0,10):
                        archivo.write("{},{},{},{},{},{}".format(Paises[x][0], Paises[x][1], Paises[x][2], Paises[x][3], Paises[x][4], Paises[x][5]))
                    archivo.close()

                elif len(Paises) < 9:
                    for x in range(len(Paises)):
                        archivo.write("{},{},{},{},{},{}".format(Paises[x][0], Paises[x][1], Paises[x][2], Paises[x][3], Paises[x][4], Paises[x][5]))
                    archivo.close()

                Top10 = funciones.buscarTop10Infectados()
                for x in range(len(Top10)):
                    print("{}/{}/{}/{}/{}/{}".format(Top10[x][0], Top10[x][1], Top10[x][2], Top10[x][3], Top10[x][4], Top10[x][5]))
                print("".center(50,"="))

            #Top 10 por muertos
            elif opcion =="2":
                print("".center(50,"="))
                print('''TOP 10/Muertos'''.center(50,"="))
                print("".center(50,"="))
                Paises = funciones.leerPaises()
                Paises.sort(reverse = True, key = lambda pais : int(pais[4]))
                archivo = open("Top10Muertos.txt", "w")
                if len(Paises) >= 9:
                    for x in range(0,10):
                        archivo.write("{},{},{},{},{},{}".format(Paises[x][0], Paises[x][1], Paises[x][2], Paises[x][3], Paises[x][4], Paises[x][5]))
                    archivo.close()

                elif len(Paises) < 9:
                    for x in range(len(Paises)):
                        archivo.write("{},{},{},{},{},{}".format(Paises[x][0], Paises[x][1], Paises[x][2], Paises[x][3], Paises[x][4], Paises[x][5]))
                    archivo.close()

                Top10 = funciones.buscarTop10Muertos()
                for x in range(len(Top10)):
                    print("{}/{}/{}/{}/{}/{}".format(Top10[x][0], Top10[x][1], Top10[x][2], Top10[x][3], Top10[x][4], Top10[x][5]))
                print("".center(50,"="))

            #Top 10 por recuperados
            elif opcion == "3":
                print("".center(50,"="))
                print('''TOP 10/Recuperados'''.center(50,"="))
                print("".center(50,"="))
                Paises = funciones.leerPaises()
                Paises.sort(reverse = True, key = lambda pais : int(pais[5]))
                archivo = open("Top10Recuperados.txt", "w")
                if len(Paises) >= 9:
                    for x in range(0,10):
                        archivo.write("{},{},{},{},{},{}".format(Paises[x][0], Paises[x][1], Paises[x][2], Paises[x][3], Paises[x][4], Paises[x][5]))
                    archivo.close()

                elif len(Paises) < 9:
                    for x in range(len(Paises)):
                        archivo.write("{},{},{},{},{},{}".format(Paises[x][0], Paises[x][1], Paises[x][2], Paises[x][3], Paises[x][4], Paises[x][5]))
                    archivo.close()

                Top10 = funciones.buscarTop10Recuperados()
                for x in range(len(Top10)):
                    print("{}/{}/{}/{}/{}/{}".format(Top10[x][0], Top10[x][1], Top10[x][2], Top10[x][3], Top10[x][4], Top10[x][5]))
                print("".center(50,"="))

            #Regresar menu principal
            elif opcion == "4":
                tierra = False

            else:
                print("---------------")
                print("Opción inválida")
                print("---------------")
                tierra = True

    #Salir del programa
    elif inicio == "3":
        agua = False

    else:
        print("---------------")
        print("Opción inválida")
        print("---------------")
        agua = True




