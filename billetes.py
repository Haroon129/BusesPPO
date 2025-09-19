class Billetes:
    def __init__(self, name, apellido):
        self.__name = name
        self.__apellido = apellido
    
    def set_name(self, name):
        self.__name = name
    
    def get_name(self):
        return self.__name
    
    def set_apellido(self, apellido):
        self.__apellido = apellido

    def get_apellido(self):
        return self.__apellido
    
    def __str__(self):
        return f"{self.__name} {self.__apellido}"
