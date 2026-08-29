from pathlib import Path
from datetime import datetime
import json


print("------Bienvenido al sistema de notas------  \n")

notas = []
def agregar_nota():
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

def ver_notas():
    if not notas:
        print("No hay notas ")

    else:
        for note in notas:
            print(f"Título: {note['titulo']}")
            print(f"Contenido: {note['contenido']}")
            print(f"Categoría: {note['categoria']}")
            print(f"Fecha: {note['fecha']}")
            print("------------------------")

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
    busqueda = input("Ingrese el título de la nota que desea buscar: \n").lower()
    encontrada = False
    for nota in notas:
        if busqueda in nota["titulo"].lower():
            print(f"Título: {nota['titulo']}")
            print(f"Contenido: {nota['contenido']}")
            print(f"Categoría: {nota['categoria']}")
            print(f"Fecha: {nota['fecha']}")
            print("------------------------")
            encontrada = True
    if not encontrada:
        print("No se encontró ninguna nota con ese título.")

def ver_nota():
    if not notas:
        print("No hay notas para mostrar.")
        return
    for i, nota in enumerate(notas, start=1):
        print(f"{i}. {nota['titulo']}")

    while True:
        try:
            opcion = int(input("Seleccione el número de la nota que desea ver: "))
            if 1 <= opcion <= len(notas):
                nota_seleccionada = notas[opcion - 1]
                print(f"Título: {nota_seleccionada['titulo']}")
                print(f"Contenido: {nota_seleccionada['contenido']}")
                print(f"Categoría: {nota_seleccionada['categoria']}")
                print(f"Fecha: {nota_seleccionada['fecha']}")
                break
            else:
                print("Número de nota inválido. Intente nuevamente.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número válido.")


def eliminar_nota():
    if not notas:
        print("No hay notas para eliminar.")
        return
    for i, nota in enumerate(notas, start=1):
        print(f"{i}. {nota['titulo']}")

    while True:
        try:
            opcion = int(input("Seleccione el número de la nota que desea eliminar: \n"))
            if 1 <= opcion <= len(notas):
                del notas[opcion -1]
                print("Nota eliminada exitosamente.")
                guardar_notas()
                break
            else:
                print("Número de nota inválido. Intente nuevamente.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número válido.")


def editar_nota():
    if not notas:
        print("No hay notas para editar.")
        return

    for i, nota in enumerate(notas, start=1):
        print(f"{i}. {nota['titulo']}")

    while True:
        try:
            opcion = int(input("Seleccione el número de la nota que desea editar: \n"))
            if 1 <= opcion <= len(notas):
                nota_seleccionada = notas[opcion - 1]
                
                nuevo_titulo = input(f"Ingrese el nuevo título (actual: {nota_seleccionada['titulo']}): ")
                nuevo_contenido = input(f"Ingrese el nuevo contenido (actual: {nota_seleccionada['contenido']}): ")
                nueva_categoria = input(f"Ingrese la nueva categoría (actual: {nota_seleccionada['categoria']}): ")

                if nuevo_titulo.strip():
                    nota_seleccionada["titulo"] = nuevo_titulo
                if nuevo_contenido.strip():
                    nota_seleccionada["contenido"] = nuevo_contenido
                if nueva_categoria.strip():
                    nota_seleccionada["categoria"] = nueva_categoria

                nota_seleccionada["fecha"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                guardar_notas()
                print("Nota editada exitosamente.")
                break
            else:
                print("Número de nota inválido. Intente nuevamente.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número válido.")





    
menu = """
Seleccione una opción:
1. Agregar nota
2. Ver notas
3. ver nota
4. Editar nota
5. Eliminar nota
6. Buscar nota
7. Salir
\n
"""

cargar_notas()
opc = 0

while opc != 7:
    try:
        opc = int(input(menu))
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número válido.")
        continue

    if opc == 1:
        print("Agregar nota")
        agregar_nota()

    elif opc == 2:
        print("Ver notas")
        ver_notas()

    elif opc == 3:
        print("Ver nota")
        ver_nota()

    elif opc == 4:
        print("Editar nota")
        editar_nota()

    elif opc == 5:
        print("Eliminar nota")
        eliminar_nota()

    elif opc == 6:
        print("Buscar nota")
        buscar_nota()

    elif opc == 7:
        print("Gracias por usar el sistema de notas. ¡Hasta luego!")  
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")


