# FUNCION INGRESAR NUMEROS
def agregaNroLista():
    muestra = []
    nro = int(input("Ingrese Nro: "))
    while nro != 0:
        muestra.append(nro)
        nro = int(input("Ingrese Nro: "))
    return muestra


def sumatoriaListaNros(listaNros):
    suma = 0
    for n in listaNros:
        suma += n
    print(suma)


def mostrarLista(lista):
    print("Lista: ", lista)
    print("------------------------------\n")


def eliminaNroLista(listaNumeros):

    eliminar = int(input("Ingrese numero a eliminar: "))
    if eliminar in listaNumeros:
        listaNumeros.remove(eliminar)
    else:
        print("El numero no esta en la lista")
    return listaNumeros


# funcion buscar un caracter en un string


def validar(miString):
    caracterBuscado = "@"
    for c in miString:
        if c == caracterBuscado:
            return True
        return False


def numerosFiltrados(listaNros, lim):
    nuevaListaNros = []
    for n in listaNros:
        if n < lim:
            nuevaListaNros.append(n)
    return nuevaListaNros


def continuar():
    seguir = 10
    while seguir != 0 or seguir != 1:
        print("Desea continuar: ")
        print("\t0- Volver ")
        print("\t1- Continuar: ")
        seguir = int(input("Ingresa tu eleccion: "))
        return seguir


def newListaLim(listaNros):
    limite = int(input("Ingresa limite: "))
    nuevaListaNumeros = numerosFiltrados(listaNros, limite)
    # for n in nuevaListaNumeros:
    # print(n)
    return nuevaListaNumeros


def frecuencias(listaNros):
    nuevaListaNros = []
    for n in listaNros:
        if ((n, listaNros.count(n))) not in nuevaListaNros:
            nuevaListaNros.append((n, listaNros.count(n)))
    return (nuevaListaNros)


def cargarDiccionario(diccionario):
    diccionario = {}
    clave = True
    while clave:
        clave = input("Ingresa palabra Clave: ")
        if clave == "0":
            clave = False
        else:
            valor = input("Ingresa Valor: ")
            diccionario[clave] = valor
    return diccionario


def mostrarDiccionario(diccionario):
    print("Diccionario: ", diccionario)
    esperar()
    print("---------------------------\n")


def listaDeLlavesNumericas(diccionario):
    listaKeysNumericas = []
    for llave in diccionario.keys():
        if (type(llave)) == int or (type(llave)) == float:
            listaKeysNumericas.append(llave)

    return (listaKeysNumericas)


def cargarSocios(socios):
    numero = int(input("Número de socio (0 para cortar): "))
    while numero != 0:
        nombre = input("Nombre y apellido: ")
        fecha = input("Fecha de ingreso (DDMMAAAA): ")
        cuota = input("¿Cuota al día? s/n: ")
        socios[numero] = [nombre, fecha, cuota.lower() == "s"]
        numero = int(input("Número de socio (0 para cortar): "))
    return socios


def modificarFecha(socios, socio, fecha_nueva):
    print("***Modificando fecha de ingreso...")
    print(type(socios[socio]))
    if socios[socio][1]!=[]:
        print("Fecha anterior: ", formatoFecha(socios[socio][1]))
        socios[socio][1] = formatoFecha(fecha_nueva)
        print("Luego de la modificacion: ", socios[socio][1])
        esperar()
        return socios
    else:
        print("El socio no existe")
        esperar()


def numeroSocio(socios, nombre):
    for numero, datos in socios.items():
        if datos[0].lower() == nombre.lower():
            return numero
    return 0


def formatoFecha(fecha):
    return fecha[:2]+"/"+fecha[2:4]+"/"+fecha[4:]


def imprimirListadoSocios(socios):
    for numero, datos in socios.items():
        print("-Número:", numero)
        print("-Nombre:", datos[0])
        print("-Ingresó:", formatoFecha(datos[1]))
        if datos[2]:
            print("-Cuota al día")
        else:
            print("-En deuda")
        print("-------------------------\n")
        esperar()


def registrarCuotaSocio(listaSocios):
    print("***Registrar pago de cuotas")
    numero = int(input("Número de socio: "))
    listaSocios[numero][2] = True


def cargarDiccHard():
    diccionarioHard = {"Martin": "29628346", "1234": "Romina",
                       "Santiago": "458", "165.5": "", }
    otroDiccionarioHard = {"Martin": ["Pera", "Manzana", "Naranja"], "Paola": ["Anana", "Pomelo", "Sandia"],
                           "Santiago": ["Melon", "Pera"]}
    listaSociosHard = {1: ["Amanda Núñez", "17032009", False], 2: [
        "Bárbara Molina", "17032009", True], 3: ["Lautaro Campos", "17032009", True]}
    print("Diccionario cargado exitosamente!")
    esperar()
    return(listaSociosHard, diccionarioHard, otroDiccionarioHard)


def eliminarSocio(listaSocios, numero):
    if numero in listaSocios:
        del listaSocios[numero]
        return listaSocios
    else:
        print("El numero de socio no se encuentra en la lista")


def mostrarCantidadSocios(listaSocios):
    print("El club tiene", len(listaSocios), "socios")


def esperar():
    input("Presione una tecla para continuar: ")
    print("\n")


def salir():
    print("Gracias por utilizar Zaiken Applications!")
    print("Hasta Luego!!")
    esperar()
    interruptor = False
    return interruptor


def muestra_opciones():
    """_summary_
    """
    print("----Menu principal del programa----")
    print("\tSELECCIONE UNA OPCION DEL MENU")
    print("\t\t1- Cargar lista de numeros")
    print("\t\t2- Mostrar listado de numeros")
    print("\t\t3- Eliminar numero de la lista")
    print("\t\t4- Eliminar lista")
    print("\t\t5- Ver Frecuencia")
    print("\t\t6- Filtrar Lista")
    print("\t\t7- Cargar diccionario")
    print("\t\t8- Lista de keys numericas en diccionario")
    print("\t\t9- Buscar numero de socio por nombre")
    print("\t\t10- Imprimir listado de socios")
    print("\t\t11- Cargar diccionario harcodeado")
    print("\t\t12- Mostrar diccionarios")
    print("\t\t13- Eliminar socio")
    print("\t\t14- Mostrar cantidad de socios")
    print("\t\t15- Modificar fecha ingreso cliente")
    print("\t\t16- Ragistrar pago cuota cliente")
    print("\t\t0- Fin Programa")


def seleccion_menu():
    """_summary_
    """
    muestra_opciones()
    print("Seleccione una opcion del Menu: ")
    opc = int(input("Opcion: "))
    while (opc > 16 or opc < 0):
        print("la opcion que selecciono no es valida.")
        opc = int(input("Opcion: "))
    return opc
