import pandas as pd
import pytest
from analisis_ventas import cargar_y_limpiar_datos

def test_calculo_total():

    data = {
        'fecha': ['2023-01-01', '2023-01-02'],
        'producto': ['Producto A', 'Producto B'],
        'cantidad': [10, 5],
        'precio_unitario': [100, 200]
    }
    df_test = pd.DataFrame(data)
    df_test = pd.DataFrame(data)
    df_test.to_csv('test_ventas.csv', index=False)
    df_procesado = cargar_y_limpiar_datos('test_ventas.csv')

    assert 'total' in df_procesado.columns
    assert df_procesado['total'].iloc[0] == 1000
    assert df_procesado['total'].iloc[1] == 1000
    import os
    os.remove('test_ventas.csv')