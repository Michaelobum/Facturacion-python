from clases.compra import Compra
from clases.detcompra import DetCompra
from utileria.funciones import gotoxy,buscarRegistro,getIva,generarCodigoAutomatico
from utileria.menu import Menu
from utileria.archivo import Archivo
from utileria.TableIT import printTable
from os import system,path
from datetime import date

def grabarCompra(fac,fec,prov,sub,iva,tot,detalles):
    try:
        venta = Compra(fac,fec,prov,sub,iva,tot)
        arch = Archivo()
        arch.escribir('data/compras.txt',venta.mostrarVenta())
        for detalle in detalles:
            det = DetCompra(detalle['ord'],detalle['producto'],detalle['costo'],detalle['cantidad'])
            if path.isfile('data/detcompras.txt'):
                datos = arch.leer('data/detcompras.txt')
                det.id= generarCodigoAutomatico(datos,1)
            arch.escribir('data/detcompras.txt',det.mostrarDetalle())
        mensaje = 'Venta Exitosa; Enter Para continuar'
    except Exception as e :
        mensaje = ['Error en La Ventana; Intenta de nuevamente ',e]
    finally:
        return mensaje
    
def compras():
    system('cls')
    men = Menu(['1).Ingreso','2).Listado','3).Reimprimir Factura','4).Salir'],'     Menu Compras')
    opc = men.mostrarMenu()
    while opc != '4':
        system('cls')
        if opc == '1':
            gotoxy(1,1);print('***************** Sistema de Compra - RegSri:#0001 ********')
            gotoxy(1,2);print('Orden....:')
            gotoxy(1,3);print('Fecha....:')
            gotoxy(13,3);print(str(date.today()))
            gotoxy(1,4);print('Proveedor.:')
            gotoxy(33,2);print('SubTotal.:')
            gotoxy(33,3);print('Iva......:')
            gotoxy(33,4);print('Total....:')
            arch = Archivo()
            fac =1
            if path.isfile('data/compras.txt'):
                datos = arch.leer('data/compras.txt')
                fac= generarCodigoAutomatico(datos)
            gotoxy(13,2);print(fac)
            gotoxy(13,3);fec = input()
            gotoxy(13,4);prov = input()
            
            proveedores =  arch.leer('data/proveedor_lote.txt')+arch.leer('data/proveedor_mayor.txt')
            registro = buscarRegistro(proveedores,prov)
            if registro:
                if len(prov) > len(registro[1]):
                    l =len(prov) -len(registro[1])
                    gotoxy(13+len(registro[1]),4);print(' '*l)
                gotoxy(13,4);print(registro[1])
            else: gotoxy(13,4);print('Sin Proveedor')
            if not fec:fec = date.today()
            gotoxy(1,5);print('**************************************************************')
            gotoxy(1,6);print('Producto')
            gotoxy(10,6);print('Descripcion')
            gotoxy(35,6);print('Costo')
            gotoxy(45,6);print('Cantidad')
            gotoxy(55,6);print('SubTotal')
            codproducto,subCab,totCab,ivaCab,linea ='',0,0,0,7
            detalle = []
            while codproducto not in('s','S'):
                gotoxy(1,linea);codproducto = input()
                arch = Archivo()
                productos = arch.leer('data/producto.txt')
                registro = buscarRegistro(productos,codproducto)
                if registro:
                    precio = float(registro[2])
                    l = len('No existe Registro') -len(registro[1])
                    gotoxy(10+len(registro[1]),linea);print(' '*l)
                    gotoxy(10,linea);print(registro[1])
                    gotoxy(35,linea);print(precio)
                    gotoxy(45,linea);cant = int(input())
                    subDet = round(cant*precio,2)
                    gotoxy(55,linea);print(subDet)
                    subCab += subDet
                    ivaCab = round(subCab*getIva(),2)
                    totCab = subCab +ivaCab
                    gotoxy(45,2);print(subCab)
                    gotoxy(45,3);print(ivaCab)
                    gotoxy(45,4);print(totCab)
                    detalle.append({'ord':fac,'producto':codproducto,'costo':precio,'cantidad':cant})
                elif codproducto not in('s','S'):                        
                    gotoxy(10,linea);print('No existe Registro')
                    linea -= 1
                    
                linea+= 1
            grabar = grabarCompra(fac,fec,prov,subCab,ivaCab,totCab,detalle)
            print(grabar)
            x = input('Registro Grabado, Precione una tecla para continuar...')

        elif opc == '2':
            gotoxy(1,15);print('Listado Compras')
            arch = Archivo()
            datos = arch.leer('data/compras.txt')
            tabla=[]
            tabla.append(['Orden','Fecha','Proveedor','Subtotal','Iva','Total'])
            proveedores = arch.leer('data/proveedor_lote.txt')+arch.leer('data/proveedor_mayor.txt')
            for dato in datos:
                #tabla.append(['\x1b[0;34m'+dato[0],'\x1b[0;34m'+dato[1],'\x1b[0;34m'+dato[2],'\x1b[0;34m'+dato[3],'\x1b[0;34m'+dato[4],'\x1b[0;34m'+dato[5]])
                proveedor = buscarRegistro(proveedores ,dato[2])
                tabla.append([dato[0],dato[1],proveedor[1] if proveedor else 'Sin Proveedor' ,dato[3],dato[4],dato[4]])
            printTable(tabla, useFieldNames=True,color=(26, 156, 171))
            x = input('\x1b[0;37m'+'Registro Grabado, Precione una tecla para continuar...')

        elif opc == '3':

            gotoxy(0,0);print('Reimprimir Orden Compra')
            gotoxy(0,2);print('Buscar Orden..:')
            gotoxy(22,2);bus = input()
            arch = Archivo()
            comps= arch.leer('data/compras.txt')
            compra = buscarRegistro(comps,bus)
            if compra:    
                proveedores =  arch.leer('data/proveedor_lote.txt')+arch.leer('data/proveedor_mayor.txt')
                proveedor = buscarRegistro(proveedores,compra[2])
                
                gotoxy(1,1);print('***************** Orden de Compra - RegSri:#0001 ******')
                gotoxy(1,2);print('Factura...: {}'.format(compra[0]))
                gotoxy(1,3);print('Fecha.....: {}'.format(compra[1]))
                gotoxy(1,4);print('Proveedor.: {}'.format(proveedor[1]if proveedor else 'Sin Proveedor'))
                gotoxy(33,2);print('SubTotal.: {}'.format(compra[3]))
                gotoxy(33,3);print('Iva......: {}'.format(compra[4]))
                gotoxy(33,4);print('Total....: {}'.format(compra[5]))


                gotoxy(1,5);print('**************************************************************')
                gotoxy(1,6);print('Producto')
                gotoxy(10,6);print('Descripcion')
                gotoxy(35,6);print('Costo')
                gotoxy(45,6);print('Cantidad')
                gotoxy(55,6);print('SubTotal')
                datos = arch.leer('data/detcompras.txt')
                linea=7
                for d in datos:
                    if d[0] == compra[0]:
                        productos = arch.leer('data/producto.txt')
                        producto = buscarRegistro(productos,d[2])
                        gotoxy(10,linea);print(producto[1])
                        gotoxy(35,linea);print(d[3])
                        gotoxy(45,linea);print(d[4])
                        gotoxy(55,linea);print(float(d[3])*float(d[3]))
                        linea+=1
                gotoxy(0,linea+2);x=input('Precione una tecla para continuar...')
            else :
                gotoxy(0,3);print('No existe Orden Compra {}'.format(bus))
                gotoxy(0,5);x=input('Precione una tecla para continuar...')
        system('cls')
        opc = men.mostrarMenu()
    
    