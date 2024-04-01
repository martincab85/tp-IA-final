import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
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


def check_nodo_siguiente(ax, canvas, G):
    global nodos_actuales

    nodo_actual = get_actual_node()
    uniones = get_uniones(nodo_actual)

    if nodo_actual != nodo_final:
        while uniones:
            nodo_siguiente = min(uniones) if uniones else None
            if nodo_siguiente not in nodos_sucesores:
                nodos_sucesores.append(nodo_siguiente)

            # Redibujar
            redibujar(ax, canvas, G, nodo_actual, nodo_siguiente)

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


def redibujar(ax, canvas, G, nodo_actual, nodo_siguiente):
    G.add_edge(nodo_actual, nodo_siguiente)

    # Limpiar el eje antes de redibujar el grafo
    ax.clear()
    # Redibujar el grafo con los nodos actuales y las conexiones
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=700,
            edge_color='black', linewidths=1, font_size=10, ax=ax)
    nx.draw_networkx_nodes(G, pos=pos, nodelist=[
                           nodo_inicial], node_color='red', node_size=700, ax=ax)
    nx.draw_networkx_edges(G, pos=pos, edgelist=G.edges(), ax=ax)

    # Actualizar el título del gráfico
    ax.set_title(f'Paso: {len(nodos_actuales)}')

    # Redibujar el lienzo
    canvas.draw()


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

    # Permite mostrar un gráfico creado con matplotlib en una ventana Tkinter.
    canvas = FigureCanvasTkAgg(fig, master=window)
    # Muestra en grafo en la ventana Tkinter
    canvas.draw()
    # canvas.get_tk_widget() devuelve el (canvas) que ha sido creado previamente con FigureCanvasTkAgg. 
    # Este método se utiliza para obtener el widget de lienzo en sí mismo.
    # .pack() es un método que se utiliza para empaquetar el widget en la ventana principal o en otro contenedor de Tkinter.
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


def paso_siguiente(ax, canvas, G):
    check_nodo_siguiente(ax, canvas, G)


def on_closing():
    window.quit()

# Configuración de la ventana principal
# Crea instancia de la grafica de window
window = tk.Tk()
# Asigna un titulo a la ventana
window.title('Visualizador de Grafo')

# Detectar cuando se cierra la ventana
window.protocol("WM_DELETE_WINDOW", on_closing)

# Botón para mostrar paso a paso
btn_mostrar_paso_a_paso = tk.Button(
    window, text="Paso a Paso", command=mostrar_paso_a_paso)
# Hace un marco para el boton de paso a paso
btn_mostrar_paso_a_paso.pack()

# Iniciar el loop de la interfaz
mostrar_grafo_inicial()
window.mainloop()
