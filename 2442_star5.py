#2442 별 찍기
#20200730

def star_5(n):
    for i in range(1,n+1):
        print(' '*(n-i)+'*'*(2*i-1))
        


n = int(input())
star_5(n)
