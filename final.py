"""
╔══════════════════════════════════════════════════════╗
║     SISTEMA DE GESTIÓN DE CLIENTES - GIMNASIO        ║
║           Simulacro - Prueba de Desempeño            ║
╚══════════════════════════════════════════════════════╝
Autor      : Simulacro Python
Descripción: CRUD de clientes con persistencia en JSON
"""

import json
import os

# ── Constantes ────────────────────────────────────────
ARCHIVO_DATOS = "clientes.json"
PLANES_VALIDOS = ("mensual", "trimestral", "anual")


# ════════════════════════════════════════════════════
#  PERSISTENCIA – cargar y guardar en JSON
# ════════════════════════════════════════════════════

def cargar_clientes() -> list:
    """
    Carga la lista de clientes desde el archivo JSON.
    Retorna una lista vacía si el archivo no existe o tiene errores.
    """
    if not os.path.exists(ARCHIVO_DATOS):
        return []
    try:
        with open(ARCHIVO_DATOS, "r", encoding="utf-8") as f:
            datos = json.load(f)
        print(f"✔ Datos cargados desde '{ARCHIVO_DATOS}' ({len(datos)} clientes).")
        return datos
    except (json.JSONDecodeError, IOError) as e:
        print(f"⚠ No se pudo leer '{ARCHIVO_DATOS}': {e}. Se inicia con lista vacía.")
        return []


def guardar_clientes(clientes: list) -> None:
    """
    Guarda la lista de clientes en el archivo JSON.
    """
    try:
        with open(ARCHIVO_DATOS, "w", encoding="utf-8") as f:
            json.dump(clientes, f, ensure_ascii=False, indent=4)
    except IOError as e:
        print(f"⚠ Error al guardar datos: {e}")


# ════════════════════════════════════════════════════
#  UTILIDADES
# ════════════════════════════════════════════════════

def generar_id(clientes: list) -> int:
    """
    Genera un ID único incremental basado en el máximo existente.
    Retorna 1 si la lista está vacía.
    """
    if not clientes:
        return 1
    return max(c["id"] for c in clientes) + 1


def separador(titulo: str = "") -> None:
    """Imprime una línea decorativa con título opcional."""
    linea = "─" * 52
    if titulo:
        print(f"\n╔{linea}╗")
        print(f"║  {titulo.upper():<50}║")
        print(f"╚{linea}╝")
    else:
        print(f"{'─' * 54}")


def mostrar_cliente(cliente: dict) -> None:
    """Imprime los datos de un cliente con formato legible."""
    estado_emoji = "🟢" if cliente["estado"] == "activo" else "🔴"
    print(f"  ID     : {cliente['id']}")
    print(f"  Nombre : {cliente['nombre']}")
    print(f"  Edad   : {cliente['edad']} años")
    print(f"  Plan   : {cliente['plan']}")
    print(f"  Estado : {estado_emoji} {cliente['estado']}")
    separador()


# ════════════════════════════════════════════════════
#  CRUD – Funciones principales
# ════════════════════════════════════════════════════

def crear_cliente(clientes: list) -> None:
    """
    Registra un nuevo cliente solicitando datos por consola.
    Valida nombre, edad, plan y asigna ID automáticamente.
    """
    separador("Registrar Nuevo Cliente")

    # ── Nombre ────────────────────────────────────────
    nombre = input("  Nombre completo : ").strip()
    if not nombre:
        print("⚠ El nombre no puede estar vacío.")
        return

    # ── Edad ──────────────────────────────────────────
    try:
        edad = int(input("  Edad            : "))
        if edad < 14 or edad > 110:
            print("⚠ La edad debe estar entre 14 y 110 años.")
            return
    except ValueError:
        print("⚠ La edad debe ser un número entero.")
        return

    # ── Plan ──────────────────────────────────────────
    print(f"  Planes disponibles: {', '.join(PLANES_VALIDOS)}")
    plan = input("  Tipo de plan    : ").strip().lower()
    if plan not in PLANES_VALIDOS:
        print(f"⚠ Plan inválido. Opciones: {', '.join(PLANES_VALIDOS)}")
        return

    # ── Crear diccionario del cliente ─────────────────
    nuevo_cliente = {
        "id"     : generar_id(clientes),
        "nombre" : nombre,
        "edad"   : edad,
        "plan"   : plan,
        "estado" : "activo"          # todo cliente inicia activo
    }

    clientes.append(nuevo_cliente)
    guardar_clientes(clientes)
    print(f"\n✅ Cliente '{nombre}' registrado con ID {nuevo_cliente['id']}.")


def listar_clientes(clientes: list) -> None:
    """
    Muestra todos los clientes registrados.
    Si la lista está vacía, lo informa.
    """
    separador("Lista de Clientes")
    if not clientes:
        print("  ℹ No hay clientes registrados aún.")
        return

    for cliente in clientes:
        mostrar_cliente(cliente)

    print(f"  Total: {len(clientes)} cliente(s).")


def buscar_cliente(clientes: list) -> dict | None:
    """
    Busca un cliente por ID (número) o por nombre (texto parcial).
    Retorna el diccionario del cliente encontrado o None.
    """
    separador("Buscar Cliente")
    termino = input("  Ingrese ID o nombre a buscar: ").strip()

    if not termino:
        print("⚠ Debe ingresar un término de búsqueda.")
        return None

    resultados = []

    # Intentar buscar por ID si el término es numérico
    if termino.isdigit():
        id_buscado = int(termino)
        resultados = [c for c in clientes if c["id"] == id_buscado]
    
    # Si no es numérico (o no se encontró por ID), buscar por nombre
    if not resultados:
        termino_lower = termino.lower()
        resultados = [c for c in clientes if termino_lower in c["nombre"].lower()]

    if not resultados:
        print(f"  ❌ No se encontró ningún cliente con '{termino}'.")
        return None

    print(f"  Se encontró/encontraron {len(resultados)} resultado(s):\n")
    for cliente in resultados:
        mostrar_cliente(cliente)

    # Retornar el primero (útil para actualizar/eliminar)
    return resultados[0]


