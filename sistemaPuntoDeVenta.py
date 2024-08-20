# Paso 1: Definir el Menú Principal
def mostrar_menu():
    print("Bienvenido al sistema de Punto de Venta")
    print("1. Agregar producto al carrito")
    print("2. Ver total del carrito")
    print("3. Pagar")
    print("4. Salir")
    print("5. Eliminar un producto del carrito")  # Nueva opción añadida

# Paso 2: Variables Globales
carrito = []
total = 0.0

# Paso 3: Función para Agregar Productos
def agregar_producto():
    global total  # Accedemos a la variable global 'total'
    producto = input("Ingresa el nombre del producto: ")
    precio = float(input("Ingresa el precio del producto: "))
    carrito.append({"producto": producto, "precio": precio})
    total += precio
    print(f"Has agregado {producto} al carrito por {precio}.")

# Paso 4: Función para Ver el Total
def ver_total():
    print(f"El total de tu carrito es: {total:.2f}.")

# Paso 5: Función para Pagar
def pagar():
    global total, carrito  # Accedemos a las variables globales 'total' y 'carrito'
    if total == 0:
        print("Tu carrito está vacío, no hay nada que pagar.")
    else:
        print(f"Tu total a pagar es: {total:.2f}")
        pago = float(input("Ingresa la cantidad con la que vas a pagar: "))
        if pago >= total:
            cambio = pago - total
            print(f"Pago realizado con éxito. Tu cambio es {cambio:.2f}.")
            # Reiniciar el carrito y el total después del pago
            carrito = []
            total = 0.0
        else:
            print("No tienes suficiente dinero para pagar.")

# Función para Eliminar un Producto (Paso añadido)
def eliminar_producto():
    global total  # Accedemos a la variable global 'total'
    if not carrito:
        print("El carrito está vacío. No hay productos para eliminar.")
        return

    print("Productos en tu carrito:")
    for i, item in enumerate(carrito, start=1):
        print(f"{i}. {item['producto']} - ${item['precio']:.2f}")

    try:
        indice = int(input("Ingresa el número del producto que deseas eliminar: "))
        if 1 <= indice <= len(carrito):
            producto_eliminado = carrito.pop(indice - 1)  # Eliminamos el producto
            total -= producto_eliminado['precio']  # Restamos el precio del total
            print(f"Has eliminado {producto_eliminado['producto']} del carrito.")
        else:
            print("Número inválido. Por favor, intenta de nuevo.")
    except ValueError:
        print("Por favor, ingresa un número válido.")

# Paso 6: Ejecutar el Programa
def ejecutar():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            ver_total()
        elif opcion == "3":
            pagar()
        elif opcion == "4":
            print("Gracias por usar el sistema. ¡Hasta luego!")
            break
        elif opcion == "5":
            eliminar_producto()  # Llamamos a la nueva función para eliminar producto
        else:
            print("Opción no válida, por favor intenta de nuevo.")

# Ejecutar el programa
ejecutar()
