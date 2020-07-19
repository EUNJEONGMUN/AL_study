#2798 블랙잭
#20200716
'''
def blackjack(n,A,M):
    A.sort()
    p,q,r=0,1,2
        
    while A[p]+A[q]+A[r]<M and p<q<r<n:
        if r!=n-1:
            r+=1
            if A[p]+A[q]+A[r]>M:
                return A[p]+A[q]+A[r-1]
        elif q!=r-1:
            q+=1
            if A[p]+A[q]+A[r]>M:
                return A[p]+A[q-1]+A[r]
        else:
            p+=1
            if A[p]+A[q]+A[r]>M:
                return A[p-1]+A[q]+A[r]


    return A[p]+A[q]+A[r]
'''
def blackjack2(n,A,M):
    A.sort()
    p,q,r = 0,1,2

    while A[p]+A[q]+A[r]<M and p<q<r<n:
        r+=1
        if A[p]+A[q]+A[r]>M:
            return A[p]+A[q]+A[r-1]
        q+=1
        if A[p]+A[q]+A[r]>M:
            return A[p]+A[q-1]+A[r]
        
        p+=1
        if A[p]+A[q]+A[r]>M:
            return A[p-1]+A[q]+A[r]


    return A[p]+A[q]+A[r]






n,M = input().split()
n,M = int(n), int(M)
A = list(map(int, input().split()))
print(blackjack(n,A,M))
        
        

    
