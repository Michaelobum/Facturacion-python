class Cliente:
    def __init__(self, ruc, nom, dir, tel, email, est=True):
        self.ruc = ruc
        self.nombre = nom
        self.direccion = dir
        self.telefono = tel
        self.email  = email
        self.estado = est
        
    def mostrarCliente(self):
        return  "{};{};{};{};{};{}".format(self.nombre,self.ruc,self.direccion,self.telefono,self.email,self.estado)


""" cli1 = Cliente('0915','Daniel','Milagro','09233434','db@gmail.com')
print(cli1.mostrarCliente())
clientes = [] """
# for i in range(1,6):
#     nombre = input("Ingrese Grupo: ")
#     grupo = Cliente(i,nombre, True)
#     clientes.append(grupo)

# for g in grupos:
#     print(g.mostrarGrupo())
    