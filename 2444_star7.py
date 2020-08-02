#2444 별 찍기
#20200802

def star_7(n):
    for i in range(1,n+1):
        print(' '*(n-i)+'*'*(2*i-1))
    for i in range(n-1,0,-1):
        print(' '*(n-i)+'*'*(2*i-1))
    
        


n = int(input())
star_7(n)
