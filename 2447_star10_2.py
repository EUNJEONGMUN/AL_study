#2447
#internet

def con(r1,r2):
    return [' '.join(x) for x in zip(r1,r2,r1)]

def star10(n):
    if n == 1:
        return ['*']

    n //=3
    x = star10(n)
    a = con(x,x)
    b = con(x,[''*n]*n)

    return a+b+a


print('\n'.join(star10(int(input()))))
