class Empresa:
    def __init__(self, id, ruc, nom, fecc, est=True):
        self.id = id
        self.ruc = ruc
        self.nombre = nom
        self.fecha_creacion = fecc
        self.estado = est
        
    def mostrarEmpresa(self):
        return  "{} - {} - {} - {} - {}".format(self.id,self.nombre,self.ruc,self.fecha_creacion,self.estado)

# empresa1 = Empresa(1,'0394837473001','Supermercado Tia','02/03/2000')
# print(empresa1.mostrarEmpresa())