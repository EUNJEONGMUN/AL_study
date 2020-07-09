#20200709 백준 2839번 설탕 배달


def sugar(n):
    count_3 = 0
    count_5 = 0
    while True:
        
        if n%5==0:
            count_5 = n//5
            n = 0
            break
        n = n - 3
        count_3 += 1

        if n<0:
            break

    if n == 0:
        return count_3+count_5
    else:
        return -1


n = int(input())
print(sugar(n))

    

