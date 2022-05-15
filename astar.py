class Graph:

    def __init__(self, graph):
        self.graph= graph
    def get_neighbours(self, node):
        return self.graph[node]
    def heuristic_function(self, current):
        H={
            'A': 1,
            'B': 2,
            'C': 2,
            'D': 1
        }
        return H[current]
    
    def algorithm(self, start, stop):
        open = set([start])
        close = set()

        g = {}
        g[start] = 0

        parents = {}
        parents[start] = start


        while len(open) > 0:
            current = None
            for node in open:
                #pick a node with lowest f score
                if current == None or g[node] + self.heuristic_function(node) < g[current] + self.heuristic_function(current):
                    current = node
            if current == None:
                print('Path does not exists!')
                return None
            
            #if current is the stop then reconstruct the path
            if current == stop:
                reconstruct_path=[]

                while parents[current] != current:
                    reconstruct_path.append(current)
                    current = parents[current]
                
                reconstruct_path.append(start)
                reconstruct_path.reverse()
                
                print('Path found {}'. format(reconstruct_path))
                return reconstruct_path
            #traverse neighbours
            for (m, weight) in self.get_neighbours(current):
                if m not in open and m not in close:
                    open.add(m)
                    parents[m] = current
                    g[m] = g[current] + weight
                else:
                    if g[m] > g[current] + weight:
                        g[m] = g[current] + weight
                        parents[m] = current

                        if m in close:
                            close.remove(m)
                            open.add(m)
            open.remove(current)
            close.add(current)
        print('Path does not exist!')
        return None

list ={
    'A' : [('B', 1), ('C', 3), ('D', 7)],
    'B' :[('D', 5)],
    'C' :[('D', 12)]
}

graph = Graph(list)
graph.algorithm('A', 'D')







                

    

