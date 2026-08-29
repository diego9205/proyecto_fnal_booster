# Sistema de Gestión de Notas en Consola 📝

Sistema interactivo desarrollado en Python para crear, visualizar, buscar, editar y eliminar notas personales con almacenamiento persistente en formato JSON.

## 📌 Descripción del Proyecto
Este programa implementa operaciones CRUD (Create, Read, Update, Delete) completas junto con mecanismos de búsqueda por coincidencia de palabras clave. Diseñado para ejecutarse directamente en la consola con manejo explícito de errores y formato visual mejorado.

---

## 🚀 Características
- **Operaciones CRUD:**
  - Agregar nueva nota con título, contenido y categoría.
  - Listar todas las notas almacenadas.
  - Ver detalle de una nota específica por selección de índice.
  - Editar campos existentes conservando datos previos al omitir campos.
  - Eliminar notas por número de lista.
- **Búsqueda interactiva:** Búsqueda insensible a mayúsculas/minúsculas por coincidencia en el título.
- **Persistencia automática:** Lectura y escritura continua en archivo `notas.json`.
- **Validación y robustez:** Control de excepciones (`try/except`) para prevenir cierres por entradas inválidas o archivos inexistentes.

---

## 🛠️ Requisitos
- Python 3.8 o superior.
- Módulos estándar utilizados (no requieren instalación de dependencias externas):
  - `datetime`
  - `json`

---

## 💻 Instrucciones de Uso

1. **Clonar o descargar el repositorio:**
   ```bash
   git clone <https://github.com/diego9205/proyecto_fnal_booster.git>
   cd <proyecto_fnal_booster>




## 📸 Ejemplos de Ejecución

### 1. Menú Principal
Al iniciar el programa, se despliega el menú de opciones:

```text
========================================
           MENÚ PRINCIPAL
========================================
1. Agregar nota
2. Ver notas
3. Ver detalle de nota
4. Editar nota
5. Eliminar nota
6. Buscar nota
7. Salir

Seleccione una opción: 1




--- AGREGAR NUEVA NOTA ---
Ingrese el título de la nota: Examen de Estructura de Datos
Ingrese el contenido de la nota: Repasar listas ligadas y árboles binarios
Ingrese la categoría de la nota: Escuela

✓ Nota agregada exitosamente.


--- DETALLE DE NOTA ---
Notas disponibles:
  1. Examen de Estructura de Datos

Seleccione el número de la nota: 1

===================================
Título:    Examen de Estructura de Datos
Contenido: Repasar listas ligadas y árboles binarios
Categoría: Escuela
Fecha:     2026-08-29 00:50:00
===================================
