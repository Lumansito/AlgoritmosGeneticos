import pandas as pd

df = pd.read_excel(io=r'TP3\TablaCapitales.xlsx', sheet_name="Sheet1")
array = df.to_numpy()

print("ARREGLO ",array)

capitales=array[:,0].copy()
print("\n\nCAPITALES############\n",len(capitales))
print("\n",capitales)

visitadas = [0 for _ in range(24)] 
print("\n\nVISITADAS############\n",len(visitadas))
print("\n",visitadas)

orden = [0 for _ in range(24)]
print("\n\nORDEN############\n",len(orden))
print("\n",orden)

distancias = array[1][1:].copy()
print("\n\nDISTANCIAS desde ",capitales[1],"############\n",len(distancias))
print("\n",distancias)