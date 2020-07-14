#2775 부녀회장이 될테야
'''

def mom(k,n):
    if n == 1:
        return 1
    num = 1
    mark = k+1
    for i in range(2,n+1):
        num = num + mark
        mark = mark + mark+1
    return num

'''

def mom(k,n):
    L = [i for i in range(15)]  #[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    
    for cmd in range(k):
        for gh in range(1,n+1):
            L[gh] = L[gh-1]+L[gh]

    print(L[n])

count = int(input())
for i in range(count):
    k = int(input())
    n = int(input())
    mom(k,n)
