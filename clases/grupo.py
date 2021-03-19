class Grupo:
    _siguiente=0
    def __init__(self, des, est=True):
        self.id = Grupo._siguiente = Grupo._siguiente +1
        self.descripcion = des
        self.estado = est
        
    def mostrarGrupo(self):
        return  "{};{};{}".format(self.id,self.descripcion,self.estado)

# grupos = []
# for i in range(1,6):
#     nombre = input("Ingrese Grupo: ")
#     grupo = Grupo(i,nombre, True)
#     grupos.append(grupo)

# for g in grupos:
#     print(g.mostrarGrupo())
    