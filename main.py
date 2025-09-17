from Estacion import Estacion
from 

estacion = Estacion()
def validar_numero(num):
    try:
        value =  int(num)
    except:
        print("Introduce un numero, porfavor")

print("BUENOS DIAS")
value = -1
while value != 0:
    while True:
        value =  int(input(  "Seleccione una Opcion:\n"\
                "   1.- Crear Bus.\n"\
                "   2.- Venta de Billetes\n"\
                "   3.- Devolución de billetes.\n"\
                "   4.- Estado del bus.\n"\
                "   0.- Salir.\n"))
        if value in range (0,5):
            break
        else: print("El numero no esta dentro de las opciones.")

    if value == 1:
        while True:
            val =  int(input( "Cuantos asientos quiere en el bus? (entre 15 a 30 asientos)"))
            validar_numero(val)


    elif value == 2:
        val =  int(input( "A que bus quiere subirse?"))
        #if val in range (0,len(self.__buses)):

    elif value == 3:
        val =  int(input( "De que bus quiere devolver el billete?"))

    elif value == 4:
        val =  int(input( "De que bus quiere ver la información?"))

print("QUE PASE UNA BUENA TARDE")