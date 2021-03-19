class Menu:
    def __init__(self, opciones=[], titulo= "", car="*"):
        self.__opciones = opciones
        self.__titulo = titulo

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, valor):
        self.__titulo = valor

    def mostrarMenu(self):
        print('{}'.format(self.titulo))
        for opcion in self.__opciones:
            print('{}'.format(opcion))
        return input('Elija Opcion:[1....{}] '.format(len(self.__opciones)))

        
        
        