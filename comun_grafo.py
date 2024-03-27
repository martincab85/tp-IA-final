import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from datos_grafo import dlr_20_1, nodos_20_1, uniones_20_1, nodo_incial_20_1, nodo_final_20_1, dlr_20_2, nodos_20_2, uniones_20_2, nodo_incial_20_2, nodo_final_20_2, dlr_20_5, nodos_20_5, uniones_20_5, nodo_incial_20_5, nodo_final_20_5

# Seleccionar el número de grafo que deseas utilizar
numero_de_grafo = 20.5  # Cambia a 20.1 si deseas utilizar el primer grafo

# Acceder a los datos correspondientes al número de grafo seleccionado
if numero_de_grafo == 20.1:
    nodo_inicial = nodo_incial_20_1
    nodo_final = nodo_incial_20_1
    dlr = dlr_20_1
    nodos = nodos_20_1
    uniones = uniones_20_1
elif numero_de_grafo == 20.2:
    nodo_inicial = nodo_incial_20_2
    nodo_final = nodo_final_20_2
    dlr = dlr_20_2
    nodos = nodos_20_2
    uniones = uniones_20_2
elif numero_de_grafo == 20.5:
    nodo_inicial = nodo_incial_20_5
    nodo_final = nodo_final_20_5
    dlr = dlr_20_5
    nodos = nodos_20_5
    uniones = uniones_20_5

# Crear un grafo
G = nx.Graph()
G.add_nodes_from(nodos)
G.add_edges_from(uniones)

nodos_actuales = {nodo_inicial: True}  # A
nodos_sucesores = []


def get_uniones(nodo):
    uniones_locales = []
    # Iterar sobre las uniones
    for union in uniones:
        # Verificar si el nodo inicial está en la unión
        if nodo == union[0] and union[1] not in nodos_actuales:
            uniones_locales.append(union[1])
        elif nodo == union[1] and union[0] not in nodos_actuales:
            uniones_locales.append(union[0])
    return uniones_locales


def get_actual_node():
    true_keys = [key for key, value in nodos_actuales.items() if value]
    true_key = true_keys[0]
    return true_key


def check_nodo_siguiente():
    global nodos_actuales

    nodo_actual = get_actual_node()
    uniones = get_uniones(nodo_actual)

    if nodo_actual != nodo_final:
        while uniones:
            nodo_siguiente = min(uniones) if uniones else None
            if nodo_siguiente not in nodos_sucesores:
                nodos_sucesores.append(nodo_siguiente)

            nodo_actual_value = dlr[nodo_actual]
            nodo_siguiente_value = dlr[nodo_siguiente]

            print(nodo_actual, ' --- nodo actual')
            print(uniones, ' --- uniones')
            print(nodo_siguiente, ' --- nodo siguiente')
            print(nodos_sucesores, ' --- nodos succesores')

            if nodo_siguiente_value <= nodo_actual_value:
                nodos_actuales[nodo_actual] = False
                nodos_actuales[nodo_siguiente] = True
                print(nodos_actuales, ' --- nodos actuales')
                print('-----------------------------------------------------')
                print('\n')
                break
            else:
                uniones.remove(nodo_siguiente)

    else:
        print('\n')
        print('se termino el programa')
        print(nodos_actuales)
        print(nodos_sucesores)

check_nodo_siguiente()
