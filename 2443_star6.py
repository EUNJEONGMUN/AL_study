#2443 별 찍기
#20200802

def star_6(n):
    for i in range(n,-1,-1):
        print(' '*(n-i)+'*'*(2*i-1))
        


n = int(input())
star_6(n)
