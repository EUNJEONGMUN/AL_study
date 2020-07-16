#2581 소수2
#20200716

def prime2(start, end):
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
    if len(P)==0:
        print(-1)
    else:
        sum_P = sum(P)
        min_P = P[0]
        for i in range(1, len(P)):
            if P[i]<min_P:
                min_P = P[i]

        print(sum_P)
        print(min_P)
    

    

start = int(input())
end = int(input())
prime2(start,end)
