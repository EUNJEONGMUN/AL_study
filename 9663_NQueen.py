#9663 N-Queen
#20200805
'''
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
            
'''
n = int(input())

global x
global num
global my_list
my_list = []
num = 0
x = [-1]*n

def NQueens(n,k):
    global x
    global num
    if k>=n:
        if x not in my_list:
            my_list.append(x)
            num+=1
            
            print(x)
            
        return

    for c in range(n):

        # 자신 뒷부분 초기화
        '''
        for m in range(k,len(x)):
            x[m] = -1
        '''
        x[k:] = [-1]*(len(x)-k)
        
        if k==0:
            x[k]=c
            NQueens(n,k+1)
        else:
            if (c not in x) and (x[k-1]!=c-1) and (x[k-1]!=c+1):
                x[k]=c

                for t in range(k):
                    if (t*n+x[t])==(n*k+x[k])-((n+1)*(k-t)) or (t*n+x[t])==(n*k+x[k])-((n-1)*(k-t)):
                        x[k] = -1


                    if x[k] != -1:

                        NQueens(n,k+1)

            
NQueens(n,0)


