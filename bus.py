from Estacion import Estacion
from billetes import Billetes

class Buses:
    def __init__(self, id, numAsientos):
        self.__id = id
        self.__numAsientos = numAsientos
        self.__billete = []
    
    def calcularAsientosRestantes(self):
        asientosRestantes = self.__numAsientos - len (self.__billete)
        return asientosRestantes
    
    def billete_noDup(self, billete):
        name = billete.get_name()
        apellido = billete.get_apellido()
        for i in range(len (self.__billete)):
            if self.__billete[i].get_name() == name and self.__billete[i].get_apellido() == apellido:
                return True
        return False
    
    def destruir_billete(self, name, apellido):
        for i in range(len (self.__billete)):
            if self.__billete[i].get_name() == name and self.__billete[i].get_apellido() == apellido:
                self.__billete.pop(i)
                return True
        return False

    def anadir_billete(self, billete):
        self.__billete.append(billete)
    
    def __str__(self):
        return f"Id: {self.__id}\n"\
        f"Total: {self.__numAsientos}\n"\
        f"Libre: {self.calcularAsientosRestantes()}\n"\
        f"Vendido: {len (self.__billete)}\n"