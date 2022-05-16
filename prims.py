INF = 999999
vertices = 5 #number of vertices
#create a graph
graph = [[0, 9, 75, 0, 0],
     [9, 0, 95, 19, 42],
     [75, 95, 0, 51, 66],
     [0, 19, 51, 0, 31],
     [0, 42, 66, 31, 0]]

selected = [0, 0, 0, 0, 0]
count = 0
#choose 0th vertex and make it True
selected[0] = True
print('Edge : Weight\n')
while count< vertices -1:
    minimum = INF
    x = 0
    y = 0
    for i in range(vertices):
        #select the vertex
        if selected[i]:
            #loop through its neighbours
            for j in range(vertices):
                #if neighbours not selected and their exists an edge
                if (not selected[j]) and graph[i][j]:
                    #check if it is smaller than the minimum and if it is make it the minimum
                    if minimum > graph[i][j]:
                        minimum = graph[i][j]
                        #store its position in x and y
                        x = i
                        y = j
    #print the positions 
    print(str(x) + '-' + str(y) + ' : ' + str(graph[x][y]))
    selected[y] = True
    count += 1
