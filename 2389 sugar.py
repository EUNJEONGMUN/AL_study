#20200709 백준 2839번 설탕 배달


def sugar(n):
    count_3 = 0
    count_5 = 0
    while n>2:
        if n%8==0:
            count_3 = count_3 + n//8
            count_5 = count_5 + n//8
            n = n%8
            break
        
        elif n%5==0:
            count_5 = count_5 + n//5
            n = n%5
            break

        n = n%5
        count_5 = n//5

        if n
        if n%3==0:
            count_3 = count_3 + n//3
            n = n%3




    if n == 0:
        return count_3+count_5
    else:
        return -1


n = int(input())
print(sugar(n))