def actualizar_cliente(clientes: list) -> None:
    """
    Busca un cliente por ID y permite modificar sus campos.
    El ID no puede modificarse. Los campos vacíos conservan el valor actual.
    """
    separador("Actualizar Cliente")
    id_str = input("  ID del cliente a actualizar: ").strip()

    if not id_str.isdigit():
        print("⚠ El ID debe ser un número entero.")
        return

    id_buscado = int(id_str)
    cliente = next((c for c in clientes if c["id"] == id_buscado), None)

    if cliente is None:
        print(f"  ❌ No existe un cliente con ID {id_buscado}.")
        return

    print(f"\n  Editando cliente: {cliente['nombre']} (ID {cliente['id']})")
    print("  (Deja el campo en blanco para conservar el valor actual)\n")

    # ── Nombre ────────────────────────────────────────
    nuevo_nombre = input(f"  Nombre [{cliente['nombre']}]: ").strip()
    if nuevo_nombre:
        cliente["nombre"] = nuevo_nombre

    # ── Edad ──────────────────────────────────────────
    nueva_edad_str = input(f"  Edad [{cliente['edad']}]: ").strip()
    if nueva_edad_str:
        try:
            nueva_edad = int(nueva_edad_str)
            if 14 <= nueva_edad <= 110:
                cliente["edad"] = nueva_edad
            else:
                print("⚠ Edad fuera de rango (14-110). Se conserva el valor anterior.")
        except ValueError:
            print("⚠ Edad inválida. Se conserva el valor anterior.")

    # ── Plan ──────────────────────────────────────────
    print(f"  Planes: {', '.join(PLANES_VALIDOS)}")
    nuevo_plan = input(f"  Plan [{cliente['plan']}]: ").strip().lower()
    if nuevo_plan:
        if nuevo_plan in PLANES_VALIDOS:
            cliente["plan"] = nuevo_plan
        else:
            print("⚠ Plan inválido. Se conserva el valor anterior.")

    # ── Estado ────────────────────────────────────────
    nuevo_estado = input(f"  Estado [{cliente['estado']}] (activo/inactivo): ").strip().lower()
    if nuevo_estado:
        if nuevo_estado in ("activo", "inactivo"):
            cliente["estado"] = nuevo_estado
        else:
            print("⚠ Estado inválido. Se conserva el valor anterior.")

    guardar_clientes(clientes)
    print(f"\n✅ Cliente ID {id_buscado} actualizado correctamente.")


def eliminar_cliente(clientes: list) -> None:
    """
    Elimina un cliente de la lista previa confirmación del usuario.
    """
    separador("Eliminar Cliente")
    id_str = input("  ID del cliente a eliminar: ").strip()

    if not id_str.isdigit():
        print("⚠ El ID debe ser un número entero.")
        return

    id_buscado = int(id_str)
    cliente = next((c for c in clientes if c["id"] == id_buscado), None)

    if cliente is None:
        print(f"  ❌ No existe un cliente con ID {id_buscado}.")
        return

    print(f"\n  Cliente a eliminar: {cliente['nombre']} (ID {cliente['id']})")
    confirmacion = input("  ¿Confirmar eliminación? (s/n): ").strip().lower()

    if confirmacion == "s":
        clientes.remove(cliente)
        guardar_clientes(clientes)
        print(f"✅ Cliente '{cliente['nombre']}' eliminado correctamente.")
    else:
        print("  ℹ Operación cancelada.")


# ════════════════════════════════════════════════════
#  MENÚ PRINCIPAL
# ════════════════════════════════════════════════════

def mostrar_menu() -> None:
    """Imprime el menú principal de opciones."""
    print("""
╔══════════════════════════════════════╗
║       🏋 GIMNASIO FIT MANAGER 🏋     ║
╠══════════════════════════════════════╣
║  1. Crear cliente                    ║
║  2. Listar clientes                  ║
║  3. Buscar cliente                   ║
║  4. Actualizar cliente               ║
║  5. Eliminar cliente                 ║
║  6. Salir                            ║
╚══════════════════════════════════════╝""")


def main() -> None:
    """
    Función principal: carga datos y ejecuta el bucle del menú.
    """
    print("\n  Bienvenido al Sistema de Gestión de Clientes del Gimnasio")
    clientes = cargar_clientes()   # BONUS: carga persistencia al iniciar

    while True:
        mostrar_menu()
        opcion = input("  Seleccione una opción (1-6): ").strip()

        if opcion == "1":
            crear_cliente(clientes)
        elif opcion == "2":
            listar_clientes(clientes)
        elif opcion == "3":
            buscar_cliente(clientes)
        elif opcion == "4":
            actualizar_cliente(clientes)
        elif opcion == "5":
            eliminar_cliente(clientes)
        elif opcion == "6":
            print("\n  👋 ¡Hasta pronto! Los datos han sido guardados.\n")
            break
        else:
            print("⚠ Opción inválida. Por favor ingrese un número del 1 al 6.")


# ── Punto de entrada ─────────────────────────────────
if __name__ == "__main__":
    main()