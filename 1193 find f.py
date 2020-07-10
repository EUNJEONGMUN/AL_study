#20200709 1193 분수찾기

def find_f(n):
    first = 1
    second = 1
    count = 1

    while count!=n:
        if (first==1) and (second%2==1):
            second += 1
            mark = 0  #0 -> down
        elif (second == 1) and (first%2==0):
            first += 1
            mark = 1  #1 -> up

        elif mark==0:
            first += 1
            second -= 1
        else:
            first -= 1
            second += 1
        count += 1

    print(first,second,sep='/')




n = int(input())
find_f(n)
