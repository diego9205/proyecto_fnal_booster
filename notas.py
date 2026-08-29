from pathlib import Path
from datetime import datetime
import json

AMARILLO = "\033[93m"
RESET = "\033[0m"

print("\n========================================")
print("     Bienvenido al sistema de notas     ")
print("========================================\n")

notas = []

def agregar_nota():
    print(f"\n{AMARILLO}--- AGREGAR NUEVA NOTA ---{RESET}")
    tiempo = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    titulo = input("Ingrese el título de la nota: ")
    contenido = input("Ingrese el contenido de la nota: ")
    categoria = input("Ingrese la categoría de la nota: ")

    nota = {
        "titulo": titulo,
        "contenido": contenido,
        "categoria": categoria,
        "fecha": tiempo
    }
    notas.append(nota)
    guardar_notas()
    print("\n✓ Nota agregada exitosamente.\n")

def ver_notas():
    print(f"\n{AMARILLO}--- LISTA DE TODAS LAS NOTAS ---{RESET}")
    if not notas:
        print("No hay notas guardadas.\n")
    else:
        for note in notas:
            print(f"\nTítulo:    {note['titulo']}")
            print(f"Contenido: {note['contenido']}")
            print(f"Categoría: {note['categoria']}")
            print(f"Fecha:     {note['fecha']}")
            print("-" * 30)
        print()

def guardar_notas():
    with open("notas.json", "w", encoding="utf-8") as archivo:
        json.dump(notas, archivo, indent=4)

def cargar_notas():
    global notas
    try:
        with open("notas.json", "r", encoding="utf-8") as archivo:
            notas = json.load(archivo)
    except FileNotFoundError:
        notas = []

def buscar_nota():
    print(f"\n{AMARILLO}--- BUSCAR NOTA ---{RESET}")
    busqueda = input("Ingrese el título a buscar: ").lower()
    encontrada = False
    print()
    for nota in notas:
        if busqueda in nota["titulo"].lower():
            print(f"Título:    {nota['titulo']}")
            print(f"Contenido: {nota['contenido']}")
            print(f"Categoría: {nota['categoria']}")
            print(f"Fecha:     {nota['fecha']}")
            print("-" * 30)
            encontrada = True
    if not encontrada:
        print("No se encontró ninguna nota con ese título.")
    print()

def ver_nota():
    print(f"\n{AMARILLO}--- DETALLE DE NOTA ---{RESET}")
    if not notas:
        print("No hay notas para mostrar.\n")
        return
    
    print("Notas disponibles:")
    for i, nota in enumerate(notas, start=1):
        print(f"  {i}. {nota['titulo']}")

    while True:
        try:
            opcion = int(input("\nSeleccione el número de la nota: "))
            if 1 <= opcion <= len(notas):
                nota_sel = notas[opcion - 1]
                print("\n" + "=" * 35)
                print(f"Título:    {nota_sel['titulo']}")
                print(f"Contenido: {nota_sel['contenido']}")
                print(f"Categoría: {nota_sel['categoria']}")
                print(f"Fecha:     {nota_sel['fecha']}")
                print("=" * 35 + "\n")
                break
            else:
                print("Número de nota inválido. Intente nuevamente.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número válido.")

def eliminar_nota():
    print(f"\n{AMARILLO}--- ELIMINAR NOTA ---{RESET}")
    if not notas:
        print("No hay notas para eliminar.\n")
        return

    print("Notas disponibles:")
    for i, nota in enumerate(notas, start=1):
        print(f"  {i}. {nota['titulo']}")

    while True:
        try:
            opcion = int(input("\nSeleccione el número de la nota que desea eliminar: "))
            if 1 <= opcion <= len(notas):
                del notas[opcion - 1]
                guardar_notas()
                print("\n✓ Nota eliminada exitosamente.\n")
                break
            else:
                print("Número de nota inválido. Intente nuevamente.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número válido.")

def editar_nota():
    print(f"\n{AMARILLO}--- EDITAR NOTA ---{RESET}")
    if not notas:
        print("No hay notas para editar.\n")
        return

    print("Notas disponibles:")
    for i, nota in enumerate(notas, start=1):
        print(f"  {i}. {nota['titulo']}")

    while True:
        try:
            opcion = int(input("\nSeleccione el número de la nota que desea editar: "))
            if 1 <= opcion <= len(notas):
                nota_sel = notas[opcion - 1]
                
                print("\n(Presione ENTER si no desea modificar el campo)")
                nuevo_titulo = input(f"Nuevo título [{nota_sel['titulo']}]: ")
                nuevo_contenido = input(f"Nuevo contenido [{nota_sel['contenido']}]: ")
                nueva_categoria = input(f"Nueva categoría [{nota_sel['categoria']}]: ")

                if nuevo_titulo.strip():
                    nota_sel["titulo"] = nuevo_titulo
                if nuevo_contenido.strip():
                    nota_sel["contenido"] = nuevo_contenido
                if nueva_categoria.strip():
                    nota_sel["categoria"] = nueva_categoria

                nota_sel["fecha"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                guardar_notas()
                print("\n✓ Nota editada exitosamente.\n")
                break
            else:
                print("Número de nota inválido. Intente nuevamente.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número válido.")

menu = f"""
{AMARILLO}========================================
           MENÚ PRINCIPAL
========================================{RESET}
1. Agregar nota
2. Ver notas
3. Ver detalle de nota
4. Editar nota
5. Eliminar nota
6. Buscar nota
7. Salir

Seleccione una opción: """

cargar_notas()
opc = 0

while opc != 7:
    try:
        opc = int(input(menu))
    except ValueError:
        print("\nEntrada inválida. Por favor, ingrese un número válido.\n")
        continue

    if opc == 1:
        agregar_nota()
    elif opc == 2:
        ver_notas()
    elif opc == 3:
        ver_nota()
    elif opc == 4:
        editar_nota()
    elif opc == 5:
        eliminar_nota()
    elif opc == 6:
        buscar_nota()
    elif opc == 7:
        print("\n========================================")
        print(" Gracias por usar el sistema de notas ")
        print("========================================\n")
    else:
        print("\nOpción inválida. Por favor, seleccione una opción del 1 al 7.\n")