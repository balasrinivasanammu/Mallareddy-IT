def validPath(n, edges, start, end):
    
    graph = {i: [] for i in range(n)}
    for a, b in edges:
        print(a,b)
        graph[a].append(b)
        graph[b].append(a)

   
    def dfs(node):
        print(node)
        if node == end:
            return True
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
        return False

    visited = set()  
    return dfs(start)


n = 6  # Number of nodes (0 to 5)
edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
start = 0
end = 5
print(validPath(n, edges, start, end))  # Output: True
