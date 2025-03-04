
def dfs(graph, start):
    visited = set()  
    stack = [start]
    
    while stack:
        node = stack.pop()
        
        if node not in visited:
            print(node, end=" ")  
            visited.add(node)  
            
            # Push all adjacent nodes to the stack in reverse order (to visit them correctly)
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}


dfs(graph, 'A')
