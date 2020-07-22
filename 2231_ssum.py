#2231 분해합
#20200721

def ssum(n):

    for i in range(n):
        my_str = str(i)
        sum_my = i

        for k in my_str:
            sum_my += int(k)

        if sum_my == n:
            return i

    return 0
    



n = int(input())
print(ssum(n))
