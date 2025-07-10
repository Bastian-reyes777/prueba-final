from Funciones import *

####################################################################################################

while True:
    try:
        print("""
            *** MENU PRINCIPAL ***
            1. Stock marca.
            2. Búsqueda por precio.
            3. Actualizar precio.
            4. Salir.      """)

####################################################################################################

        opcion = int(input("Ingrese opción"))

        match opcion:
            case 1:
                marca = input("Ingrese marca a consultar : ")
                codigo = input("Ingrese codigo del producto : ")
                stock_marca(marca)

            case 2:
                codigo = input("Ingrese modelo a actualizar : ")
                preciomax = int(input("ingrese precio max : "))
                preciomin = int(input("ingrese precio min : "))
                buscar_por_precio()

            case 3:
                modelo = input("Ingrese modelo a actualizar :")
                precio_nuevo = int(input("Ingrese precio nuevo :"))
                actualizar_precio()

            case 4:
                print("Programa finalizado.")
                print("Se despide (Origamista)")
                break

    except:
        print("error")

####################################################################################################
