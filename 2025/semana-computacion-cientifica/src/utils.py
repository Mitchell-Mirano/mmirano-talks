from graphviz import Digraph

def draw_forward(root):
    """
    Visualiza el grafo computacional generado a partir de un tensor.
    """
    dot = Digraph(format='png', graph_attr={'rankdir': 'LR'})  # de izquierda a derecha
    nodes, edges = set(), set()

    def add_nodes_edges(t):
        if id(t) not in nodes:
            nodes.add(id(t))
            op_str = f"({t._op})=" if t._op else ''
            label = f"{op_str}{t.data}"
            dot.node(str(id(t)), label, shape='record')
            for child in getattr(t, "_prev", []):
                edges.add((id(child), id(t)))
                add_nodes_edges(child)

    add_nodes_edges(root)

    for n1, n2 in edges:
        dot.edge(str(n1), str(n2))

    return dot

def draw_backward(root):
    """
    Visualiza el grafo computacional generado a partir de un tensor,
    con las flechas invertidas (de adelante hacia atrás).
    """
    dot = Digraph(
        format='png',
        graph_attr={'rankdir': 'RL'}  # orientación derecha→izquierda
    )

    nodes, edges = set(), set()

    def add_nodes_edges(t):
        if id(t) not in nodes:
            nodes.add(id(t))
            op_str = f"({t._op})=" if getattr(t, "_op", None) else ''
            label = f"{op_str}{t.grad}"
            dot.node(str(id(t)), label, shape='record')

            for child in getattr(t, "_prev", []):
                edges.add((id(t), id(child)))  # ← invertimos la dirección
                add_nodes_edges(child)

    add_nodes_edges(root)

    for n1, n2 in edges:
        dot.edge(str(n1), str(n2))

    return dot

