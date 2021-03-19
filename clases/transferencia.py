from proveedor import ProveedorLote

class Transferencia:
    def __init__(self, id, prov,fecp, pago,ban,cuen, est= True):
        self.id = id
        self.proveedor = prov
        self.fecha_pago = fecp
        self.pago = pago
        self.cuenta_bancaria = cuen
        self.banco = ban
        self.estado =  est
    
    def mostrarTransferencia(self):
        return "{} - {} - {} - {} - {} - {} - {}".format( self.id,self.proveedor.nombre,self.fecha_pago,self.pago,self.cuenta_bancaria,self.banco,self.estado)

prov1= ProveedorLote('0748398399001','Nutileche','Duran','0298374283','nutipack@gmail.com','2093847232114')
trans1  = Transferencia(1,prov1, '05/03/21',450.98,'Banco Pacifico',prov1.cuenta_banco)
print(trans1.mostrarTransferencia())