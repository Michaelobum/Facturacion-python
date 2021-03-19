from clases.empresa import Empresa

class Empleado:
    def __init__(self, id, ced, nom, sue, feci,empr, est=True):
        self.id = id
        self.cedula = ced
        self.nombre = nom
        self.fecha_ingreso = feci
        self.empresa = empr
        self.sueldo = sue
        self.estado = est
        
    def mostrarEmpleado(self):
        return  "{} - {} - {} - {} - {} - {} - {}".format(self.id,self.nombre,self.cedula,self.fecha_ingreso,self.empresa.nombre,self.sueldo,self.estado)

# empresa1 = Empresa(1,'0394837473001','Supermercado Tia','02/03/2000')
# empl1 = Empleado(1,'0949029831','Juan',400.00,'12/02/20',empresa1)
# print(empl1.mostrarEmpleado())
