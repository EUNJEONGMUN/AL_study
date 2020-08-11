#2606 바이러스
#20200811

def dfs(v):  # v : 각 노드
    global count
    mark[v] = 'visited'
    #print(v, end=' ')
    count+=1

    for i in edge:
        if v in i:
            if i[0] == v:s
                if mark[i[1]]=='unvisited':

                    dfs(i[1])
            else:
                if mark[i[0]]=='unvisited':

                    dfs(i[0])
 
    


N = int(input())
M = int(input())
edge = []
node = [i for i in range(1,N+1)]  # node = [1,2,3,4]
mark = ['unvisited']*(N+1)  # mark = ['unvisited','unvisited','unvisited'...]
for _ in range(M):
    edge.append(tuple(map(int,input().split())))

edge.sort()

global count
count = -1
dfs(1)
print(count)
