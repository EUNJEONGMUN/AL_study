#15649 N과 M(1)-1
#20200803


N,M = map(int, input().split())
visited = [False]*N
out = []

def solve(depth,N,M):
    if depth == M:
        print(' '.join(map(str, out)))
        return

    for i in range(len(visited)):
        if not visited[i]:
            visited[i] = True
            out.append(i+1)
            solve(depth+1,N,M)
            visited[i] = False
            out.pop()

solve(0,N,M)
