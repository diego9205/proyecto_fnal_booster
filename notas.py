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


opc = 0

while opc != 7:

    opc = int(input(menu)) 
    if opc == 1:
        print("Agregar nota")
        agregar_nota()

    elif opc == 2:
        print("Ver notas")
        ver_notas()

    elif opc == 3:
        print("Ver nota")

    elif opc == 4:
        print("Editar nota")

    elif opc == 5:
        print("Eliminar nota")

    elif opc == 6:
        print("Buscar nota")

    elif opc == 7:
        print("Gracias por usar el sistema de notas. ¡Hasta luego!")  

    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")


