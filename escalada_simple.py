import networkx as nx
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox

def draw_graph(num_nodes, start_node, end_node):
    # Crear un grafo
    G = nx.Graph()

    # Añadir nodos
    nodes = [chr(65 + i) for i in range(num_nodes)]
    G.add_nodes_from(nodes)

    # Añadir uniones con pesos (ejemplo de uniones aleatorias)
    import random
    for i in range(num_nodes):
        for j in range(i+1, num_nodes):
            G.add_edge(nodes[i], nodes[j], weight=random.randint(1, 10))

    # Dibujar el grafo
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=900, node_color="skyblue", labels={node: node for node in G.nodes()})
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): d['weight'] for u, v, d in G.edges(data=True)})

    # Pintar nodos inicial y final
    if start_node:
        nx.draw_networkx_nodes(G, pos, nodelist=[start_node], node_color='red', node_size=900)
    if end_node:
        nx.draw_networkx_nodes(G, pos, nodelist=[end_node], node_color='green', node_size=900)

    plt.show()

def on_submit():
    try:
        num_nodes = int(entry_num_nodes.get())
        
        if num_nodes < 2:
            messagebox.showerror("Error", "La cantidad de nodos debe ser al menos 2.")
            return

        # Definir la lista de nodos dentro de on_submit()
        nodes = [chr(65 + i) for i in range(num_nodes)]

        start_node = entry_start_node.get().upper()
        end_node = entry_end_node.get().upper()

        if start_node not in nodes or end_node not in nodes:
            messagebox.showerror("Error", "Los nodos de inicio o fin no están en el grafo.")
            return

        draw_graph(num_nodes, start_node, end_node)

    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese un número válido para la cantidad de nodos.")

# Crear ventana
window = tk.Tk()
window.title("Cargar Grafo")

# Etiqueta y entrada para la cantidad de nodos
label_num_nodes = tk.Label(window, text="Cantidad de nodos:")
label_num_nodes.grid(row=0, column=0)
entry_num_nodes = tk.Entry(window)
entry_num_nodes.grid(row=0, column=1)

# Etiqueta para el nodo inicial
label_start_node = tk.Label(window, text="Nodo inicial:")
label_start_node.grid(row=1, column=0)
entry_start_node = tk.Entry(window)
entry_start_node.grid(row=1, column=1)

# Etiqueta para el nodo final
label_end_node = tk.Label(window, text="Nodo final:")
label_end_node.grid(row=2, column=0)
entry_end_node = tk.Entry(window)
entry_end_node.grid(row=2, column=1)

# Botón para cargar el grafo
submit_button = tk.Button(window, text="Cargar Grafo", command=on_submit)
submit_button.grid(row=3, columnspan=2)

# Mostrar la ventana
window.mainloop()
