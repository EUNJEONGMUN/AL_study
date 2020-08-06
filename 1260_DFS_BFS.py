#1260 DFS와 BFS
#20200806

def solution_dfs(N,V,line):
   ''' 
    # line = [[1,2],[1,3],[1,4],[2,4],[3,4]]

    node = []   # 정점의 개수만큼 F  (node = [T,F,F,F])
    move = []   # 내가 움직인 경로
 
    for _ in range(N): 
        node.append('F')

    node[V-1] = 'T' # 시작 정점 'T'로

    state = V  # state - 나의 위치
    move.apped(state)

    while True:
        if 'F' not in node:  #모든 노드를 방문했을 경우 끝
            break

        for i in line:
            if state in i:
   '''             


   graph = [[]]*N


   for i in line:
        graph[i[0]-1].append(i[1])

    print(graph)            
        
        
        

        
    
    
def solution_bfs(N,V,line):
    pass


N,M,V = input().split()
N,M,V = int(N),int(M),int(V)
line = []
for _ in range(M):
    line.append(list(map(int,input().split())))

solution_dfs(N,V,line)
solution_bfs(N,V,line)
    
