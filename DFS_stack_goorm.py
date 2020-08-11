#dfs stack

def dfs(s):
    stack = []
    stack.append((None,s))
    while len(stack) != 0:
        p,v = stack.pop()
        if mark[v] == 'unvisited':
            mark[v] = 'visited'
            print(v)
            parent[v] = p

           

            for i in edge:
                if v in i:
                    if i[0] == v:
                        if mark[i[1]]=='unvisited':
                            stack.append(i)
                    else:
                        if mark[i[0]]=='unvisited':
                            stack.append(i)



N,M,V = input().split()
N,M,V = int(N),int(M),int(V)

mark = ['unvisited']*(N+1)
parent = [0]*(N+1)

edge = []


for _ in range(M):
    edge.append(tuple(map(int,input().split())))

edge.sort(reverse=True) # stack 기능을 해야하므로 역순 정렬


dfs(V)
