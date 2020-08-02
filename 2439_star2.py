#2439 별 찍기
#20200730

def star_2(n):
    for i in range(n-1,-1,-1):
        print(' '*i+'*'*(n-i))
        


n = int(input())
star_2(n)
