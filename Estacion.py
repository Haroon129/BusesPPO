class Estacion:
    def __init__(self):
        self.__buses = []

    def menu(self):
        while True:
            try:
                val =  int(input(  "Seleccione una Opcion:\n"\
                        "   1.- Venta de Billetes\n"\
                        "   2.- Devolución de billetes.\n"\
                        "   3.- Estado de la venta.\n"\
                        "   0.- Salir.\n"))
                if val in range (0,4):
                    return val
                else: print("El numero no esta dentro de las opciones.")
            except:
                print("Introduce un numero, porfavor")
    
    def acciones(self):
        print("BUENOS DIAS")
        value = -1
        while value != 0:
            value = self.menu()
            if value == 1:
                val =  int(input( "A que bus quiere subirse?"))
                #if val in range (0,len(self.__buses)):

            elif value == 2:
                val =  int(input( "De que bus quiere devolver el billete?"))

            elif value == 3:
                val =  int(input( "De que bus quiere ver la información?"))

        print("QUE PASE UNA BUENA TARDE")


    def añadir_bus(self,bus):
        self.__buses.append(bus)

    def get_buses(self):
        for i in range(len(self.__buses)):
            print(self.__buses[i])


estacion = Estacion()
aux = estacion.menu()