#2869 달팽이는 올라가고 싶다
#20200714
'''
def snail(A,B,V):
    day = 0
    h = 0
    while True:
        h += A
        day += 1

        if h >= V:
            return day
        h -= B
    '''

def snail(A,B,V):
    day = 0
    h = 0
    
    while h<V:
        h += A
        day += 1
        if h<V:
            h -= B

    return day
        

A,B,V = input().split()
A = int(A)
B = int(B)
V = int(V)

print(snail(A,B,V))
