# Djikistra's Algorithm


def shortest_paths(graph, source):
    min_paths = {node: float("inf") for node in graph.keys()}

    # the minimum path to the source node must be zero
    min_paths[source] = 0

    visited = set()
    
    def dfs(node):
        if node in visited:
            return
        
        visited.add(node)
        for nei, dist in graph[node].items():
            if nei not in visited:
                min_paths[nei] = min(
                    min_paths[nei],
                    min_paths[node] + dist,
                )
                dfs(nei)
    
    return min_paths

if __name__ == "__main__":
    graph = {
        0: {1: 4, 2: 1}, 
        1: {3: 1}, 
        2: {1: 2, 3: 5}, 
        3: {}
    }

    sp = shortest_paths(graph, 0)
    print(sp)


        