from clases.marca import Marca
from clases.grupo import Grupo
from clases.producto  import Producto
from clases.empresa import Empresa
from clases.cliente import Cliente
from clases.empleado import Empleado
from clases.detventa import DetVenta

class Venta:
    def __init__(self, fac, fec, cli, sub,iva,tot,det=[],est=True):
        self.factura = fac
        self.fecha = fec
        self.cliente = cli
        #self.empleado = emp
        self.subtotal = sub
        self.iva = iva
        self.total = tot
        self.detalle = det
        self.estado = est
        
    def mostrarVenta(self):
        return '{};{};{};{};{};{}'.format(  
                    self.factura,
                    self.fecha,
                    self.cliente,
                    #self.empleado,
                    self.subtotal,
                    self.iva,
                    self.total)


# grupo1 = Grupo(1,"Embutidos",True)
# grupo2 = Grupo(2,"Lacteos",True)
# grupo3 = Grupo(3,"Colas",True)
# grupos = [grupo1,grupo2,grupo3]

# marca1 = Marca(1,"Plumrose",True)
# marca2 = Marca(2,"La Vaquita",True)
# marca3 = Marca(3,"Coca Cola",True)
# marcas = [marca1,marca2,marca3]

# productos = []
# for i in range(0,3):
#     nombre = input("Ingrese Producto: ")
#     precio = input("Ingrese precio: ")
#     stock = input("Ingrese stock: ")
            
#     producto = Producto(i,nombre,precio,stock,marcas[i],grupos[i],True)
#     productos.append(producto)

# print("\nProductos Seleccionados\n")
# for p in productos:
#     print(p.mostrarProducto())

# det1 = DetVenta(1,productos[0],0,5)
# det2 = DetVenta(2,productos[1],0,15)
# det3 = DetVenta(3,productos[2],0,10)
# detalle = [det1,det2,det3]

# cli1 = Cliente('0915','Daniel','Milagro','09233434','db@gmail.com')
# empresa1 = Empresa(1,'0394837473001','Supermercado Tia','02/03/2000')
# empl1 = Empleado(1,'0949029831','Juan',400.00,'12/02/20',empresa1)

# venta1 = Venta('F01','03/03/2021',cli1,empl1,20,2,22,detalle)

# datosVenta = venta1.mostrarVenta()
# print('\nDatos de la facura\n')
# print(datosVenta[0],datosVenta[1],datosVenta[2].nombre,datosVenta[3].nombre,datosVenta[6])
# print('\nDetalle de la facura\n')
# for det  in datosVenta[7]:
#     print(det.mostrarDetalle())

