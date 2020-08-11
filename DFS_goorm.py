# DFS
# 20200811

def dfs(v):  # v : 각 노드
    global curr_time
    mark[v] = 'visited'
    print(v, end=' ')

    pre[v] = curr_time
    curr_time += 1

    for i in edge:
        if v in i:
            if i[0] == v:
                if mark[i[1]]=='unvisited':
                    parent[i[1]] = v
                    #print(i[1])
                    dfs(i[1])
            else:
                if mark[i[0]]=='unvisited':
                    parent[i[0]] = v
                    #print(i[0])
                    dfs(i[0])
    post[v] = curr_time
    curr_time += 1

    

def dfsAll(G):  # G = [1,2,3,4]
    for node in G:
        if mark[node] == 'unvisited':
            dfs(node)

    print()
    print(pre)
    print(post)

    



N,M,V = input().split()
N,M,V = int(N),int(M),int(V)
edge = []
node = [i for i in range(1,N+1)]  # node = [1,2,3,4]
parent = [0]*(N+1)  # parend = [0,0,0,0,0] 
mark = ['unvisited']*(N+1)  # mark = ['unvisited','unvisited','unvisited'...]
for _ in range(M):
    edge.append(tuple(map(int,input().split())))

edge.sort()

pre = [0]*(N+1)
post = [0]*(N+1)
global curr_time
curr_time = 1

dfsAll(node)
