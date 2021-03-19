from clases.marca import Marca
from clases.grupo import Grupo
from clases.producto  import Producto
from clases.proveedor import ProveedorLote, ProveedorMayor
from clases.detcompra import DetCompra

class Compra:
    def __init__(self,orde, fec, prov, sub,iva,tot,det=[],est=True):
        self.orden = orde
        self.fecha = fec
        self.proveedor = prov
        self.subtotal = sub
        self.iva = iva
        self.total = tot
        self.detalle = det
        self.estado = est
        
    def mostrarVenta(self):
        return '{};{};{};{};{};{}'.format(
                    self.orden,
                    self.fecha,
                    self.proveedor,
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

# producto1 = Producto(1,'Leche 1 litro',1,marcas[1],grupos[1])
# producto2 = Producto(2,'Leche Condensada',4.50,marcas[1],grupos[1])
# producto3 = Producto(3,'Leche en polvo',2.50,marcas[1],grupos[1])
# producto4 = Producto(4,'Leche Descremada',3.50,marcas[1],grupos[1])
# productos  = [producto1,producto2,producto3,producto4]

# det1 = DetCompra(1,productos[0],0.60,50)#el costo $1.3 del producto se ingresa ya que no el precio es para la venta
# det2 = DetCompra(2,productos[1],3.40,150)
# det3 = DetCompra(3,productos[2],1.75,100)
# det4 = DetCompra(4,productos[3],2.75,100)
# detalle1 = [det1,det2,det3,det4]

# proveedor_lote = ProveedorLote('0748398399001','La Vaquita','Duran','0298374283','lavaquita@gmail.com','2093847232114')

# print('\nProveedor Por Lote\n')
# compra1 = Compra('OC-02993','04/03/21',proveedor_lote,5000,500,5500,detalle1)
# datosVenta = compra1.mostrarVenta()
# print('\nDatos de la facura\n')
# print(datosVenta[0],datosVenta[1],datosVenta[2].nombre,datosVenta[5])
# print('\nDetalle de la facura\n')
# for det  in datosVenta[6]:
#     print(det.mostrarDetalle())



# prove_mayor= ProveedorMayor('0293299839001','Coca Cola','Guayaquil','0299227393','cocaecuador@gmail.com','Visa')


# productos = []

# producto1 = Producto(1,'Cola personal',0.30,marcas[2],grupos[2])
# producto2 = Producto(2,'Cola 1 Lt',0.90,marcas[2],grupos[2])
# producto3 = Producto(3,'Cola 3 Lt',2.50,marcas[2],grupos[2])
# producto4 = Producto(4,'Cola retornable 1 lt',3.50,marcas[2],grupos[2])
# productos  = [producto1,producto2,producto3,producto4]

# det1 = DetCompra(1,productos[0],0.60,50)#el costo $1.3 del producto se ingresa ya que no el precio es para la venta
# det2 = DetCompra(2,productos[1],3.40,150)
# det3 = DetCompra(3,productos[2],1.75,100)
# det4 = DetCompra(4,productos[3],2.75,100)
# detalle1 = [det1,det2,det3,det4]

# print('\nProveedor Por Mayor\n')
# compra1 = Compra('OC-02993','04/03/21',prove_mayor,5000,500,5500,detalle1)
# datosVenta = compra1.mostrarVenta()
# print('\nDatos de la facura\n')
# print(datosVenta[0],datosVenta[1],datosVenta[2].nombre,datosVenta[5])
# print('\nDetalle de la facura\n')
# for det  in datosVenta[6]:
#     print(det.mostrarDetalle())
