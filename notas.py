from pathlib import Path
from datetime import datetime
print("------Bienvenido al sistema de notas------  \n")


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
    elif opc == 2:
        print("Ver notas")
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

