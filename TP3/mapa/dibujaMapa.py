import geopandas as gpd
import matplotlib.pyplot as plt
import networkx as nx

# Coordenadas corregidas para las capitales indicadas
capitales = {
    'Cdad. de Bs. As.': (-58.3772, -34.6131),
    'Córdoba': (-64.1888, -31.4201),
    'Corrientes': (-57.8341, -27.9692),
    'Formosa': (-58.1781, -26.1775),
    'La Plata': (-57.9545, -34.9214),   
    'La Rioja': (-66.8557, -29.4135),
    'Mendoza': (-68.8458, -32.8895),
    'Neuquén': (-68.9583, -38.9517),
    'Paraná': (-59.52, -31.7413),
    'Posadas': (-55.8929, -27.3646),
    'Rawson': (-65.3085, -43.2527),
    'Resistencia': (-58.9906, -27.4606),
    'Río Galleqos': (-69.3105, -51.6234),
    'S.F.d.V.d. Catamarca': (-65.7851, -28.4696), 
    'S.M. de Tucumán': (-65.2226, -26.8241),  
    'S.S. de Jujuy': (-65.2971, -24.1946),    
    'Salta': (-65.4117, -24.7821),
    'San Juan': (-68.5367, -31.5375),
    'San Luis': (-66.3378, -33.3017),
    'Santa Fe': (-60.7733, -31.6230),
    'Santa Rosa': (-64.2838, -36.6202),
    'Sgo. Del Estero': (-64.2642, -27.7845),  
    'Ushuaia': (-68.3040, -54.8050),
    'Viedma': (-64.2143, -40.58)
}

# Lista de localidades en el mismo orden que los índices
localidades = [
    'Cdad. de Bs. As.', 'Córdoba', 'Corrientes', 'Formosa', 'La Plata', 
    'La Rioja', 'Mendoza', 'Neuquén', 'Paraná', 'Posadas', 
    'Rawson', 'Resistencia', 'Río Galleqos', 'S.F.d.V.d. Catamarca', 
    'S.M. de Tucumán', 'S.S. de Jujuy', 'Salta', 'San Juan', 
    'San Luis', 'Santa Fe', 'Santa Rosa', 'Sgo. Del Estero', 
    'Ushuaia', 'Viedma'
]

# Función que recibe el orden y dibuja el mapa
def dibujarMapa(orden):
    # Crear un grafo
    G = nx.Graph()

    # Añadir nodos al grafo con las posiciones de las capitales según el orden proporcionado
    for i in orden:
        localidad = localidades[i]
        if localidad in capitales:
            G.add_node(localidad, pos=capitales[localidad])

    # Añadir aristas entre las capitales en el orden especificado
    for i in range(len(orden) - 1):
        localidad_origen = localidades[orden[i]]
        localidad_destino = localidades[orden[i + 1]]
        G.add_edge(localidad_origen, localidad_destino)

    # Intentar cargar el mapa de Argentina desde el shapefile
    try:
        print("Cargando el mapa de Argentina...")
        argentina = gpd.read_file('TP3\mapa\gadm41_ARG_1.shp')  # Cambia 'gadm41_ARG_0.shp' al nombre correcto de tu archivo
        print("Mapa cargado con éxito.")
    except Exception as e:
        print(f"Error al cargar el mapa: {e}")
        exit()

    # Crear la figura y los ejes
    fig, ax = plt.subplots(figsize=(10, 15))

    # Dibujar el mapa con límites en color negro
    argentina.plot(ax=ax, color='lightgrey', edgecolor='black')

    # Obtener las posiciones de los nodos
    pos = nx.get_node_attributes(G, 'pos')

    # Dibujar las líneas entre las capitales
    nx.draw_networkx_edges(G, pos, ax=ax, edge_color='blue', width=1)

    # Dibujar las capitales
    nx.draw_networkx_nodes(G, pos, ax=ax, node_size=10, node_color='red')

    # Etiquetas de las capitales
    nx.draw_networkx_labels(G, pos, ax=ax, font_size=5, font_color='black')

    # Mostrar el mapa
    plt.title("Recorrido realizado")
    plt.axis('off')  # No mostrar ejes
    plt.show()

# El orden que recibes como parámetro
#orden =  [15, 16, 14, 21, 13, 5, 17, 6, 18, 1, 19, 8, 0, 4, 20, 7, 23, 10, 12, 22, 11, 2, 3, 9]
# Llamar a la función con el orden proporcionado
#dibujarMapa(orden)
