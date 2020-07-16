#4948 베르트랑 공준
#20200716

def prime4(n):
    count = 0
    for i in range(n+1,2*n+1):
        if i == 1:
            mark = 1
        else:
            mark = 0
        for k in range(2, i):
            if i % k == 0 or i==1:
                mark = 1
        if mark == 0:
            count += 1

    return print(count)




while True:
    n = int(input())
    if n!=0:
        prime4(n)
    else:
        break
