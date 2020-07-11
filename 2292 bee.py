def bee(n):
    if n == 1:
        return 1
    count = 0
    while True:
        start = (6*count*(count+1)/2)+2
        finish  = (6*(count+1)*(count+2)/2)+1

        if(start >= n) and (finish <= n):
            break
        else:
            count += 1

    return count+1


n = int(input())
print(bee(n))
