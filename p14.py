import networkx as nx

G = nx.DiGraph()
n = 1000000
G.add_nodes_from([i for i in range(1,n)])
for i in [n for n in G]:
    if i%100000 == 0:
        print(i)
    if i%2 == 0:
        G.add_edge(i,i//2)
    else:
        G.add_edges_from([(i,3*i+1)])
        if (3*i+1) >= n:
            z = 3*i+1
            while z >= n:
                if z%2 == 0:
                    G.add_edge(z,z//2)
                    z = z//2
                else:
                    G.add_edge(z,3*z+1)
                    z = 3*z+1
paths = nx.shortest_path(G, target = 1)
#print(paths)
#for n in G.nodes:
#    print(n, paths[n], len(paths[n]))
max = 1
index = 1
for i in [x for x in G]:
    #if i < n:
    #    print(i)
    if i < n:
        if len(paths[i]) > max:
            max = len(paths[i])
            index = i
            #print(index, max, paths[i])
print(index, max)