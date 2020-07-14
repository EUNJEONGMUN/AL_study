#2775 부녀회장이 될테야


def mom(k,n):
    if n == 1:
        return 1
    num = 1
    mark = k+1
    for i in range(2,n+1):
        num = num + mark
        mark = mark + mark+1
    return num


k = int(input())
n = int(input())
print(mom(k,n))
