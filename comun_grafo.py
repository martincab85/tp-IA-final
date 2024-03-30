import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib.widgets import Button
import networkx as nx
import matplotlib.pyplot as plt
from datos_grafo import dlr_20_1, nodos_20_1, uniones_20_1, nodo_incial_20_1, nodo_final_20_1, dlr_20_2, nodos_20_2, uniones_20_2, nodo_incial_20_2, nodo_final_20_2, dlr_20_5, nodos_20_5, uniones_20_5, nodo_incial_20_5, nodo_final_20_5

# Seleccionar el número de grafo que deseas utilizar
numero_de_grafo = 20.5  # Cambia a 20.1 si deseas utilizar el primer grafo

# Acceder a los datos correspondientes al número de grafo seleccionado
if numero_de_grafo == 20.1:
    nodo_inicial = nodo_incial_20_1
    nodo_final = nodo_final_20_1
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

nodos_actuales = {nodo_inicial: True}  # A
nodos_sucesores = []
random_seed = 42


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

            # print(nodo_actual, ' --- nodo actual')
            # print(uniones, ' --- uniones')
            # print(nodo_siguiente, ' --- nodo siguiente')
            # print(nodos_sucesores, ' --- nodos succesores')

            if nodo_siguiente_value <= nodo_actual_value:
                nodos_actuales[nodo_actual] = False
                nodos_actuales[nodo_siguiente] = True

                # print(nodos_actuales, ' --- nodos actuales')
                # print('-----------------------------------------------------')
                # print('\n')
                break
            else:
                uniones.remove(nodo_siguiente)

    else:
        print('\n')
        print('se termino el programa')
        print(nodos_actuales)
        print(nodos_sucesores)


def mostrar_grafo_inicial():
    # Crear grafo
    G = nx.Graph()
    G.add_nodes_from(nodos)
    G.add_edges_from(uniones)

    # Mostrar grafo
    fig, ax = plt.subplots()
    pos = nx.spring_layout(G, seed=random_seed)
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=700,
            edge_color='black', linewidths=1, font_size=10, ax=ax)
    nx.draw_networkx_nodes(
        G, pos, nodelist=[nodo_inicial], node_size=700, node_color='red')
    nx.draw_networkx_nodes(
        G, pos, nodelist=[nodo_final], node_size=700, node_color='green')
    ax.set_title('Grafo Inicial')
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack()


def mostrar_paso_a_paso():
    # Crear ventana secundaria para mostrar paso a paso
    window_paso_a_paso = tk.Toplevel(window)
    window_paso_a_paso.title('Paso a Paso')

    # Mostrar primer paso
    fig, ax = plt.subplots()
    G = nx.Graph()
    G.add_nodes_from(nodo_inicial)
    pos = nx.spring_layout(G, seed=random_seed)
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=700,
            edge_color='black', linewidths=1, font_size=10, ax=ax)
    ax.set_title('Paso: 1')
    canvas = FigureCanvasTkAgg(fig, master=window_paso_a_paso)
    canvas.draw()
    canvas.get_tk_widget().pack()

    # Botón para avanzar al siguiente paso
    btn_paso_siguiente = tk.Button(
        window_paso_a_paso, text="Siguiente Paso", command=lambda: paso_siguiente(ax, canvas, G))
    btn_paso_siguiente.pack()


def paso_siguiente(ax,canvas,G):
    global nodos_actuales, nodos_sucesores
    check_nodo_siguiente()
    print(nodos_actuales)
    print(nodos_sucesores)

    # Limpiar el eje antes de redibujar el grafo
    ax.clear()

    # Redibujar el grafo con nodos actuales
    pos = nx.spring_layout(G, seed=random_seed)
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=700,
            edge_color='black', linewidths=1, font_size=10, ax=ax)

    # Dibujar el nodo inicial en rojo
    nx.draw_networkx_nodes(G, pos=pos, nodelist=[nodo_inicial], node_color='red', node_size=700, ax=ax)
    print(G.nodes())
    print(G.edges())
    # Dibujar nodos sucesores que van apareciendo
    for nodo in nodos_sucesores:
        if nodo in G:
            nx.draw_networkx_nodes(G, pos=pos, nodelist=[nodo], node_color='green', node_size=700, ax=ax)
            G.add_edge(nodo_inicial, nodo)
        else:
            print(f"El nodo {nodo} no está presente en el grafo original.")

    # Dibujar los bordes
    nx.draw_networkx_edges(G, pos=pos, edgelist=G.edges(), ax=ax)

    # Actualizar el título del gráfico
    ax.set_title(f'Paso: {len(nodos_actuales)}')

    # Redibujar el lienzo
    canvas.draw()

