class Proveedor:
    def __init__(self, ruc, nom, dir, tel, email, est=True):
        self.__ruc = ruc
        self.__nombre = nom
        self.__direccion = dir
        self.__telefono = tel
        self.__email  = email
        self.__estado = est

    @property
    def ruc(self):
        return self.__ruc
    
    @ruc.setter
    def ruc(self,valor):
        self.__ruc = valor

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,valor):
        self.__nombre = valor
        
    @property
    def direccion(self):
        return self.__direccion
    
    @direccion.setter
    def direccion(self,valor):
        self.__direccion = valor

    @property
    def telefono(self):
        return self.__telefono
    
    @telefono.setter
    def telefono(self,valor):
        self.__telefono = valor
    
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self,valor):
        self.__email = valor

    @property
    def estado(self):
        return self.__estado
    
    @estado.setter
    def estado(self,valor):
        self.__estado = valor
        
        
        
        
    
    def mostrarProveedor(self):
        return  "{};{};{};{};{}".format(self.ruc,self.nombre,self.direccion,self.telefono,self.email)

class ProveedorMayor(Proveedor):

    def __init__(self, ruc, nom, dir, tel, email,tar, est=True):
        super().__init__(ruc,nom,dir,tel,email,est)
        self.tarjeta =  tar
    
    def mostrarProveedor(self):
        mostrar = super().mostrarProveedor()
        return "{};{}".format(mostrar,self.tarjeta)
        
class ProveedorLote(Proveedor):

    def __init__(self, ruc, nom, dir, tel, email,ctnbanco, est=True):
        super().__init__(ruc,nom,dir,tel,email,est)
        self.cuentabanco =  ctnbanco

    def mostrarProveedor(self):
        mostrar = super().mostrarProveedor()
        return "{};{}".format(mostrar,self.cuentabanco)

# prove_lote= ProveedorLote('0748398399001','Nutileche','Duran','0298374283','nutipack@gmail.com','2093847232114')
# print(prove_lote.mostrarProveedor())
# prove_mayor= ProveedorMayor('0293299839001','Coca Cola','Guayaquil','0299227393','cocaecuador@gmail.com','Visa')
# print(prove_mayor.mostrarProveedor())