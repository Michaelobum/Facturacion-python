from clases.grupo import Grupo
from utileria.archivo import Archivo
from utileria.menu import  Menu
from utileria.TableIT import printTable
from utileria.funciones  import generarCodigoAutomatico
from os import system, path
import time

def grupos():
    system('cls')
    pos = lambda y,x:'\x1b[%d;%dH'%(y,x)
    men = Menu(['1).Ingreso','2).Listado','3).Salir'],'     Menu Grupos')
    opc = men.mostrarMenu()
    while opc != '3':
        system('cls')
        if opc == '1':
            y = 10000
            print(pos(1,25)+'Ingreso Grupo')
            print(pos(2,25)+'')
            des = input('Descripcion.........:'+pos(3,25))
            arch = Archivo()
            gru = Grupo(des)
            if path.isfile('data/grupo.txt'):
                datos = arch.leer('data/grupo.txt')
                gru.id = generarCodigoAutomatico(datos)
            arch.escribir('data/grupo.txt',gru.mostrarGrupo())
            x = input('Registro Grabado, Precione una tecla para continuar...')

        elif opc == '2':
            print(pos(1,15)+'Listado de Grupos')
            arch = Archivo()
            datos = arch.leer('data/grupo.txt')
            tabla=[]
            tabla.append(['Codigo','Descripcion'])
        
            for dato in datos:
                #tabla.append(['\x1b[0;34m'+dato[0],'\x1b[0;34m'+dato[1],'\x1b[0;34m'+dato[2],'\x1b[0;34m'+dato[3],'\x1b[0;34m'+dato[4],'\x1b[0;34m'+dato[5]])
                tabla.append([dato[0],dato[1]])
            printTable(tabla, useFieldNames=True,color=(26, 156, 171))
            x = input('\x1b[0;37m'+'Registro Grabado, Precione una tecla para continuar...')
        system('cls')
        opc = men.mostrarMenu()