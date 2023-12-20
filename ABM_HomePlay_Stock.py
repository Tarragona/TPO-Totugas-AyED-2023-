# Precondiciones y Postcondiciones para la función leer_archivo:

# Precondiciones:
# 1. El archivo especificado por 'nombre_archivo' debe existir en el mismo directorio que el script.
# 2. El formato del archivo debe ser CSV y contener datos organizados con las columnas 'Plataforma', 'Titulo', 'Stock', y 'Precio'.
# 3. Cada fila en el archivo debe representar una entrada de juego con valores correspondientes para cada columna.
# 4. El archivo debe estar codificado en UTF-8.

# Postcondiciones:
# 1. Si la lectura del archivo es exitosa, la función devuelve una lista de diccionarios que representan los datos del juego.
# 2. Si hay algún error al leer el archivo, se imprime un mensaje de error y la función devuelve None.

def leer_archivo(nombre_archivo: str):
    try:
        with open (nombre_archivo + '.csv', 'rt', encoding='utf-8') as archivo:
            datos = [linea.strip().split(';') for linea in archivo] 
            columnas = datos[0]
            datos = [dict(zip(columnas, fila)) for fila in datos[1:]] 
        return datos
    except Exception as msg:
        print(f"Error al leer el archivo: {msg}")
        return None

#-------------------------------------------------------------------------------------------------------------------------------------------------
# Precondiciones y Postcondiciones para la función plataforma_seleccionada:

# Precondiciones:
# 1. El archivo pasado como parámetro a la función debe existir.

# Postcondiciones:
# 1. Si el archivo no es None, la función imprime las plataformas disponibles y solicita al usuario seleccionar una.
# 2. Si la selección es válida, la función devuelve la plataforma seleccionada.
# 3. Si la selección no es válida o el archivo es None, se imprime un mensaje indicando que no existe la plataforma y la función devuelve None.

def plataforma_seleccionada(archivo: dict[str, str]):
    print('\nPlataformas: ')
    if archivo is not None:
        try:
            #Para validar que la plataforma ingresada exista
            plataformas = sorted(set(fila['Plataforma'] for fila in archivo))
            separadas = '|'.join([f"{i+1}- {plataforma}" for i, plataforma in enumerate(plataformas)])
            print(separadas)
            opcion = int(input('\nIngrese el numero de la plataforma: '))
            print(f"Plataforma Elegida: {plataformas[opcion-1]}")
            return list(plataformas)[opcion-1]
        except:
            print(f"\nNo existe la plataforma")
    else:
        return None

#-------------------------------------------------------------------------------------------------------------------------------------------------
# Precondiciones y Postcondiciones para la función seleccionar_juego:

# Precondiciones:
# 1. La variable 'archivo' debe contener datos válidos.

# Postcondiciones:
# 1. La función muestra en consola los juegos disponibles y permite al usuario seleccionar uno.
# 2. Si la selección es válida, devuelve el juego seleccionado.
# 3. Si la selección es 0, devuelve None indicando cancelación.
# 4. Si la selección no es válida, imprime un mensaje correspondiente y solicita otra selección.

