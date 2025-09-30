# Ejercicio Práctico: Análisis de Ventas

**Autor:** Diego Mori  
**Fecha de Entrega:** 01 de octubre de 2025

## 1. Introducción

Este proyecto es la solución al ejercicio de análisis de ventas, diseñado para demostrar mi competencia en el manejo de datos con Python. El objetivo principal es procesar un archivo CSV, realizar un análisis estadístico, visualizar los resultados y persistir los datos en una base de datos, siguiendo las mejores prácticas de la programación.

A continuación, se detalla la estructura del proyecto, las decisiones técnicas tomadas y la justificación detrás de cada componente, como si fuera a ser presentado en una entrevista técnica.

## 2. Estructura del Proyecto

La solución está organizada de forma modular para garantizar la claridad y la reusabilidad del código.

- **analisis_ventas.py:** Este es el script principal que contiene toda la lógica de negocio. Lo he estructurado en funciones (cargar_y_limpiar_datos, analizar_datos, etc.) para promover la modularidad y la reutilización. Al encapsular la lógica, cada función tiene una única responsabilidad, lo que facilita la lectura y el mantenimiento.

- **test_analisis.py:** Archivo de pruebas unitarias. Muestra la capacidad para validar la lógica del script de forma automática utilizando pytest, una librería estándar en el desarrollo de Python para el testing.

- **ventas.csv:** El archivo de datos de entrada.

- **grafico.png:** El gráfico de la facturación mensual. Se genera automáticamente al ejecutar el script principal, lo que demuestra la automatización del proceso.

- **ventas.db:** La base de datos SQLite. Es una opción ligera y sin servidor, ideal para este tipo de ejercicios, ya que permite la persistencia de datos de forma sencilla.

## 3. Justificación de las Decisiones Técnicas

En esta sección, explico el porqué de cada línea de código y la elección de las librerías.

### A. Importaciones

```python
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
```

**import pandas as pd:**
- **Palabra clave `import`:** Indica que se carga un módulo o biblioteca externa.
- **pandas:** Es la biblioteca de facto para el análisis de datos en Python. Ofrece estructuras de datos de alto rendimiento como los DataFrame, que son ideales para manejar datos tabulares.
- **as pd:** La palabra clave `as` crea un alias. `pd` es la convención estándar de la comunidad, lo que hace el código más legible y reconocible para otros desarrolladores.

**import matplotlib.pyplot as plt:**
- **matplotlib.pyplot:** Es un submódulo de la biblioteca matplotlib que proporciona una interfaz de creación de gráficos similar a la de MATLAB.
- **as plt:** `plt` es el alias estándar para este submódulo.

**import sqlite3:**
- **sqlite3** es una biblioteca estándar de Python (incluida en la instalación base) para interactuar con bases de datos SQLite. No requiere instalación de librerías adicionales ni un servidor de base de datos, por lo que es la opción más práctica y ligera para este ejercicio.

### B. Primera Función: cargar_y_limpiar_datos

```python
def cargar_y_limpiar_datos(filepath='ventas.csv'):
    # ...
```

- **def:** La palabra clave que define una función, una práctica clave de la programación estructurada que divide el código en bloques lógicos.

- **filepath='ventas.csv':** Se utiliza un parámetro con valor por defecto. Esto hace que la función sea más flexible. Si no se especifica un archivo al llamarla, automáticamente usará `ventas.csv`. Esto facilita tanto las pruebas como la reutilización del código.

- **try...except FileNotFoundError:** Se implementa un bloque de manejo de excepciones. En lugar de que el programa se caiga si el archivo no existe, este bloque captura el error `FileNotFoundError`, imprime un mensaje amigable para el usuario y permite que el programa termine de manera controlada.

```python
    df = pd.read_csv(filepath)
    df.dropna(inplace=True)
    df = df[df['cantidad'] > 0]
    df['total'] = df['cantidad'] * df['precio_unitario']
    return df
```

- **df:** Esta variable es una convención estándar para referirse al DataFrame de pandas.

- **df.dropna(inplace=True):** El método `.dropna()` se utiliza para eliminar filas con valores nulos (NaN). El argumento `inplace=True` es crucial, ya que modifica el DataFrame original en memoria, evitando la creación de una copia y optimizando el uso de recursos.

- **df = df[df['cantidad'] > 0]:** Se utiliza el filtrado por máscara booleana, una técnica vectorial y altamente eficiente en pandas para seleccionar filas que cumplen una condición. Es significativamente más rápido que iterar sobre las filas con un bucle.

- **df['total'] = ...:** Esta es una operación vectorizada. pandas realiza la multiplicación de las series de datos `df['cantidad']` y `df['precio_unitario']` de forma nativa en C, lo que resulta en un rendimiento superior a cualquier bucle for de Python.

### C. Segunda Función: analizar_datos

- **df.groupby(...):** El método `.groupby()` es el corazón de cualquier análisis en pandas. Permite agrupar las filas por una o varias columnas, lo que facilita el cálculo de agregados (sumas, promedios, etc.) para cada grupo.

- **.idxmax():** Se utiliza este método en lugar de ordenar los datos con `sort_values` y luego seleccionar el primer elemento. `idxmax()` es más eficiente porque solo busca el índice del valor máximo, sin necesidad de ordenar todo el conjunto de datos.

### D. Tercera Función: generar_grafico

