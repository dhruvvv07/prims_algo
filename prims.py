def prim_mst(graph, start='A'):
    visited = set([start])
    mst = []

    while len(visited) < len(graph):
        min_edge = None
        min_weight = float('inf')  

        for u in visited:
            for v, weight in graph[u]:
                if v not in visited and weight < min_weight:
                    min_edge = (u, v, weight)
                    min_weight = weight

        if min_edge:
            u, v, weight = min_edge
            visited.add(v)
            mst.append((u, v, weight))
        else:
            break  
    return mst

graph = {
    'A': [('B', 9), ('C', 4)],
    'B': [('C', 2), ('E', 7), ('A', 9), ('D', 1)],
    'C': [('D', 4), ('A', 4), ('B', 2), ('F', 3)],
    'D': [('B', 1), ('E', 2), ('F', 5), ('C', 4)],
    'E': [('B', 7), ('D', 2), ('F', 6), ('G', 3)],
    'F': [('D', 5), ('E', 6), ('G', 8), ('H', 5)],
    'G': [('E', 3), ('F', 8), ('H', 1), ('I', 3)],
    'H': [('F', 5), ('G', 1), ('I', 2)],
    'I': [('G', 3), ('H', 2)]
}

mst = prim_mst(graph)

print("Minimum Spanning Tree:")
for u, v, w in mst:
    print(f"{u} - {v}: {w}")
