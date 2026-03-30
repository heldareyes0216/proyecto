"""
╔══════════════════════════════════════════════════════╗
║     SISTEMA DE GESTIÓN DE CLIENTES - GIMNASIO        ║
║                 VERSIÓN PRO FINAL                    ║
╚══════════════════════════════════════════════════════╝
"""

# ───────── IMPORTACIONES ─────────
import json   # permite guardar y leer datos en formato JSON
import os     # permite verificar si el archivo existe


# ───────── COLORES (DECORACIÓN) ─────────
# Estos códigos ANSI sirven para cambiar el color del texto en la terminal
ROJO = "\033[91m"
VERDE = "\033[92m"
AMARILLO = "\033[93m"
AZUL = "\033[94m"
RESET = "\033[0m"   # vuelve al color normal


# ───────── CONSTANTES ─────────
ARCHIVO_DATOS = "clientes.json"   # nombre del archivo donde se guardan los datos
PLANES_VALIDOS = ("mensual", "trimestral", "anual")  # opciones válidas de plan


# ════════════════════════════════════════════════════
#  PERSISTENCIA (JSON)
# ════════════════════════════════════════════════════

def cargar_clientes() -> list:
    """
    Carga los clientes desde el archivo JSON.
    Si no existe o hay error, retorna una lista vacía.
    """
    # si el archivo no existe
    if not os.path.exists(ARCHIVO_DATOS):
        return []

    try:
        # abrimos el archivo en modo lectura
        with open(ARCHIVO_DATOS, "r") as f:
            datos = json.load(f)   # convertimos JSON a lista de Python

        print(VERDE + f"✔ Datos cargados ({len(datos)} clientes)" + RESET)
        return datos

    except:
        # si ocurre un error al leer el archivo
        print(ROJO + "Error leyendo archivo, iniciando vacío" + RESET)
        return []


def guardar_clientes(clientes: list) -> None:
    """
    Guarda la lista de clientes en el archivo JSON.
    """
    try:
        # abrimos el archivo en modo escritura
        with open(ARCHIVO_DATOS, "w") as f:
            json.dump(clientes, f, indent=4)  # guardamos con formato bonito

    except:
        print(ROJO + "Error al guardar" + RESET)


# ════════════════════════════════════════════════════
#  UTILIDADES
# ════════════════════════════════════════════════════

def generar_id(clientes: list) -> int:
    """
    Genera un ID único.
    Si no hay clientes, retorna 1.
    Si hay clientes, toma el ID mayor y suma 1.
    """
    if not clientes:
        return 1

    # busca el mayor ID en la lista
    return max(c["id"] for c in clientes) + 1


def separador(titulo: str = "") -> None:
    """
    Imprime una línea decorativa con título opcional.
    (Esto es solo visual, no afecta la lógica)
    """
    linea = "═" * 50

    if titulo:
        print(AZUL + f"\n╔{linea}╗" + RESET)
        print(AZUL + f"║  {titulo.upper():<46}║" + RESET)
        print(AZUL + f"╚{linea}╝" + RESET)
    else:
        print(AZUL + "═" * 54 + RESET)


def pausar():
    """
    Pausa el programa hasta que el usuario presione ENTER.
    """
    input(AMARILLO + "\nPresione ENTER para continuar..." + RESET)


def pedir_entero(mensaje):
    """
    Pide un número entero al usuario y valida que sea correcto.
    """
    while True:
        valor = input(mensaje)

        # verificamos que sea número
        if valor.isdigit():
            return int(valor)

        print(ROJO + "Ingrese un número válido" + RESET)


def pedir_texto(mensaje):
    """
    Pide texto al usuario y valida que no esté vacío.
    """
    while True:
        texto = input(mensaje).strip()

        if texto:
            return texto

        print(ROJO + "No puede estar vacío" + RESET)


def mostrar_cliente(cliente: dict) -> None:
    """
    Muestra la información de un cliente de forma organizada.
    """
    # usamos emoji dependiendo del estado
    estado = "🟢" if cliente["estado"] == "activo" else "🔴"

    print(f"{VERDE}ID:{RESET} {cliente['id']}")
    print(f"{VERDE}Nombre:{RESET} {cliente['nombre']}")
    print(f"{VERDE}Edad:{RESET} {cliente['edad']}")
    print(f"{VERDE}Plan:{RESET} {cliente['plan']}")
    print(f"{VERDE}Estado:{RESET} {estado} {cliente['estado']}")

    separador()   # línea decorativa


# ════════════════════════════════════════════════════
#  CRUD (FUNCIONES PRINCIPALES)
# ════════════════════════════════════════════════════

