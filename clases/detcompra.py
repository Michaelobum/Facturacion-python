from clases.marca import Marca
from clases.grupo import Grupo
from clases.producto  import Producto

class DetCompra:
    _siguiente= 0
    def __init__(self, orde, pro, cost=0, can=0):
        self.id = DetCompra._siguiente = DetCompra._siguiente +1
        self.orden = orde
        self.producto = pro
        self.costo = cost#pro.precio no se toma el precio del producto ya  se ingresa el costo de la compra del producto
        self.cantidad = can
        
    def mostrarDetalle(self):
        return  "{};{};{};{};{}".format(self.orden,self.id,self.producto,self.costo,self.cantidad)

""" grupo1 = Grupo(1,"Embutidos",True)
grupo2 = Grupo(2,"Lacteos",True)
grupo3 = Grupo(3,"Colas",True)
grupos = [grupo1,grupo2,grupo3]

marca1 = Marca(1,"Plumrose",True)
marca2 = Marca(2,"La Vaquita",True)
marca3 = Marca(3,"Coca Cola",True)
marcas = [marca1,marca2,marca3]

productos = []
for i in range(0,3):
    nombre = input("Ingrese Producto: ")
    precio = input("Ingrese precio: ")
    stock = input("Ingrese stock: ")
            
    producto = Producto(i,nombre,precio,stock,marcas[i],grupos[i],True)
    productos.append(producto)

print("\nProductos Seleccionados\n")
for p in productos:
    print(p.mostrarProducto())

det1 = DetCompra(1,productos[0],1.3,5)
det2 = DetCompra(2,productos[1],0.60,15)
det3 = DetCompra(3,productos[2],0.20,10)
print("\nDetalle de Compra\n")
detalles = [det1,det2,det3]
for d in detalles:
    print(d.mostrarDetalle())
 """