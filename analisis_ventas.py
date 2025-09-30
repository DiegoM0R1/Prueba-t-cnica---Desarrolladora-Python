import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

def cargar_y_limpiar_datos(filepath='ventas.csv'):
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

def analizar_datos(df):
    producto_mas_vendido = df.groupby('producto')['cantidad'].sum().idxmax()
    print(f"a) El producto más vendido por cantidad es: {producto_mas_vendido}")

    producto_mayor_facturación = df.groupby('producto')['total'].sum().idxmax()
    print(f"b) El producto con mayor facturación total es: {producto_mayor_facturación}")

    #facturación total del mes
    df['mes'] = df['fecha'].dt.strftime('%Y-%m')
    facturacion_por_mes = df.groupby('mes')['total'].sum()
    print("\nc) Facturación total por mes:")
    print(facturacion_por_mes)
    return facturacion_por_mes, producto_mayor_facturación

def generar_grafico(facturacion_por_mes, output_file='grafico.png'):

    plt.figure(figsize=(10, 6))
    facturacion_por_mes.plot(kind='bar', color='skyblue')
    plt.title('Facturación Total por Mes', fontsize=16)
    plt.xlabel('Mes', fontsize=12)
    plt.ylabel('Facturación Total', fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(output_file)
    print(f"\nGráfico '{output_file}' generando exitosamente.")
    
def guardar_en_db(df, db_file='ventas.db'):

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
            
