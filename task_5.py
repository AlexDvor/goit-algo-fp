import uuid
import networkx as nx
import matplotlib.pyplot as plt
import colorsys
from collections import deque


class Node:
    def __init__(self, key, color="#87CEEB"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2**layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree_dynamic(tree_root, title="Tree"):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    plt.title(title)
    nx.draw(
        tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors
    )
    plt.show()


# 🔵 Генерація кольорів від темних до світлих
def generate_color_palette(n):
    colors = []
    for i in range(n):
        hue = 0.58  # синій
        saturation = 0.7 - (i / n) * 0.5
        value = 0.5 + (i / n) * 0.5
        rgb = colorsys.hsv_to_rgb(hue, saturation, value)
        hex_color = "#%02x%02x%02x" % tuple(int(255 * x) for x in rgb)
        colors.append(hex_color)
    return colors


#  Обхід у глибину (DFS) — за допомогою стеку
def dfs_iterative(root):
    stack = [root]
    visited = []
    colors = generate_color_palette(100)

    index = 0
    while stack:
        node = stack.pop()
        if node not in visited:
            node.color = colors[index]
            visited.append(node)
            draw_tree_dynamic(root, f"DFS: Step {index+1}")
            index += 1
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)


#  Обхід у ширину (BFS) — за допомогою черги
def bfs_iterative(root):
    queue = deque([root])
    visited = []
    colors = generate_color_palette(100)

    index = 0
    while queue:
        node = queue.popleft()
        if node not in visited:
            node.color = colors[index]
            visited.append(node)
            draw_tree_dynamic(root, f"BFS: Step {index+1}")
            index += 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


# Побудова дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Запуск обходів
print("📘 DFS (в глибину):")
dfs_iterative(root)

# Після DFS кольори змінені — перевизначаємо
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

print("📗 BFS (в ширину):")
bfs_iterative(root)
