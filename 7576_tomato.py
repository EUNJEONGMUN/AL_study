#7576 토마토
#20200820

def bfs(a,b):
    global count


    Q = []
    Q.append([a,b])

    while Q:
        q,w = Q[0][0],Q[0][1]
        del Q[0]

        for i in range(4):
            t = q + dx[i]
            g = w + dy[i]

            if 0 <= t < N and 0 <= g < M and tomato[t][g] == 0:
                tomato[t][g] = 1
                Q.append([t,g])
        count+=1
            

M,N = map(int,input().split())
dx = [1,-1,0,0]
dy = [0,0,1,-1]
global count
count = 0
tomato = []
for _ in range(N):
    tomato.append(list(map(int, input().split())))

for a in range(N):
    for b in range(M):
        if tomato[a][b] == 1:
            count+=1
            bfs(a,b)

print(count)
