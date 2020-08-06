#9663 N-Queen
#20200805

def solution(n):

    L = [['F'*n]*n]
    count = 0

    while True:
        if 'F' not in L:
            break
        
        

    for a in range(n):
        for b in range(n):
            if L[a][b] == 'F':
                L[a]= 'T'*n
                
                
            count+=1
            


n = int(input())
solution(n)
