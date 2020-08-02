#2445 별 찍기
#20200802

def star_8(n):
    for i in range(1,n+1):
        print('*'*i+' '*(2*(n-i))+'*'*i)
    for i in range(1,n+1):
        print('*'*(n-i)+' '*(i*2)+'*'*(n-i))
        


n = int(input())
star_8(n)
