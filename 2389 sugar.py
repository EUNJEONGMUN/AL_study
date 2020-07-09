#20200709 백준 2839번 설탕 배달


def sugar(n):
    count_3 = 0
    count_5 = 0
    mark = 0
    while n>2:
        if n%8==0:
            count_3 = count_5 = n//8
            n = 0
            break
        
        elif n%5==0:
            count_5 = n//5
            n = 0
            break
        
        elif n%3 == 0 and (n//3)<5:
            count_3 = n//3
            n = 0
            break

        else:
            if mark == 0:
                count_5 = count_5 + n//5
                n = n%5
            

        if n%3==0:
            count_3 = count_3 + n//3
            n = 0
            break

        elif (n==1) and (mark == 0):
            n += 5
            count_5 -= 1
            mark = 1

        else:
            break




    if n == 0:
        return count_3+count_5
    else:
        return -1


n = int(input())
print(sugar(n))

    

