class Marca:
    _siguiente = 0
    def __init__(self, des, est=True):
        self.id = Marca._siguiente = Marca._siguiente +1
        self.descripcion = des
        self.estado = est
        
    def mostrarMarca(self):
        return  "{};{};{}".format(self.id,self.descripcion,self.estado)
        
    # def __str__(self):
    #     return  "{} - {} - {}".format(self.id,self.descripcion,self.estado)

# marcas = []
# for i in range(1,6):
#     nombre = input("Ingrese Marca: ")
#     marca = Marca(i,nombre, True)
#     marcas.append(marca)

# for m in marcas:
#     print(m.mostrarMarca())
    