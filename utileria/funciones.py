def gotoxy(x,y):
    print ("%c[%d;%df" % (0x1B, y, x), end='')

def buscarRegistro(datos,buscado):
    resp=[]
    for registro in datos:
        if registro[0] == buscado:
            resp = registro
    return resp

def getIva():
    return 0.12

def generarCodigoAutomatico(datos,pos=0):
    return int(datos[-1][pos])+1