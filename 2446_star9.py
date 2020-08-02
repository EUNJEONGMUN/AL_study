#2446 별 찍기
#20200802

def star_9(n):
    for i in range(n,0,-1):
        print(' '*(n-i)+'*'*(i*2-1))
    for i in range(2,n+1):
        print(' '*(n-i)+'*'*(i*2-1))
        


n = int(input())
star_9(n)
