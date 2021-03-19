from utileria.menu import  Menu
from os import system 
#opciones
from opciones.proveedor_lote import proveedorLote
from opciones.proveedor_x_mayor import proveedorMayor
from opciones.grupos import grupos
from opciones.marcas import marcas
from opciones.clientes import clientes
from opciones.productos import productos
from opciones.ventas import ventas
from opciones.compras import compras


men = Menu(['1).Grupos','2).Marcas','3).Producto','4).Proveedor Lote','5).Proveedor x Mayor','6).Clientes',
'7).Ventas','8).Compras','9).Salir'],'     Menu Facturacion')
system('cls')
opc = men.mostrarMenu()
while opc != '9':
    if opc == '1':grupos()
    elif opc == '2':marcas()
    elif opc == '3':productos()
    elif opc == '4':proveedorLote()
    elif opc == '5':proveedorMayor()
    elif opc == '6':clientes()
    elif opc == '7':ventas()
    elif opc == '8':compras()
    system('cls')
    opc = men.mostrarMenu()