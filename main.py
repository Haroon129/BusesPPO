from Estacion import Estacion
from bus import Buses
from billetes import Billetes
import random

def validar_numero(mensaje, minimo=None, maximo=None):
    while True:
        try:
            valor = int(input(mensaje+"\n"))
            if minimo is not None and maximo is not None:
                if not (minimo <= valor <= maximo):
                    print(f"Introduce un número entre {minimo} y {maximo}.")
                    continue
            return valor
        except ValueError:
            print("Error: introduce un número válido.")

def crear_bus():
    asientos = validar_numero("Cuantos asientos quiere en el bus? (entre 15 a 30 asientos)", 15, 30)
    bus = Buses(estacion.num_buses(), asientos)
    estacion.anadir_bus(bus) 
    
    print("- El Bus ha sido creado correctamente")

def vender_billete():
    if estacion.num_buses() == 0:
        print("- No hay buses disponibles en la estación.")
        return
    bus_id = validar_numero(f"A que bus quiere subirse? (0 a {estacion.num_buses()-1}):", 0, estacion.num_buses()-1)
    bus = estacion.get_bus(bus_id)

    if bus.calcularAsientosRestantes() == 0:
        print("- No hay asientos disponibles")
        return
    nombre = input("Indique su nombre\n")
    apellido = input("Indique su apellido\n")
    billete = Billetes(nombre,apellido)
    if bus.billete_noDup(billete):
        print("- Ya hay un billete con dicho Nombre - Apellido")
        return
    bus.anadir_billete(billete)
    print("- Su billete ha sido comprado con exito")

def devolver_billete():
    if estacion.num_buses() == 0:
        print("- No hay buses disponibles en la estación.")
        return
    bus_id = validar_numero(f"De qué bus quiere devolver el billete? (0 a {estacion.num_buses()-1}): ", 0, estacion.num_buses() - 1)
    bus = estacion.get_bus(bus_id)

    nombre = input("Indique su nombre\n")
    apellido = input("Indique su apellido\n")

    if bus.destruir_billete(nombre,apellido):
        print("- El billete se ha devuelto con exito")
        return
    print("- No se ha podido devolver el billete. Compruebe que el nombre sea correcto.")
    
def estado_bus():
    if estacion.num_buses() == 0:
        print("- No hay buses disponibles en la estación.")
        return
    bus_id = validar_numero(f"De qué bus quiere ver la información? (0 a {estacion.num_buses() - 1}): ", 0, estacion.num_buses() - 1)
    bus = estacion.get_bus(bus_id)
    print(bus)

def salir():
    print("QUE TENGA UN BUEN DIA")
    exit()

def crear_n_estaciones(num_estaciones):
    estaciones = []
    for i in range (num_estaciones):
        random.shuffle(localidades)
        estaciones.append(Estacion(localidades.pop()))

    return estaciones



def menu_estacion():
    opciones = {
        1: crear_bus,
        2: vender_billete,
        3: devolver_billete,
        4: estado_bus,
        0: salir,
    }
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

estacion = Estacion("")
localidades = ["Barcelona", "Madrid", "Malaga", "Sevilla"]

print("BUENOS DIAS")
num_estacions = validar_numero("Cuantas estaciones desea abrir?\n"\
                               f"   Disponemos de {len(localidades)} localidades\n"\
                                "   Se necesita un minimo de 2 estaciones\n",2, len(localidades))

estaciones = crear_n_estaciones(num_estacions)


menu_estacion()