def on_closing():
    window.quit()

# Configuración de la ventana principal
window = tk.Tk()
window.title('Visualizador de Grafo')

# Detectar cuando se cierra la ventana
window.protocol("WM_DELETE_WINDOW", on_closing)

# Botón para mostrar paso a paso
btn_mostrar_paso_a_paso = tk.Button(
    window, text="Paso a Paso", command=mostrar_paso_a_paso)
btn_mostrar_paso_a_paso.pack()

# Iniciar el loop de la interfaz
mostrar_grafo_inicial()
window.mainloop()


# # Función para mostrar el grafo principal
# def mostrar_grafo():
#     G = nx.Graph()
#     G.add_nodes_from(nodos)
#     G.add_edges_from(uniones)

#     pos = nx.spring_layout(G)  # Layout para posicionar los nodos

#     fig, ax = plt.subplots()
#     nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=700,
#             edge_color='black', linewidths=1, font_size=10, ax=ax)
#     nx.draw_networkx_nodes(
#         G, pos, nodelist=[nodo_inicial], node_size=700, node_color='red')
#     nx.draw_networkx_nodes(
#         G, pos, nodelist=[nodo_final], node_size=700, node_color='green')
#     plt.title('Grafo Principal')

#     # Función para el botón Siguiente Paso
#     def on_button_clicked(event):
#         paso_a_paso()

#     # Crear el botón dentro del gráfico
#     # [left, bottom, width, height]
#     button_ax1 = fig.add_axes([0.7, 0.05, 0.2, 0.05])
#     button1 = Button(button_ax1, 'Siguiente Paso')
#     button1.on_clicked(on_button_clicked)

#     plt.show()


# # Función para mostrar el grafo paso a paso
# def paso_a_paso():
#     print('paso a paso')
#     G2 = nx.Graph()
#     G2.add_node(nodo_inicial)
#     pos = nx.spring_layout(G2)
#     fig, ax = plt.subplots()
#     nx.draw(G2, pos, with_labels=True, node_color='skyblue',
#             node_size=700, edge_color='black', linewidths=1, font_size=10, ax=ax)
#     nx.draw_networkx_nodes(
#         G2, pos, nodelist=[nodo_inicial], node_size=700, node_color='red')
#     plt.title('Escalada Simple')

#     # Función para el botón Siguiente Paso
#     def next(event):
#         siguiente()

#     # Crear el botón dentro del gráfico
#     button_ax2 = fig.add_axes([0.7, 0.05, 0.2, 0.05])  # Corregir la posición del botón
#     button2 = Button(button_ax2, 'Proxima Iteracion')
#     button2.on_clicked(next)
#     plt.show()


# def siguiente():
#     print('Siguiente')
#     check_nodo_siguiente()


# # Crear el botón para mostrar el grafo
# mostrar_grafo()

# # Dibujar el grafo inicial
# plt.figure(figsize=(7,5))
# pos = nx.spring_layout(G)  # Posiciones de los nodos
# nx.draw(G, pos, with_labels=True, node_size=900,
#         node_color='skyblue', font_size=15, font_weight='bold')
# nx.draw_networkx_nodes(
#     G, pos, nodelist=[nodo_inicial], node_size=900, node_color='red')
# nx.draw_networkx_nodes(
#     G, pos, nodelist=[nodo_final], node_size=900, node_color='green')

# # Botón para avanzar en el grafo
# ax_next_button = plt.axes([0.77, 0.01, 0.2, 0.05])
# next_button = Button(ax_next_button, 'Siguiente Nodo')
# next_button.on_clicked(check_nodo_siguiente)

# plt.show()


# # Crear un nuevo grafo para mostrar el paso a paso
# plt.clf()  # Limpiar la figura anterior
# plt.figure(figsize=(7,5))  # Dimensiones de la figura
# G_new = nx.Graph()
# G_new.add_nodes_from(nodos)
# G_new.add_edges_from(uniones)
# pos_new = nx.spring_layout(G_new)
# nx.draw(G_new, pos_new, with_labels=True, node_size=900,
#         node_color='skyblue', font_size=15, font_weight='bold')
# nx.draw_networkx_nodes(
#     G_new, pos_new, nodelist=list(nodos_actuales.keys()), node_size=900, node_color='red')
# plt.title(f'Paso a Paso - Nodo Actual: {nodo_actual}')
# plt.axis('off')
# # Posición del botón
# ax_next_button = plt.axes([0.81, 0.02, 0.1, 0.05])
# next_button = Button(ax_next_button, 'Siguiente Nodo')
# next_button.on_clicked(check_nodo_siguiente)

# plt.show()
