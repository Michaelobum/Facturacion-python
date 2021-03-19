from clases.marca import Marca
from clases.grupo import Grupo

class Producto:
    _siguiente=0
    def __init__(self,des="",pre=1,sto=1,mar=None,gru=None,est=True):
        self.id = Producto._siguiente = Producto._siguiente + 1
        self.descripcion = des
        self.precio = pre
        self.stock = sto
        self.marca  = mar
        self.grupo = gru
        self.estado = est

    def mostrarProducto(self):
        return  "{};{};{};{};{};{};{}".format(self.id,self.descripcion,self.precio,self.stock,self.marca,self.grupo,self.estado)
    