#1978 소수 찾기
#20180716

def prime(n,A):
    count = 0
    for i in A:
        if i == 1:
            mark = 1
        else:
            mark = 0
        for k in range(2, i):
            if i % k == 0 or i==1:
                mark = 1
        if mark == 0:
            count += 1

    return count

n = int(input())
A = list(map(int, input().split()))
print(prime(n,A))

        
