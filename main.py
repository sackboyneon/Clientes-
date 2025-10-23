import os
from datetime import datetime

#Simulación de usuarios del equipo
usuarios = {
    "AnaDev": "Desarrolladora principal",
    "LuisOps": "Encargado de automatización"
}

#carpeta donde se guardan los archivos de clientes
CLIENTES_DIR = "clientes"
os.makedirs(CLIENTES_DIR, exist_ok=True)

#tabla hash para asociar nombre con archivo
clientes = {}

#cargar clientes existentes al iniciar
for archivo in os.listdir(CLIENTES_DIR):
    if archivo.endswith(".txt"):
        nombre = archivo.replace(".txt", "")
        clientes[nombre] = os.path.join(CLIENTES_DIR, archivo)

#menú de opciones
def menu():
    print("\n--- Gestión de Clientes Axanet ---")
    print("1. Crear nuevo cliente")
    print("2. Consultar cliente")
    print("3. Modificar cliente")
    print("4. Borrar cliente")
    print("5. Salir")

#crear cliente
def crear_cliente():
    nombre = input("Nombre del cliente: ")
    if nombre in clientes:
        print("El cliente ya existe.")
        return
    servicio = input("Descripción del servicio: ")
    ruta = os.path.join(CLIENTES_DIR, f"{nombre}.txt")
    with open(ruta, "w") as f:
        f.write(f"Cliente: {nombre}\n")
        f.write(f"Fecha de registro: {datetime.now()}\n")
        f.write("Servicios:\n")
        f.write(f"- {servicio}\n")
    clientes[nombre] = ruta
    print("Cliente creado exitosamente.")
    notificar_equipo("Se ha creado un nuevo cliente.")

#consultar cliente
def consultar_cliente():
    nombre = input("Nombre del cliente: ")
    if nombre not in clientes:
        print("Cliente no encontrado.")
        return
    with open(clientes[nombre], "r") as f:
        print(f.read())
    notificar_equipo("se ha consultado la información de un cliente.")

#modificar cliente
def modificar_cliente():
    nombre = input("Nombre del cliente: ")
    if nombre not in clientes:
        print(" Cliente no encontrado.")
        return
    servicio = input("Nueva descripción del servicio: ")
    with open(clientes[nombre], "a") as f:
        f.write(f"- {servicio}\n")
    print(" Servicio agregado.")
    notificar_equipo("Se ha actualizado un cliente existente.")

# 🗑️ Borrar cliente
def borrar_cliente():
    nombre = input("Nombre del cliente: ")
    if nombre not in clientes:
        print(" Cliente no encontrado.")
        return
    os.remove(clientes[nombre])
    del clientes[nombre]
    print("🗑️ Cliente eliminado.")

#simulación de notificación a miembros del equipo
def notificar_equipo(mensaje):
    print("\n Notificaciones al equipo:")
    for usuario, rol in usuarios.items():
        print(f" {usuario} ({rol}): {mensaje}")

# ejecutar menú
while True:
    menu()
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        crear_cliente()
    elif opcion == "2":
        consultar_cliente()
    elif opcion == "3":
        modificar_cliente()
    elif opcion == "4":
        borrar_cliente()
    elif opcion == "5":
        print("saliendo del sistema. ¡Hasta luego!")
        break
    else:
        print("opción inválida.")

