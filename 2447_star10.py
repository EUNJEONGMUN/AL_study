#2447 별 찍기 -10
#20200728
'''
def star_10(n):

    if n == 3:
        print('***')
        print('* *')
        print('***')
        
        for i in range(3):
            if i == 1:
                print('*'*(n//3)+' '*(n//3)+'*'*(n//3))
            else:
                print('*'*n)
        

        print('***'*(n//3))
        print('* *'*(n//3))
        print('***'*(n//3))
        

    
    else:
        star_10(n//3)
        star_10(n//3)
        star_10(n//3)
        star_10(n//3)
        star_10(n//3)
        

            



n = int(input())
star_10(n)
'''

def stars(n):
    matrix=[]
    for i in range(3 * len(n)): # 입력한 수 만큼의 길이
        if i // len(n) == 1:
            matrix.append(n[i % len(n)] + " " * len(n) + n[i % len(n)])
        else:
            matrix.append(n[i % len(n)] * 3)
    return(list(matrix))

star = ["***","* *","***"]
n = int(input())
k = 0
while n != 3:
    n = int(n / 3)
    k += 1
    
for i in range(k):
    star = stars(star)
for i in star:
    print(i)