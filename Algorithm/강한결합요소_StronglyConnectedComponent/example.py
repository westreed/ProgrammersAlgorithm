
id = 0

def SCC(v:int, graph:list, scc:list, visit:list, d:list, stack:list, node:int):
    global id
    id += 1
    d[node] = id
    stack.append(node)
    parent = d[node]
    for _node in graph[node]:
        if d[_node] == 0:
            parent = min(parent, SCC(v,graph,scc,visit,d,stack,_node))
        elif not visit[_node]:
            parent = min(parent, d[_node])
    
    if parent == d[node]:
        _scc = []
        while True:
            t = stack.pop()
            _scc.append(t)
            visit[t] = True
            if t == node: break
        scc.append(_scc)
    
    return parent



if __name__ == "__main__":
    v = 11
    graph = [[] for _ in range(v+1)]
    scc = []
    d = [0]*(v+1)
    visit = [False]*(v+1)
    stack = []

    graph[1].append(2)
    graph[2].append(3)
    graph[3].append(1)
    graph[4].append(2)
    graph[4].append(5)
    graph[5].append(7)
    graph[6].append(5)
    graph[7].append(6)
    graph[8].append(5)
    graph[8].append(9)
    graph[9].append(10)
    graph[10].append(11)
    graph[11].append(3)
    graph[11].append(8)

    print(graph)
    
    for i in range(1,v+1):
        if d[i] == 0: SCC(v, graph, scc, visit, d, stack, i)
    
    print(scc)