def seleccionar_juego(archivo: list[dict[str, str]]):
    print()
    print("Juegos disponibles:")
    for i, juego in enumerate(archivo, start=1):
        print(f"{i}. {juego['Titulo']} | Stock: {juego['Stock']} | Precio: {juego['Precio']}")
    
    while True:
        try:
            print()
            opcion = int(input("Seleccione el número del juego (0 para cancelar): "))
            if opcion == 0:
                return None
            elif 1 <= opcion <= len(archivo):
                return archivo[opcion - 1]
            else:
                print("Opción inválida. Intente de nuevo.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

#-------------------------------------------------------------------------------------------------------------------------------------------------
# Precondiciones y Postcondiciones para la función guardar_venta:

# Precondiciones:
# 1. La variable 'juego', 'cantidad', y 'p_final' deben contener datos válidos.

# Postcondiciones:
# 1. La función guarda la información de la venta en 'HomePlay_Ventas.csv'.
# 2. Si la operación es exitosa, imprime un mensaje indicando que la venta se guardó correctamente.
# 3. Si hay algún error al guardar la venta, se imprime un mensaje correspondiente.

def guardar_venta(juego: dict[str, str], cantidad: int, p_final: str): #Guardar la venta en un archivo
    #titulos = (';'.join(archivo[0])+ '\n') (otra forma de usar los encabezados pero cambiando el titulo de 'Cantidad' por 'Stock' ya que los trae del archivo original)
    try:
        with open('HomePlay_Ventas.csv', 'a', newline='', encoding='utf-8') as archivo_ex:
            archivo_ex.writelines(f"Plataforma;Titulo;Cantidad;Precio Final(USD)" + '\n') #y si quiero usar 'titulos', seria "archivo_ex.writelines(titulos)"
            archivo_ex.write(f"{juego['Plataforma']};{juego['Titulo']};{cantidad};{p_final}\n\n")
            print("Venta guardada en el archivo.")
    except Exception as msg:
        print(f"Error al guardar la venta: {msg}")

#------------------------------------------------------------------------------------------------------------------------------------------------- Opcion 1
# Precondiciones y Postcondiciones para la función mostrar_todo:

# Precondiciones:
# 1. La variable 'archivo' debe contener datos válidos.

# Postcondiciones:
# 1. La función imprime en consola la información de todos los juegos en el archivo.

#Opcion 1
def mostrar_todo(archivo: list[dict[str, str]]):
    for juego in archivo:
        print(f"\n| {juego['Plataforma']} | {juego['Titulo']} | {juego['Stock']} | {juego['Precio']} |")
    return

#------------------------------------------------------------------------------------------------------------------------------------------------- Opcion 2
# Precondiciones y Postcondiciones para la función listar_plataformas:

# Precondiciones:
# 1. La variable 'archivo' debe contener datos válidos.
# 2. La variable 'plataforma' debe ser una plataforma válida presente en el archivo.

# Postcondiciones:
# 1. La función imprime en consola la información de todos los juegos de la plataforma seleccionada.
# 2. La función devuelve una lista de juegos de la plataforma seleccionada.

#Opcion 2
def listar_plataformas(archivo: dict[str, str], plataforma: list[dict[str, str]]):
    juegos = [fila for fila in archivo if plataforma == fila['Plataforma']] #Si la plataforma elegida se encuentra dentro del archivo -->
    
    for juego in juegos:
        print(f"\n| {juego['Plataforma']} | {juego['Titulo']} | {juego['Stock']} | {juego['Precio']} |")
    return juegos

#------------------------------------------------------------------------------------------------------------------------------------------------- Opcion 3
# Precondiciones y Postcondiciones para la función venta:

# Precondiciones:
# 1. La variable 'archivo' debe contener datos válidos.

# Postcondiciones:
# 1. La función realiza el proceso de venta, actualizando el stock y guardando la venta en 'HomePlay_Ventas.csv'.
# 2. Si la venta es exitosa, imprime un mensaje indicando que la venta se realizó.
# 3. Si hay un error o el stock es insuficiente, se imprime el mensaje correspondiente.

#Opcion 3
def venta(archivo: list[dict[str, str]]):
    plataforma = plataforma_seleccionada(archivo)
    if plataforma is not None:
        juegos = listar_plataformas(archivo, plataforma)
        juego_seleccionado = seleccionar_juego(juegos)
        
        if juego_seleccionado is not None:
            cant_vendida = int(input("Ingrese la cantidad a vender: "))
            if cant_vendida > 0 and int(juego_seleccionado['Stock']) > cant_vendida:
                juego_seleccionado['Stock'] = str(int(juego_seleccionado['Stock'])-cant_vendida)
                precio_final = str(int(juego_seleccionado['Precio'])*cant_vendida)
                guardar_venta(juego_seleccionado, cant_vendida, precio_final)
                print("Venta realizada.")
            else:
                print("Stock insuficiente.")

#------------------------------------------------------------------------------------------------------------------------------------------------- Opcion 4
# Precondiciones y Postcondiciones para la función agregar_juego:

# Precondiciones:
# 1. La variable 'nombre_archivo' debe contener un nombre de archivo válido.
# 2. La variable 'archivo' debe contener datos válidos.

# Postcondiciones:
# 1. La función agrega un nuevo juego al archivo y muestra un mensaje indicando que la operación se realizó con éxito.
# 2. Si hay algún error al modificar el archivo, se imprime un mensaje correspondiente.

#Opcion 4
def agregar_juego(nombre_archivo: str, archivo: list[dict[str, str]]):
    plataforma = plataforma_seleccionada(archivo)
    if plataforma is not None:
        juego = input("Ingresar Titulo: ")
        stock = int(input("Ingresar Stock: "))
        precio = int(input("Ingresar Precio(USD): "))
        agregar = {"Plataforma": plataforma, "Titulo": juego, "Stock": stock, "Precio": precio}
    try:
        with open(nombre_archivo + '.csv', "a", encoding = "utf-8") as arch:
            arch.write(f"{agregar['Plataforma']};{agregar['Titulo']};{agregar['Stock']};{agregar['Precio']}\n")
            print(f"El juego ({agregar['Titulo']}) fue agregado exitosamente al archivo")
    except:
        print("No se pudo modificar el archivo")

#------------------------------------------------------------------------------------------------------------------------------------------------- Opcion 5
# Precondiciones y Postcondiciones para la función eliminar_juego:

# Precondiciones:
# 1. La variable 'nombre_archivo' debe contener un nombre de archivo válido.
# 2. La variable 'archivo' debe contener datos válidos.

# Postcondiciones:
# 1. La función elimina un juego seleccionado del archivo y muestra un mensaje indicando que la operación se realizó con éxito.
# 2. Si hay algún error al modificar el archivo, se imprime un mensaje correspondiente.

#Opcion 5
def eliminar_juego(nombre_archivo: str, archivo: list[dict[str, str]]):
    plataforma = plataforma_seleccionada(archivo)
    if plataforma is not None:
        juegos = listar_plataformas(archivo, plataforma)
        juego_seleccionado = seleccionar_juego(juegos)
        
        if juego_seleccionado is not None:
            archivo.remove(juego_seleccionado)
            titulos = (';'.join(archivo[0])+ '\n')
            try: #Una vez que remuevo el juego seleccionado del archivo original, sobreescribo ese archivo original con los datos sin ese juego
                with open(nombre_archivo + '.csv', 'w', newline='', encoding='utf-8') as archivo_ex:
                    archivo_ex.writelines(titulos)
                    
                    for juego in archivo:
                        archivo_ex.write(f"{juego['Plataforma']};{juego['Titulo']};{juego['Stock']};{juego['Precio']}\n")
                        
                    print(f"El juego ({juego_seleccionado['Titulo']}) fue eliminado del archivo.")
            except Exception as msg:
                print(f"Error al eliminar del archivo: {msg}")

#------------------------------------------------------------------------------------------------------------------------------------------------- Opcion 6 
# Precondiciones y Postcondiciones para la función modificar_juego:

# Precondiciones:
# 1. La variable 'nombre_archivo' debe contener un nombre de archivo válido.
# 2. La variable 'archivo' debe contener datos válidos.

# Postcondiciones:
# 1. La función permite al usuario seleccionar un juego, modificar su stock y precio, y guarda los cambios en el archivo.
# 2. Si la modificación es exitosa, imprime un mensaje indicando que el juego se modificó correctamente.
# 3. Si hay algún error al modificar el juego, se imprime un mensaje correspondiente.

#Opcion 6 
def modificar_juego(nombre_archivo, archivo):
    plataforma = plataforma_seleccionada(archivo)
    if plataforma is not None:
        juegos = listar_plataformas(archivo, plataforma)
        juego_seleccionado = seleccionar_juego(juegos)
        
        if juego_seleccionado is not None:
            print(f"\nDatos actuales del juego:")
            print(f"Titulo: {juego_seleccionado['Titulo']}")
            print(f"Stock: {juego_seleccionado['Stock']}")
            print(f"Precio: {juego_seleccionado['Precio']}")
            
            nuevo_stock = int(input("Ingrese el nuevo stock: "))
            nuevo_precio = int(input("Ingrese el nuevo precio (USD): ")) # Solicita al usuario ingresar el nuevo stock y precio del juego
            
            juego_seleccionado['Stock'] = str(nuevo_stock)
            juego_seleccionado['Precio'] = str(nuevo_precio)# Actualiza el stock y precio del juego seleccionado
            
            titulos = (';'.join(archivo[0]) + '\n')
            
            try:# Abre el archivo en modo escritura
                with open(nombre_archivo + '.csv', 'w', newline='', encoding='utf-8') as archivo_ex:
                    archivo_ex.writelines(titulos)
                    
                    for juego in archivo:
                        archivo_ex.write(f"{juego['Plataforma']};{juego['Titulo']};{juego['Stock']};{juego['Precio']}\n")
                    
                    print(f"El juego ({juego_seleccionado['Titulo']}) fue modificado exitosamente.")
            except Exception as msg:
                print(f"Error al modificar el juego en el archivo: {msg}")

#-------------------------------------------------------------------------------------------------------------------------------------------------
# Precondiciones y Postcondiciones para la función menu:

# Precondiciones:
# 1. No hay precondiciones específicas.

# Postcondiciones:
# 1. La función imprime en consola el menú con las opciones disponibles.

def menu():
    op = {"1": "Mostrar todos los Juegos",
          "2": "Mostrar juegos por plataforma",
          "3": "Venta",
          "4": "Agregar juego",
          "5": "Eliminar juego",
          "6": "Modificar juego",
          "0": "Salir"}
    for x, i in op.items():
        print(f"{x}- {i}")
    return

#-------------------------------------------------------------------------------------------------------------------------------------------------
# Precondiciones y Postcondiciones para la función main:

# Precondiciones:
# 1. La variable 'nombre_archivo' debe contener un nombre de archivo válido.

# Postcondiciones:
# 1. La función ejecuta el menú principal del programa y permite al usuario interactuar con las opciones disponibles.

def main():
    nombre_archivo = 'HomePlay_Stock'
    archivo = leer_archivo(nombre_archivo)
    while True:
        menu()
        opcion = input("Ingrese la opcion: ")
        if opcion == '1':
            mostrar_todo(archivo)
            print()
        elif opcion == '2':
            plataforma = plataforma_seleccionada(archivo)
            listar_plataformas(archivo, plataforma)
            print()
        elif opcion == '3':
            venta(archivo)
            print()
        elif opcion == '4':
            agregar_juego(nombre_archivo, archivo)
            print()
        elif opcion == '5':
            eliminar_juego(nombre_archivo, archivo)
            print()
        elif opcion == '6':
            break
        elif opcion == '0':
            print('\nSaliendo del programa...')
            break


if __name__ == "__main__":
    main()
