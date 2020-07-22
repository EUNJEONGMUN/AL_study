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


'''


def blackjack3(n,A,M):
    sum_my = 0   # 세 수의 합
    for i in range(n-2): #첫 번째 원소
        for j in range(i+1,n-1): # 두 번째 원소
            for k in range(j+1,n): # 세 번째 원소
                if A[i]+A[j]+A[k]<=M: # 합이 M보다 같거나 작다면
                    sum_my = max(sum_my,A[i]+A[j]+A[k]) #원래 sum_my에 있던 수와 비교하여 더 큰수를 sum_my에 저

    return sum_my

            
            

n,M = input().split()
n,M = int(n), int(M)
A = list(map(int, input().split()))
print(blackjack3(n,A,M))
        
        

    