- **plt.figure(figsize=(10, 6)):** Crea una figura de tamaño específico, lo que permite controlar la calidad y el aspecto del gráfico final.

- **plt.savefig('grafico.png'):** Este método guarda el gráfico en un archivo. Es una práctica recomendada para scripts de fondo (background scripts) o para entornos sin una interfaz gráfica (como servidores remotos), ya que no requiere una ventana para mostrar el gráfico.

### E. Bloque Principal if __name__ == "__main__":

Este es un idioma estándar de Python. El código dentro de este bloque solo se ejecutará cuando el script se corra directamente desde la terminal. Si el archivo `analisis_ventas.py` fuera importado por otro script, este bloque no se ejecutaría, lo que permite reutilizar las funciones sin efectos secundarios.

## Instrucciones para la Ejecución

Para ejecutar la solución, sigue estos sencillos pasos:

1. **Asegúrate de tener Python 3.x instalado.**

2. **Instala las librerías necesarias:**
   ```bash
   pip install pandas matplotlib pytest
   ```

3. **Coloca los archivos** `analisis_ventas.py`, `test_analisis.py` y `ventas.csv` en el mismo directorio.

4. **Ejecutar el Análisis:**
   ```bash
   python analisis_ventas.py
   ```
   Este comando correrá el script, que imprimirá los resultados en la consola, generará el gráfico `grafico.png` y la base de datos `ventas.db`.

5. **Correr las Pruebas:**
   ```bash
   pytest
   ```
   Este comando ejecutará las pruebas unitarias definidas en `test_analisis.py` para validar la lógica del script.

## Códigos Finales y Corregidos

He corregido los errores que mencionaste y te entrego el código limpio y listo para usar.

### analisis_ventas.py

```python
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

# --- Carga y Limpieza de Datos ---
def cargar_y_limpiar_datos(filepath='ventas.csv'):
    """Lee el archivo CSV, limpia los datos y crea la columna 'total'."""
    try:
        df = pd.read_csv(filepath)
    except FileNotFoundError:
        print(f"Error: El archivo {filepath} no se encuentra.")
        return None

    df.dropna(inplace=True)
    df = df[df['cantidad'] > 0]
    df['total'] = df['cantidad'] * df['precio_unitario']
    df['fecha'] = pd.to_datetime(df['fecha'])
    return df

# --- Análisis Básico ---
def analizar_datos(df):
    """Realiza los análisis solicitados."""
    # a) Producto más vendido por cantidad
    producto_mas_vendido = df.groupby('producto')['cantidad'].sum().idxmax()
    print(f"a) El producto más vendido por cantidad es: {producto_mas_vendido}")

    # b) Producto con mayor facturación total
    producto_mayor_facturacion = df.groupby('producto')['total'].sum().idxmax()
    print(f"b) El producto con mayor facturación total es: {producto_mayor_facturacion}")

    # c) Facturación total por mes
    df['mes'] = df['fecha'].dt.strftime('%Y-%m')
    facturacion_por_mes = df.groupby('mes')['total'].sum()
    print("\nc) Facturación total por mes:")
    print(facturacion_por_mes)
    return facturacion_por_mes, producto_mayor_facturacion

# --- Visualización Simple ---
def generar_grafico(facturacion_por_mes, output_file='grafico.png'):
    """Genera y guarda un gráfico de barras."""
    plt.figure(figsize=(10, 6))
    facturacion_por_mes.plot(kind='bar', color='skyblue')
    plt.title('Facturación Total por Mes', fontsize=16)
    plt.xlabel('Mes', fontsize=12)
    plt.ylabel('Facturación Total', fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(output_file)
    print(f"\nGráfico '{output_file}' generado exitosamente.")

# --- Persistencia en Base de Datos ---
def guardar_en_db(df, db_file='ventas.db'):
    """Guarda los resultados del análisis en una base de datos SQLite."""
    conn = sqlite3.connect(db_file)
    df.to_sql('ventas_analisis', conn, if_exists='replace', index=False)
    conn.close()
    print(f"\nDatos guardados en la base de datos '{db_file}'.")

if __name__ == "__main__":
    df_ventas = cargar_y_limpiar_datos()
    if df_ventas is not None:
        facturacion_mensual, _ = analizar_datos(df_ventas)
        generar_grafico(facturacion_mensual)
        guardar_en_db(df_ventas)
```

### test_analisis.py

```python
import pandas as pd
import pytest
import os
from analisis_ventas import cargar_y_limpiar_datos

def test_calculo_total():
    """Valida que la columna 'total' se calcule correctamente."""
    # Crea un DataFrame de prueba con datos simulados
    data = {
        'fecha': ['2023-01-01', '2023-01-02'],
        'producto': ['Producto A', 'Producto B'],
        'cantidad': [10, 5],
        'precio_unitario': [100, 200]
    }
    df_test = pd.DataFrame(data)

    # Guarda el DataFrame de prueba en un archivo CSV temporal
    df_test.to_csv('test_ventas.csv', index=False)

    # Llama a la función de carga y limpieza con el archivo de prueba
    df_procesado = cargar_y_limpiar_datos('test_ventas.csv')
    
    # Verifica que la columna 'total' sea correcta
    assert 'total' in df_procesado.columns
    assert df_procesado['total'].iloc[0] == 1000
    assert df_procesado['total'].iloc[1] == 1000

    # Limpia el archivo de prueba
    os.remove('test_ventas.csv')
```