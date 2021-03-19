from clases.cliente import Cliente
from utileria.archivo import Archivo
from utileria.menu import  Menu
from utileria.TableIT import printTable
from os import system
import time

def clientes():
    system('cls')
    pos = lambda y,x:'\x1b[%d;%dH'%(y,x)
    men = Menu(['1).Ingreso','2).Listado','3).Salir'],'     Menu Clientes')
    opc = men.mostrarMenu()
    while opc != '3':
        system('cls')
        if opc == '1':
            y = 10000
            print(pos(1,25)+'Ingreso Cliente')
            nom = input('Nombre......:'+pos(3,25))
            ruc = input('Ruc.........:'+pos(4,25))
            dir = input('Direccion...:'+pos(5,25))
            tel = input('Telefono....:'+pos(6,25))
            mai = input('Email.......:'+pos(7,25))
            cli = Cliente(ruc,nom,dir,tel,mai)
            arch = Archivo()
            arch.escribir('data/cliente.txt',cli.mostrarCliente())
            x = input('Registro Grabado, Precione una tecla para continuar...')

        elif opc == '2':
            print(pos(1,15)+'Listado Cliente')
            arch = Archivo()
            datos = arch.leer('data/cliente.txt')
            tabla=[]
            tabla.append(['Ruc','Nombre','Direccion','Telefono','Email'])
        
            for dato in datos:
                #tabla.append(['\x1b[0;34m'+dato[0],'\x1b[0;34m'+dato[1],'\x1b[0;34m'+dato[2],'\x1b[0;34m'+dato[3],'\x1b[0;34m'+dato[4],'\x1b[0;34m'+dato[5]])
                tabla.append([dato[0],dato[1],dato[2],dato[3],dato[4]])
            printTable(tabla, useFieldNames=True,color=(26, 156, 171))
            x = input('\x1b[0;37m'+'Registro Grabado, Precione una tecla para continuar...')
        system('cls')
        opc = men.mostrarMenu()