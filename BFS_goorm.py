#BFS
#20200811

def bfs(G):  # G = [1,2,3,4,5,6,7,8]
    visited = [False]*(N+1)
    parent = [-1]*(N+1)
    dist = [0]*(N+1)
    Q = []

    for s in G:
        if visited[s] == False:
            Q.append(s)
            visited[s] = True
            while len(Q)!=0:
                v = Q.pop(0)
                print(v)
                for i in edge:
                    if v in i:
                        if v == i[0]:

                            if visited[i[1]]==False:
                                Q.append(i[1])
                            
                                visited[i[1]]=True
                            
                                parent[i[1]]=v
                                dist[i[1]] = dist[v]+1 
                        else:
                            if visited[i[0]]==False:
                                Q.append(i[0])
                            
                                visited[i[0]]=True
                            
                                parent[i[0]]=v
                                dist[i[0]] = dist[v]+1

        

N,M,V = input().split()
N,M,V = int(N),int(M),int(V)

node = [i for i in range(1,N+1)]
        
edge = []

for _ in range(M):
    edge.append(tuple(map(int,input().split())))

edge.sort()

bfs(node)
