from Estacion import Estacion
#from Autobus import Bus

def validar_numero(mensaje, minimo=None, maximo=None):
    while True:
        try:
            valor = int(input(mensaje))
            if minimo is not None and maximo is not None:
                if not (minimo <= valor <= maximo):
                    print(f"Introduce un número entre {minimo} y {maximo}.")
                    continue
            return valor
        except ValueError:
            print("Error: introduce un número válido.")

def crear_bus():
    asientos = validar_numero("Cuantos asientos quiere en el bus? (entre 15 a 30 asientos)", 15, 30)
    print("TODO: Añadir logica de crear_bus ")
    """
    Añadir logica de creación 
    bus = Bus(estacion.num_buses(), asientos)
    estacion.anadir_bus(bus)    
    """

def vender_billete():
    if estacion.num_buses() == 0:
        print("No hay buses disponibles en la estación.")
        return
    bus = validar_numero(f"A que bus quiere subirse? (0 a {estacion.num_buses()-1}):", 0, estacion.num_buses()-1)
    #comprobar que el bus tiene asientos disponibles
    nombre = input("Indique su nombre")
    apellido = input("Indique su apellido")
    print("TODO: Añadir logica de vender_billete ")
    """
    Añadir Comprar Billete
    billete = Billete(bus, nombre, apellido)
    logica de añadir billete a bus    
    """

def devolver_billete():
    if estacion.num_buses() == 0:
        print("No hay buses disponibles en la estación.")
        return
    bus = validar_numero(f"De qué bus quiere devolver el billete? (0 a {estacion.num_buses()-1}): ", 0, estacion.num_buses() - 1)
    nombre = input("Indique su nombre")
    apellido = input("Indique su apellido")
    print("TODO: Añadir logica de devolver_billete ")

    """
    Añadir Devolver Billete
    Comprovar que el bus tiene dicho billete
    Destruir el billete objeto    
    """
def estado_bus():
    if estacion.num_buses() == 0:
        print("No hay buses disponibles en la estación.")
        return
    indice = validar_numero(f"De qué bus quiere ver la información? (0 a {estacion.num_buses() - 1}): ", 0, estacion.num_buses() - 1)
    print("TODO: Añadir logica de estado_bus ")
    """
    Añadir Estado Bus
    """

def salir():
    print("QUE PASE UNA BUENA TARDE")
    exit()

opciones = {
    1: crear_bus,
    2: vender_billete,
    3: devolver_billete,
    4: estado_bus,
    0: salir,
}
estacion = Estacion()
print("BUENOS DIAS")
while True:
    opcion = validar_numero(
        "Seleccione una Opcion:\n"\
        "   1.- Crear Bus.\n"\
        "   2.- Venta de Billetes\n"\
        "   3.- Devolución de billetes.\n"\
        "   4.- Estado del bus.\n"\
        "   0.- Salir.\n",
        0,4)
    accion = opciones.get(opcion)
    accion()
