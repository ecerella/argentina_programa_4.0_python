import networkx as nx
import matplotlib.pyplot as plt

# Definir una función recursiva para crear un árbol binario con los valores de Fibonacci
def fibonacci_tree(n):
    if n <= 0:
        return None
    elif n == 1:
        return nx.Graph([(0, None)])
    elif n == 2:
        return nx.Graph([(0, 1)])
    else:
        G = fibonacci_tree(n - 1)
        leaf_nodes = list(G.nodes)
        new_node = max(leaf_nodes) + 1
        G.add_edge(new_node, leaf_nodes[-1])
        return G

# Solicitar al usuario ingresar el valor máximo
max_value = int(input("Ingrese el valor máximo para la secuencia de Fibonacci: "))

# Definir una función para calcular la secuencia de Fibonacci hasta un valor máximo
def fibonacci(max_value):
    sequence = [0, 1]
    while sequence[-1] + sequence[-2] <= max_value:
        next_value = sequence[-1] + sequence[-2]
        sequence.append(next_value)
    return sequence

# Obtener un árbol con los valores de Fibonacci hasta el valor máximo
fibonacci_sequence = fibonacci(max_value)
fibonacci_tree_graph = fibonacci_tree(max_value)

# Dibujar el árbol
pos = nx.spring_layout(fibonacci_tree_graph)
nx.draw(fibonacci_tree_graph, pos, with_labels=True, node_size=500, node_color='skyblue')
labels = {node: val for node, val in zip(fibonacci_tree_graph.nodes, fibonacci_sequence)}
nx.draw_networkx_labels(fibonacci_tree_graph, pos, labels=labels)
plt.title(f"Árbol de Fibonacci hasta el valor {max_value}")
plt.show()