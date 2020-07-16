#1929 소수구하기
#20200716

def prime3(start, end):
    P = []
    for i in range(start, end+1):
        if i == 1:
            mark = 1
        else:
            mark = 0
        for k in range(2, i):
            if i % k == 0 or i==1:
                mark = 1
        if mark == 0:
            P.append(i)
            
    for i in range(len(P)):
        print(P[i])

    

start,end = input().split()
start, end = int(start), int(end)
prime3(start,end)
