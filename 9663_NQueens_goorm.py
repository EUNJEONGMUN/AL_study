def B(k, col): #check if the k-th queen can be placed at (k, col)

    if k == 1:   # k가 1일 때는 무조건 ok
        return True
    else:        # k가 1이 아니라면
        x[k:] = [0]*(len(x)-k)  #x[k] 이후를 우선 0으로 초기화
        
        if col in x:   # 같은 열에 있으면 False
            return False

        mark = 0   # 대각선에 있으면 mark==1 없으면 mark==0
        for t in range(1,k+1): 
            if ((t-1)*n+x[t])==(n*(k-1)+col)-((n+1)*(k-t)) or ((t-1)*n+x[t])==(n*(k-1)+col)-((n-1)*(k-t)):  #대각선에 있는지 확인
                mark = 1

        if mark == 1:   # 대각선에 있으면
            return False  #Flase
        else:               # 대각선에 없으면
            return True        #True
            


def nQueens(k): # decide a valid x[k]
    global sol # sol : 전역 변수로 사용한다는 의미
    if k > n:
        sol += 1 # 해가 하나 발견되어 갯수 증가
        #print(x[1:])
        return

    for col in range(1, n+1):   # 열 하나씩
        if B(k, col):     # 조건에 성립하면
            x[k] = col        # x 에 대입하고
            nQueens(k+1)     # 그 다음 행으로


n = int(input())
x = [0]*(n+1) # 해를 기록
sol = 0 # 해의 개수를 기록
nQueens(1)
print(sol)
