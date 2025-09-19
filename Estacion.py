class Estacion:
    def __init__(self):
        self.__buses = []
        self.__contador = 0

    def num_buses(self):
        return len(self.__buses)

    def anadir_bus(self,bus):
        self.__buses.append(bus)

    def get_bus(self,id):
        return self.__buses[id]

    def get_buses(self):
        for i in range(len(self.__buses)):
            print(self.__buses[i])