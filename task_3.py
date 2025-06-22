import heapq


def dijkstra(graph, start):
    """Ініціалізуємо відстані як нескінченність"""
    distances = {vertex: float("inf") for vertex in graph}
    """ Відстань до початкової вершини = 0 """
    distances[start] = 0

    """(відстань, вершина)"""
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        """Якщо поточна відстань більша за збережену, пропускаємо"""
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            """Якщо знайдено коротший шлях — оновлюємо"""
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# Представлення графа у вигляді словника
graph = {
    "A": {"B": 5, "C": 1},
    "B": {"A": 5, "C": 2, "D": 1},
    "C": {"A": 1, "B": 2, "D": 4, "E": 8},
    "D": {"B": 1, "C": 4, "E": 3, "F": 6},
    "E": {"C": 8, "D": 3},
    "F": {"D": 6},
}

# Знайдемо найкоротші відстані від вершини 'A'
shortest_paths = dijkstra(graph, "A")

for vertex, distance in shortest_paths.items():
    print(f"Відстань від A до {vertex}: {distance}")
