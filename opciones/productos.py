from clases.producto import Producto
from utileria.archivo import Archivo
from utileria.funciones import gotoxy,buscarRegistro,getIva,generarCodigoAutomatico
from utileria.menu import  Menu
from utileria.TableIT import printTable
from os import system, path
import time
def productos():
    system('cls')
    men = Menu(['1).Ingreso','2).Listado','3).Salir'],'     Menu Producto')
    opc = men.mostrarMenu()
    while opc != '3':
        system('cls')
        if opc == '1':
            arch =  Archivo()
            gotoxy(25,0);print('Ingreso Producto')
            
            gotoxy(1,2);print('Nombre......:')
            gotoxy(1,3);print('Grupo.......:')
            gotoxy(1,4);print('Marca.......:')
            gotoxy(1,5);print('Precio......:')
            gotoxy(1,6);print('Stock.......:')


            gotoxy(16,2);nombre = input()
            gotoxy(16,3);grupo = input()
            grupos = arch.leer('data/grupo.txt')
            registro = buscarRegistro(grupos,grupo)
            if registro: gotoxy(16,3);print(registro[1])
            else: 
                gotoxy(16,3);print('Sin Grupo')
                grupo=0
            gotoxy(16,4);marca = input()
            marcas = arch.leer('data/marca.txt')
            registro = buscarRegistro(marcas,marca)
            if registro: gotoxy(16,4);print(registro[1])
            else: 
                gotoxy(16,4);print('Sin Marca')
                marca=0
            gotoxy(16,5);precio = input()
            gotoxy(16,6);stock = input()
            prod = Producto(nombre,precio,stock,marca,grupo)
            arch = Archivo()
            print(prod.id)
            if path.isfile('data/producto.txt'):
                datos = arch.leer('data/producto.txt')
                prod.id = generarCodigoAutomatico(datos)
    
            arch.escribir('data/producto.txt',prod.mostrarProducto())
            gotoxy(1,8);x = input('Registro Grabado, Precione una tecla para continuar...')
            gotoxy(1,9);print(prod.id)
            gotoxy(1,10);print(prod._siguiente)
        elif opc == '2':
            gotoxy(1,15);print('Listado Productos')
            arch = Archivo()
            datos = arch.leer('data/producto.txt')
            tabla=[]
            tabla.append(['Id','Nombre','Precio','Stock','Marca','Grupo'])
            marcas = arch.leer('data/marca.txt')
            grupos = arch.leer('data/grupo.txt')
            for dato in datos:
                #tabla.append(['\x1b[0;34m'+dato[0],'\x1b[0;34m'+dato[1],'\x1b[0;34m'+dato[2],'\x1b[0;34m'+dato[3],'\x1b[0;34m'+dato[4],'\x1b[0;34m'+dato[5]])
                grp = buscarRegistro(marcas ,dato[4])
                mar = buscarRegistro(grupos ,dato[5])
                if not grp:
                    grp = 'Sin Grupo'
                else: 
                    grp= grp[1]
                if not mar:
                    mar = 'Sin Marca'
                else:
                    mar= mar[1]
                tabla.append([dato[0],dato[1],dato[2],dato[3],grp,mar])
            printTable(tabla, useFieldNames=True,color=(26, 156, 171))
            x = input('\x1b[0;37m'+'Registro Grabado, Precione una tecla para continuar...')
        system('cls')
        opc = men.mostrarMenu()