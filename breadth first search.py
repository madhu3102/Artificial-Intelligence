graph={
    '5':['3','7'],
    '3':['2','4'],
    '7':['8'],
    '2':[],
    '4':['8'],
    '8':[]}
visited=[]
queue=[]
def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)
    while queue:
        m=queue.pop(0)
        print(m,end=" ")
        for neigh in graph[m]:
            if neigh not in visited:
                visited.append(neigh)
                queue.append(neigh)
print("Breadth first search")
bfs(visited,graph,'5')