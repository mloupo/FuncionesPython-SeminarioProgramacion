from misFunciones import *
listaNumeros = []
diccionario = {}
otroDiccionario={}
listaSocios={}


def control_menu(listaNumeros, listaSocios, diccionario, otroDiccionario):
    interruptor = True
    while interruptor:

        opcion = seleccion_menu()
        if opcion == 1:
            print("\nOpcion 1\n")
            listaNumeros = agregaNroLista()
            mostrarLista(listaNumeros)
        elif opcion == 2:
            print("\nOpcion 2\n")
            mostrarLista(listaNumeros)

        elif opcion == 3:
            print("\nOpcion 3\n")
            listaNumeros = eliminaNroLista(listaNumeros)
            mostrarLista(listaNumeros)

        elif opcion == 4:
            print("\nOpcion 4\n")
            listaNumeros.clear()
            mostrarLista(listaNumeros)

        elif opcion == 5:
            print("\nOpcion 5\n")
            print("Muestra(N): ", len(listaNumeros))
            listaNumeros = frecuencias(listaNumeros)
            mostrarLista(listaNumeros)

        elif opcion == 6:
            print("\nOpcion 6\n")
            listaNumeros = newListaLim(listaNumeros)
            mostrarLista(listaNumeros)

        elif opcion == 7:
            print("\nOpcion 7\n")
            diccionario = cargarDiccionario(diccionario)
            mostrarDiccionario(diccionario)

        elif opcion == 8:
            print("\nOpcion 8\n")
            listaNumeros = listaDeLlavesNumericas(diccionario)
            mostrarLista(listaNumeros)

        elif opcion == 9:
            print("\nOpcion 9\n")
            listaSocios = cargarSocios(listaSocios)
            imprimirListadoSocios(listaSocios)

        elif opcion == 10:
            print("\nOpcion 10\n")
            nombre = input("Ingrese nombre a buscar: ")
            numeroSocio = numeroSocio(listaSocios, nombre)
            print("El numero de asociado es: ", numeroSocio)

        elif opcion == 11:
            print("\nOpcion 11\n")
            listaSocios, diccionario, otroDiccionario = cargarDiccHard()

        elif opcion == 12:
            print("\nOpcion 12\n")
            imprimirListadoSocios(listaSocios)
            mostrarDiccionario(diccionario)
            mostrarDiccionario(otroDiccionario)

        elif opcion == 13:
            print("\nOpcion 13\n")
            numero = int(input("Ingrese numero de socio: "))
            eliminarSocio(listaSocios, numero)
            imprimirListadoSocios(listaSocios)

        elif opcion == 14:
            print("\nOpcion 14\n")
            mostrarCantidadSocios(listaSocios)

        elif opcion == 15:
            print("\nOpcion 15\n")
            socio=int(input("Ingrese socio: "))
            fecha=input("Ingrese Fecha: ")         
            listaSocios = modificarFecha(listaSocios, socio, fecha)
        elif opcion == 16:
            print("\nOpcion 16\n")
            registrarCuotaSocio(listaSocios)

        elif opcion == 0:
            print("\nOpcion Salir\n")
            """Fin App"""
            interruptor = salir()





   
control_menu(listaNumeros, listaSocios, diccionario, otroDiccionario)
    




    
    
