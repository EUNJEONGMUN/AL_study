#1018 체스판 다시 칠하기
#20200723

def chess(N,M,L):
    min_count = 64
    
    for a in range(N-7):
        for b in range(M-7):
            count1 = 0
            count2 = 0
            for c in range(a,a+8):
                for d in range(b,b+8):

                    if c%2==0 and d%2==0:
                        if L[c][d]=='B':
                            count1+=1
                    elif c%2==0 and d%2==1:
                        if L[c][d]=='W':
                            count1+=1
                    elif c%2==1 and d%2==0:
                        if L[c][d]=='W':
                            count1+=1
                    else: 
                        if L[c][d]=='B':
                            count1+=1

            for c in range(a,a+8):
                for d in range(b,b+8):

                    if c%2==0 and d%2==0:
                        if L[c][d]=='W':
                            count2+=1
                    elif c%2==0 and d%2==1:
                        if L[c][d]=='B':
                            count2+=1
                    elif c%2==1 and d%2==0:
                        if L[c][d]=='B':
                            count2+=1
                    else:
                        if L[c][d]=='W':
                            count2+=1


            min_count = min(min_count, count1, count2)

    print(min_count)
                        
                



N,M = input().split()
N,M = int(N),int(M)
L = []

for i in range(N):
    L.append(input())

chess(N,M,L)


    
