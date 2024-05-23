import pandas as pd

# Definir los datos para las tablas
datos_personas = {
    'Nombre': ['Ana', 'Juan', 'Pedro', 'Maria'],
    'Edad': [23, 35, 45, 29],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Sevilla']
}

datos_productos = {
    'Producto': ['A', 'B', 'C', 'D'],
    'Precio': [10, 20, 30, 40],
    'Cantidad': [100, 150, 200, 250]
}

# Crear DataFrames a partir de los datos
df_personas = pd.DataFrame(datos_personas)
df_productos = pd.DataFrame(datos_productos)

# Crear un archivo Excel con múltiples hojas
with pd.ExcelWriter('datos_exportados.xlsx') as writer:
    df_personas.to_excel(writer, sheet_name='Personas', index=False)
    df_productos.to_excel(writer, sheet_name='Productos', index=False)
