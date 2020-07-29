#11650 좌표 정렬하기
#20200728

def xy_sort(L):

    for i in range(len(L)-1,-1,-1):
        for j in range(i):
            if L[j][0]>L[j+1][0]:
                L[j],L[j+1] = L[j+1],L[j]
            elif L[j][0]==L[j+1][0]:
                if L[j][1]>L[j+1][1]:
                    L[j],L[j+1] = L[j+1],L[j]

    for i in range(len(L)):
        print(L[i][0],L[i][1])
                    

            

    



n = int(input())
L = []
for i in range(n):
    x,y = input().split()
    x,y = int(x),int(y)
    L.append((x,y))

xy_sort(L)

    

    
