from proveedor import ProveedorMayor

class TarjetaCredito:
    def __init__(self, id, prov,fecp, pago,tarjeta="", est= True):
        self.id = id
        self.proveedor = prov
        self.fecha_pago = fecp
        self.pago = pago
        self.tarjeta = tarjeta
        self.estado =  est
    
    def mostrarTarjeta(self):
        return "{} - {} - {} - {} - {} - {}".format( self.id,self.proveedor.nombre,self.fecha_pago,self.pago,self.tarjeta,self.estado)


prove1= ProveedorMayor('0293299839001','Coca Cola','Guayaquil','0299227393','cocaecuador@gmail.com','Visa')

Tarj1 = TarjetaCredito(1,prove1,'05/03/21',550.00,prove1.tarjeta)
print(Tarj1.mostrarTarjeta())