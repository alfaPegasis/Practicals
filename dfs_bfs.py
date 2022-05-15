#create graph
from inspect import stack


graph = {
    'A' : ['B', 'D'],
    'B' : ['C'],
    'C' : ['E', 'G'],
    'D' : [],
    'E' : ['F'],
    'F' : [],
    'G' : []
}

def depth_first_search(graph, source):
    stack = [source]
    result = []
    while len(stack) > 0:
        current = stack.pop()
        result.append(current)
        for neighbours in graph[current]:
            stack.append(neighbours)
    return result

def breadth_first_search(graph, source):
    queue = [source]
    result = []
    while len(queue) > 0:
        current = queue.pop(0)
        result.append(current)
        for neighbours in graph[current]:
            queue.append(neighbours)
    return result

print(depth_first_search(graph, 'A'))
print(breadth_first_search(graph, 'A'))