def crear_cliente(clientes: list) -> None:
    """
    Crea un nuevo cliente solicitando datos al usuario.
    """
    separador("Crear Cliente")

    # pedimos datos con validación
    nombre = pedir_texto("Nombre: ")
    edad = pedir_entero("Edad: ")

    print(f"Planes: {', '.join(PLANES_VALIDOS)}")
    plan = pedir_texto("Plan: ").lower()

    # validamos que el plan sea correcto
    if plan not in PLANES_VALIDOS:
        print(ROJO + "Plan inválido" + RESET)
        return

    # creamos el diccionario del cliente
    nuevo = {
        "id": generar_id(clientes),  # ID automático
        "nombre": nombre,
        "edad": edad,
        "plan": plan,
        "estado": "activo"
    }

    # agregamos a la lista
    clientes.append(nuevo)

    # guardamos en JSON
    guardar_clientes(clientes)

    print(VERDE + "Cliente creado" + RESET)


def listar_clientes(clientes: list) -> None:
    """
    Muestra todos los clientes registrados.
    """
    separador("Lista de Clientes")

    if not clientes:
        print(AMARILLO + "No hay clientes" + RESET)
        return

    # recorremos la lista
    for c in clientes:
        mostrar_cliente(c)

    print(f"Total: {len(clientes)}")


def buscar_cliente(clientes: list):
    """
    Busca clientes por ID o por nombre.
    """
    separador("Buscar Cliente")

    termino = input("Ingrese ID o nombre: ").strip()

    if not termino:
        print(ROJO + "Entrada vacía" + RESET)
        return None

    resultados = []

    # búsqueda por ID
    if termino.isdigit():
        resultados = [c for c in clientes if c["id"] == int(termino)]

    # búsqueda por nombre
    else:
        resultados = [c for c in clientes if termino.lower() in c["nombre"].lower()]

    if not resultados:
        print(ROJO + "No encontrado" + RESET)
        return None

    for c in resultados:
        mostrar_cliente(c)

    return resultados[0]


def actualizar_cliente(clientes: list) -> None:
    """
    Permite modificar los datos de un cliente existente.
    """
    separador("Actualizar Cliente")

    id_buscar = pedir_entero("ID: ")

    # buscamos el cliente
    cliente = next((c for c in clientes if c["id"] == id_buscar), None)

    if not cliente:
        print(ROJO + "No encontrado" + RESET)
        return

    print("Dejar vacío para no cambiar")

    # actualizamos campos
    nombre = input("Nombre: ").strip()
    if nombre:
        cliente["nombre"] = nombre

    edad = input("Edad: ").strip()
    if edad.isdigit():
        cliente["edad"] = int(edad)

    plan = input("Plan: ").strip().lower()
    if plan in PLANES_VALIDOS:
        cliente["plan"] = plan

    estado = input("Estado (activo/inactivo): ").strip().lower()
    if estado in ("activo", "inactivo"):
        cliente["estado"] = estado

    guardar_clientes(clientes)

    print(VERDE + "Actualizado" + RESET)


def eliminar_cliente(clientes: list) -> None:
    """
    Elimina un cliente de la lista.
    """
    separador("Eliminar Cliente")

    id_buscar = pedir_entero("ID: ")

    cliente = next((c for c in clientes if c["id"] == id_buscar), None)

    if not cliente:
        print(ROJO + "No encontrado" + RESET)
        return

    confirmar = input("¿Seguro? (s/n): ").lower()

    if confirmar == "s":
        clientes.remove(cliente)
        guardar_clientes(clientes)
        print(VERDE + "Eliminado" + RESET)
    else:
        print(AMARILLO + "Cancelado" + RESET)


# ════════════════════════════════════════════════════
#  MENÚ PRINCIPAL
# ════════════════════════════════════════════════════

def mostrar_menu() -> None:
    """
    Muestra el menú principal del sistema.
    """
    print("\n" + AZUL + "╔════════════════════════════╗" + RESET)
    print(AZUL + "║   🏋 GIMNASIO PRO SYSTEM 🏋  ║" + RESET)
    print(AZUL + "╠════════════════════════════╣" + RESET)
    print("1. Crear cliente")
    print("2. Listar clientes")
    print("3. Buscar cliente")
    print("4. Actualizar cliente")
    print("5. Eliminar cliente")
    print("6. Salir")
    print(AZUL + "╚════════════════════════════╝" + RESET)


def main() -> None:
    """
    Función principal que ejecuta el sistema.
    """
    # cargamos datos al iniciar
    clientes = cargar_clientes()

    opcion = ""

    # bucle del menú
    while opcion != "6":
        mostrar_menu()
        opcion = input("Seleccione: ")

        if opcion == "1":
            crear_cliente(clientes)
            pausar()

        elif opcion == "2":
            listar_clientes(clientes)
            pausar()

        elif opcion == "3":
            buscar_cliente(clientes)
            pausar()

        elif opcion == "4":
            actualizar_cliente(clientes)
            pausar()

        elif opcion == "5":
            eliminar_cliente(clientes)
            pausar()

        elif opcion == "6":
            print(VERDE + "👋 Hasta luego" + RESET)

        else:
            print(ROJO + "Opción inválida" + RESET)


# ───────── PUNTO DE ENTRADA ─────────
if __name__ == "__main__":
    main()