"""Una pequeña tienda quiere entender cómo se comportan 
sus ventas a lo largo del mes
para detectar productos más rentables y oportunidades de mejora"""

import pandas as pd
import os

base_path = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(base_path, 'ventas.csv')

# Cargar los datos
ventas = pd.read_csv(data_path)
print(ventas.head())

# Información básica del DataFrame
print(ventas.info())

#Control de tipo de datos
ventas['date'] = pd.to_datetime(ventas['date'], infer_datetime_format=True)
ventas['category'] = ventas['category'].astype('string')

print(ventas.info())

#Ventas totales
ventas_totales = ventas['price'].sum()
print(f"Ventas totales: ${ventas_totales:.2f}")

# Calcular ventas totales por categoría
ventas_por_categoria = ventas.groupby('category')['price'].sum().reset_index()
print(ventas_por_categoria)

# Productos más vendidos por cantidad
print(f"Productos más vendidos por cantidad:")
productos_top = ventas.groupby('product_name')['quantity'].sum().reset_index()
productos_top = productos_top.sort_values(by='quantity', ascending=False).head(2)
print(productos_top)

#Resumende ventas
resumen = {
    "Ventas totales ($)": ventas_totales,
    "Categoría líder": ventas_por_categoria.loc[ventas_por_categoria['price'].idxmax(), 'category'],
    "Ventas Categoría Líder ($)": round(ventas_por_categoria['price'].max(), 2),
    "Top 2 Productos Más Vendidos": productos_top.to_dict('records')
}

#Mostrar resumen
print("RESUMEN DE VENTAS")
for key, value in resumen.items():
    print(f"{key}: {value}")

# Guardar resumen en un archivo de texto
resumen_path = os.path.join(base_path, 'resumen_ventas.txt')

 