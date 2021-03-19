from clases.marca import Marca
from clases.grupo import Grupo
from clases.producto  import Producto

class DetVenta:
    _siguiente = 0
    def __init__(self, fac=0, pro=0, pre=0.0, can=0):
        self.id = DetVenta._siguiente = DetVenta._siguiente + 1
        self.factura = fac
        self.producto = pro
        self.precio = pre
        self.cantidad = can
        
    def mostrarDetalle(self):
        return  "{};{};{};{};{}".format(self.factura,self.id,self.producto,self.precio,self.cantidad)

#producto = Producto()
# productos =  producto.listProducto()
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

det1 = DetVenta(1,productos[0],0,5)
det2 = DetVenta(2,productos[1],0,15)
det3 = DetVenta(3,productos[2],0,10)
print("\nDetalle de Venta\n")
detalles = [det1,det2,det3]
for d in detalles:
    print(d.mostrarDetalle()) """

