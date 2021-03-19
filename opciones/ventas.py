from clases.venta import Venta
from clases.detventa import DetVenta
from utileria.funciones import gotoxy,buscarRegistro,getIva,generarCodigoAutomatico
from utileria.menu import Menu
from utileria.archivo import Archivo
from utileria.TableIT import printTable
from os import system,path
from datetime import date

def grabarVenta(fac,fec,cli,sub,iva,tot,detalles):
    try:
        venta = Venta(fac,fec,cli,sub,iva,tot)
        arch = Archivo()
        arch.escribir('data/ventas.txt',venta.mostrarVenta())
        for detalle in detalles:
            det = DetVenta(detalle['fac'],detalle['producto'],detalle['precio'],detalle['cantidad'])
            if path.isfile('data/detventas.txt'):
                datos = arch.leer('data/detventas.txt')
                det.id= generarCodigoAutomatico(datos,1)
            arch.escribir('data/detventas.txt',det.mostrarDetalle())
        mensaje = 'Venta Exitosa; Enter Para continuar'
    except Exception as e :
        mensaje = ['Error en La Ventana; Intenta de nuevamente ',e]
    finally:
        return mensaje
    
def ventas():
    system('cls')
    men = Menu(['1).Ingreso','2).Listado','3).Reimprimir Factura','4).Salir'],'     Menu Ventas')
    opc = men.mostrarMenu()
    while opc != '4':
        system('cls')
        if opc == '1':
            gotoxy(1,1);print('***************** Sistema de Facturacion - RegSri:#0001 ******')
            gotoxy(1,2);print('Factura..:')
            gotoxy(1,3);print('Fecha....:')
            gotoxy(13,3);print(str(date.today()))
            gotoxy(1,4);print('Cliente..:')
            gotoxy(33,2);print('SubTotal.:')
            gotoxy(33,3);print('Iva......:')
            gotoxy(33,4);print('Total....:')
            arch = Archivo()
            fac =1
            if path.isfile('data/ventas.txt'):
                datos = arch.leer('data/ventas.txt')
                fac= generarCodigoAutomatico(datos)
            gotoxy(13,2);print(fac)
            gotoxy(13,3);fec = input()
            gotoxy(13,4);cli = input()
            
            clientes = arch.leer('data/cliente.txt')
            registro = buscarRegistro(clientes,cli)
            if registro:
                if len(cli) > len(registro[1]):
                    l =len(cli) -len(registro[1])
                    gotoxy(13+len(registro[1]),4);print(' '*l)
                gotoxy(13,4);print(registro[1])
            else: gotoxy(13,4);print('Consumidor Final')
            if not fec:fec = date.today()
            gotoxy(1,5);print('**************************************************************')
            gotoxy(1,6);print('Producto')
            gotoxy(10,6);print('Descripcion')
            gotoxy(35,6);print('Precio')
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
                    detalle.append({'fac':fac,'producto':codproducto,'precio':precio,'cantidad':cant})
                elif codproducto not in('s','S'):
                    # '                            
                    gotoxy(10,linea);print('No existe Registro')
                    
                    linea -= 1
                    
                linea+= 1
            grabar = grabarVenta(fac,fec,cli,subCab,ivaCab,totCab,detalle)
            print(grabar)
            x = input('Registro Grabado, Precione una tecla para continuar...')

        elif opc == '2':
            gotoxy(1,15);print('Listado Ventas')
            arch = Archivo()
            datos = arch.leer('data/ventas.txt')
            tabla=[]
            tabla.append(['Factura','Fecha','Cliente','Subtotal','Iva','Total'])
            clientes = arch.leer('data/cliente.txt')
            for dato in datos:
                #tabla.append(['\x1b[0;34m'+dato[0],'\x1b[0;34m'+dato[1],'\x1b[0;34m'+dato[2],'\x1b[0;34m'+dato[3],'\x1b[0;34m'+dato[4],'\x1b[0;34m'+dato[5]])
                cliente = buscarRegistro(clientes ,dato[2])
                cl =cliente[1] if cliente else 'Consumidor Final' 
                tabla.append([dato[0],dato[1],cl,dato[3],dato[4],dato[4]])
            printTable(tabla, useFieldNames=True,color=(26, 156, 171))
            x = input('\x1b[0;37m'+'Registro Grabado, Precione una tecla para continuar...')

        elif opc == '3':
            gotoxy(0,0);print('Reimprimir Factura')
            gotoxy(0,2);print('Buscar Factura..:')
            gotoxy(22,2);bus = input()
            arch = Archivo()
            vents= arch.leer('data/ventas.txt')
            venta = buscarRegistro(vents,bus)
            if venta:
                clientes = arch.leer('data/cliente.txt')
                cliente = buscarRegistro(clientes,venta[2])
                
                gotoxy(1,1);print('***************** Factura - RegSri:#0001 ******')
                gotoxy(1,2);print('Factura...: {}'.format(venta[0]))
                gotoxy(1,3);print('Fecha.....: {}'.format(venta[1]))
                gotoxy(1,4);print('Cliente...: {}'.format(cliente[1] if cliente else'Consumidor Final'))
                gotoxy(33,2);print('SubTotal.: {}'.format(venta[3]))
                gotoxy(33,3);print('Iva......: {}'.format(venta[4]))
                gotoxy(33,4);print('Total....: {}'.format(venta[5]))


                gotoxy(1,5);print('**************************************************************')
                gotoxy(1,6);print('Producto')
                gotoxy(10,6);print('Descripcion')
                gotoxy(35,6);print('Precio')
                gotoxy(45,6);print('Cantidad')
                gotoxy(55,6);print('SubTotal')
                datos = arch.leer('data/detventas.txt')
                linea=7
                for d in datos:
                    if d[0] == venta[0]:
                        productos = arch.leer('data/producto.txt')
                        producto = buscarRegistro(productos,d[2])
                        gotoxy(10,linea);print(producto[1])
                        gotoxy(35,linea);print(d[3])
                        gotoxy(45,linea);print(d[4])
                        gotoxy(55,linea);print(float(d[3])*float(d[3]))
                        linea+=1
                gotoxy(0,linea);x=input('Registro Grabado, Precione una tecla para continuar...')
            else :
                gotoxy(0,3);print('No existe Factura {}'.format(bus))
                gotoxy(0,5);x=input('Registro Grabado, Precione una tecla para continuar...')
        system('cls')
        opc = men.mostrarMenu()
    
    