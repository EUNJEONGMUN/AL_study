#2750 수 정렬하기
#20200721

def sort_n2(n,L):
    for i in range(n-1,-1,-1):
        for j in range(0,i):
            if L[j]>L[j+1]:
                L[j],L[j+1] = L[j+1],L[j]

    for m in L:
        print(m)


    

n = int(input())
L = []
for i in range(n):
    k = int(input())
    L.append(k)


sort_book(n,L)




    
