import json
import os

# ───────── COLORES ─────────
ROJO = "\033[91m"
VERDE = "\033[92m"
AMARILLO = "\033[93m"
AZUL = "\033[94m"
RESET = "\033[0m"

archivo = "clientes.json"


# ───────── UTILIDADES ─────────
def linea():
    print(AZUL + "═" * 50 + RESET)


def pausar():
    input(AMARILLO + "\nPresione ENTER para continuar..." + RESET)


# ───────── PERSISTENCIA ─────────
def cargar():
    if os.path.exists(archivo):
        try:
            with open(archivo, "r") as f:
                return json.load(f)
        except:
            print(ROJO + "Error leyendo archivo, iniciando vacío" + RESET)
            return []
    return []


def guardar(clientes):
    with open(archivo, "w") as f:
        json.dump(clientes, f, indent=4)


# ───────── ID ─────────
def generar_id(clientes):
    if not clientes:
        return 1
    return max(c["id"] for c in clientes) + 1


# ───────── VALIDACIONES ─────────
def pedir_entero(mensaje):
    while True:
        valor = input(mensaje)
        if valor.isdigit():
            return int(valor)
        print(ROJO + "Debe ingresar un número válido" + RESET)


def pedir_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        print(ROJO + "No puede estar vacío" + RESET)


# ───────── CRUD ─────────
def crear(clientes):
    linea()
    print(VERDE + "🟢 CREAR CLIENTE" + RESET)

    nombre = pedir_texto("Nombre: ")
    edad = pedir_entero("Edad: ")
    plan = pedir_texto("Plan (mensual/trimestral/anual): ").lower()

    cliente = {
        "id": generar_id(clientes),
        "nombre": nombre,
        "edad": edad,
        "plan": plan,
        "estado": "activo"
    }

    clientes.append(cliente)
    guardar(clientes)

    print(VERDE + "✅ Cliente registrado" + RESET)


def mostrar(clientes):
    linea()
    print(AZUL + "📋 LISTA DE CLIENTES" + RESET)

    if not clientes:
        print(AMARILLO + "No hay clientes" + RESET)
        return

    for c in clientes:
        estado = "🟢" if c["estado"] == "activo" else "🔴"

        print(f"{VERDE}ID:{RESET} {c['id']}")
        print(f"{VERDE}Nombre:{RESET} {c['nombre']}")
        print(f"{VERDE}Edad:{RESET} {c['edad']}")
        print(f"{VERDE}Plan:{RESET} {c['plan']}")
        print(f"{VERDE}Estado:{RESET} {estado} {c['estado']}")
        linea()


def buscar(clientes):
    linea()
    print(AMARILLO + "🔍 BUSCAR CLIENTE" + RESET)

    termino = input("Ingrese ID o nombre: ").strip()

    if not termino:
        print(ROJO + "Entrada vacía" + RESET)
        return

    resultados = []

    if termino.isdigit():
        id_buscar = int(termino)
        resultados = [c for c in clientes if c["id"] == id_buscar]
    else:
        termino = termino.lower()
        resultados = [c for c in clientes if termino in c["nombre"].lower()]

    if not resultados:
        print(ROJO + "No encontrado" + RESET)
        return

    for c in resultados:
        print(VERDE + "✔ Encontrado:" + RESET, c)


def actualizar(clientes):
    linea()
    print(AMARILLO + "✏ ACTUALIZAR CLIENTE" + RESET)

    id_buscar = pedir_entero("ID: ")

    for c in clientes:
        if c["id"] == id_buscar:

            print("Deje vacío para no cambiar")

            nombre = input("Nuevo nombre: ").strip()
            if nombre:
                c["nombre"] = nombre

            edad = input("Nueva edad: ").strip()
            if edad.isdigit():
                c["edad"] = int(edad)

            plan = input("Nuevo plan: ").strip().lower()
            if plan:
                c["plan"] = plan

            estado = input("Estado (activo/inactivo): ").strip().lower()
            if estado in ("activo", "inactivo"):
                c["estado"] = estado

            guardar(clientes)
            print(VERDE + "Actualizado" + RESET)
            return

    print(ROJO + "Cliente no encontrado" + RESET)


def eliminar(clientes):
    linea()
    print(ROJO + "🗑 ELIMINAR CLIENTE" + RESET)

    id_buscar = pedir_entero("ID: ")

    for c in clientes:
        if c["id"] == id_buscar:
            confirmar = input("¿Seguro? (s/n): ").lower()

            if confirmar == "s":
                clientes.remove(c)
                guardar(clientes)
                print(VERDE + "Eliminado" + RESET)
            else:
                print(AMARILLO + "Cancelado" + RESET)
            return

    print(ROJO + "Cliente no encontrado" + RESET)


# ───────── MENÚ ─────────
clientes = cargar()
opcion = ""

while opcion != "6":

    print("\n" + AZUL + "╔════════════════════════════╗" + RESET)
    print(AZUL + "║   🏋 GIMNASIO PRO SYSTEM 🏋  ║" + RESET)
    print(AZUL + "╠════════════════════════════╣" + RESET)
    print("1. Crear cliente")
    print("2. Mostrar clientes")
    print("3. Buscar cliente")
    print("4. Actualizar cliente")
    print("5. Eliminar cliente")
    print("6. Salir")
    print(AZUL + "╚════════════════════════════╝" + RESET)

    opcion = input("Seleccione: ")

    if opcion == "1":
        crear(clientes)
        pausar()
    elif opcion == "2":
        mostrar(clientes)
        pausar()
    elif opcion == "3":
        buscar(clientes)
        pausar()
    elif opcion == "4":
        actualizar(clientes)
        pausar()
    elif opcion == "5":
        eliminar(clientes)
        pausar()
    elif opcion == "6":
        print(VERDE + "👋 Hasta luego" + RESET)
    else:
        print(ROJO + "Opción inválida" + RESET)