def dfs(graph, start):

    stack = []
    visited = set()
    stack.append(start)

    visited.add(start)

    while stack:

        vertex = stack.pop()
        
        print(vertex)

        for element in graph[vertex]:
            if element not in visited:
                stack.append(element)
                visited.add(element)

graph = {
    '0': set(['1']),
    '1': set(['0', '2']),
    '2': set(['1', '4', '3']),
    '3': set(['2', '4']),
    '4': set(['2', '3'])
}

dfs(graph, '0')
