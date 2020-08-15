#2667 단지 번호 붙이기
#20200811

def solutoin(a,b):
    home_count = 0

    for i in range(a,n):
        for j in range(b,n):

            if i >= n-1 or j >= n-1:
                pass

            
            if mark[i][j] == 'F' and L[i][j] == 1: # 아직 방문하지 않았고, 집이 있을 때
                if mark[i+1][j] == 'F' and L[i+1][j] == 1:
                    mark[i][j] = 'T'
                    home_count+=1
                    
                    sloution(i+1,j)
                elif mark[i][j+1] == 'F' and 
                    
                mark[i][j] = 'T'
                
                

            else:
                if mark[j+1]
                
                
                

    


n = int(input())
L = []
mark = [['F']*n]*n
town = 0
for _ in range(n):
    L.append(list(map(int,input().split())))


solution(0,0)


    
