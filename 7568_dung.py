#7568 덩치
#20200723

def dung(n, L):
    for i in range(n):
        rank = 0
        my_w = L[i][0]
        my_h = L[i][1]

        for j in range(n):
            if i!=j:
                if (L[j][0]>my_w) and (L[j][1]>my_h):
                    rank += 1

        print(rank+1, end=" ")
    
        
    


n = int(input())
L = []
for i in range(n):
    w,h = input().split()
    w, h = int(w), int(h)

    L.append((w,h))

dung(n, L)
