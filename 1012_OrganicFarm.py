#1012 유기농 배추


def bfs(i,j):
    Q = [(i,j)]
    Farm[i][j] = 0

    while Q:
        a,b = Q[0][0], Q[0][1]
        del Q[0]
        for k in range(4):
            x = a + dx[k]
            y = b + dy[k]

            if 0<=x<n and 0<=y<n and Farm[x][y] == 1:
                Farm[x][y] = 0
                Q.append((x,y))


def solution(M,N,Farm):   #가로 M // 세로 N
    count = 0
    for a in range(N):
        for b in range(M):
            if Farm[a][b] == 1:
                count += 1
                bfs(a,b)

    print(count)
    


n = int(input())
dx = [1,-1,0,0]
dy = [0,0,1,-1]

'''
for _ in range(n):
    M,N,K = input().split()
    M,N,K = int(M),int(N),int(K)

    Farm = [[0]*M]*N

    for _ in range(K):
        x,y = input().split()
        x,y = int(x),int(y)
        Farm[y][x] = 1

    solution(M,N,Farm)

'''
M = 5
N = 3
Farm = [[0,0,0,0,1],[0,0,0,0,0],[1,1,1,1,1]]
solution(M,N,Farm)
        
        


    
