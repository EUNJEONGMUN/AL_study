#2441 별 찍기
#20200730

def star_4(n):
    for i in range(n):
        print(' '*i+'*'*(n-i))
        


n = int(input())
star_4(n)
