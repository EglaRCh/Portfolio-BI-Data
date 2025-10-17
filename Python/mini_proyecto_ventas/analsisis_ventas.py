"""
Una pequeña tienda quiere entender cómo se comportan 
sus ventas a lo largo del mes
para detectar productos más rentables y oportunidades de mejora.
Este script analiza el dataset de ventas y genera resúmenes numéricos y visuales.
"""

import pandas as pd
import matplotlib.pyplot as plt
import os

# ===============================
# 1️⃣ Configuración de rutas y carga de datos
# ===============================
base_path = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(base_path, 'ventas.csv')

ventas = pd.read_csv(data_path)
print("\n📘 Vista inicial del dataset:")
print(ventas.head())

# ===============================
# 2️⃣ Información básica del DataFrame
# ===============================
print("\n📊 Información general del DataFrame:")
print(ventas.info())

# ===============================
# 3️⃣ Control y ajuste de tipos de datos
# ===============================
ventas['date'] = pd.to_datetime(ventas['date'], infer_datetime_format=True)
ventas['category'] = ventas['category'].astype('string')

print("\n🔍 Validación de tipos de datos después de conversión:")
print(ventas.info())

# ===============================
# 4️⃣ Cálculos principales
# ===============================
ventas_totales = ventas['price'].sum()
print(f"\n💰 Ventas totales: ${ventas_totales:.2f}")

# Ventas por categoría
ventas_por_categoria = ventas.groupby('category')['price'].sum().reset_index()
print("\n📈 Ventas totales por categoría:")
print(ventas_por_categoria)

# Productos más vendidos por cantidad
print("\n🏆 Productos más vendidos por cantidad:")
productos_top = ventas.groupby('product_name')['quantity'].sum().reset_index()
productos_top = productos_top.sort_values(by='quantity', ascending=False).head(2)
print(productos_top)

# ===============================
# 5️⃣ Resumen general
# ===============================
resumen = {
    "Ventas totales ($)": ventas_totales,
    "Categoría líder": ventas_por_categoria.loc[ventas_por_categoria['price'].idxmax(), 'category'],
    "Ventas Categoría Líder ($)": round(ventas_por_categoria['price'].max(), 2),
    "Top 2 Productos Más Vendidos": productos_top.to_dict('records')
}

print("\n🧾 RESUMEN DE VENTAS")
for key, value in resumen.items():
    print(f"{key}: {value}")

# ===============================
# 6️⃣ Visualización de datos con Matplotlib
# ===============================

# --- Gráfico 1: Barras de ventas por categoría ---
plt.figure(figsize=(8, 5))
plt.bar(ventas_por_categoria['category'], ventas_por_categoria['price'], color='teal')
plt.title('Ingresos Totales por Categoría', fontsize=13, fontweight='bold')
plt.xlabel('Categoría', fontsize=11)
plt.ylabel('Ventas ($)', fontsize=11)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

# --- Gráfico 2: Pie chart de distribución por categoría ---
plt.figure(figsize=(6, 6))
plt.pie(
    ventas_por_categoria['price'],
    labels=ventas_por_categoria['category'],
    autopct='%1.1f%%',
    startangle=140,
    colors=['#4DB6AC', '#008080', '#80CBC4', '#004D40']
)
plt.title('Distribución de Ventas por Categoría', fontsize=13, fontweight='bold')
plt.tight_layout()
plt.show()

# ===============================
# 7️⃣ Guardar resumen en un archivo de texto
# ===============================
resumen_path = os.path.join(base_path, 'resumen_ventas.txt')
with open(resumen_path, 'w', encoding='utf-8') as f:
    f.write("RESUMEN DE VENTAS\n")
    for key, value in resumen.items():
        f.write(f"{key}: {value}\n")

print(f"\n📂 Resumen guardado en: {resumen_path}")

 