class Archivo:
    def leer(self,name):
        registros = []
        with open(name, 'r') as datos:
            for dato in datos:
                registro = dato[:-1].split(';')
                registros.append(registro)
        return registros

    def escribir(self,name,datos):
        with open(name, mode='a',encoding='utf-8') as writer:
            writer.write(datos + '\n')
        return''
        