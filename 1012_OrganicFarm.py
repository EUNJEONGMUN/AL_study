#1012 유기농 배추


def bfs(i,j):
    Q = [(i,j)]

    while Q:
        a,b = Q[0][0], Q[0][1]
        del Q[0]
        for k in range(4):
            x = a + dx[k]
            y = b + dy[k]

            if 0<=x<N and 0<=y<M and Farm[x][y] == 1:
                Farm[x][y] = 0
                Q.append((x,y))


n = int(input())
dx = [1,-1,0,0]
dy = [0,0,1,-1]

for _ in range(n):
    M,N,K = input().split()
    M,N,K = int(M),int(N),int(K)

    Farm = [[0]*M for _ in range(N)]
    count = 0

    for _ in range(K):
        a,b = map(int,input().split())
        Farm[b][a] = 1

    for x in range(N):
        for y in range(M):
            if Farm[x][y] == 1:
                bfs(x,y)
                Farm[x][y] = 0
                count += 1

    print(count)
        





    
