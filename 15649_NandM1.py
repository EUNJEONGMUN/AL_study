#15649 N과 M(1)
#20200730

# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열


from itertools import permutations

def n_and_m_1(N,M):
    #L = [i for i in range(1,N+1)]  # L = 1,2,3...N


    L = permutations(range(1,N+1),M)

    for i in L:
        print(' '.join(map(str,i)))


N,M = input().split()
N,M = int(N), int(M)

n_and_m_1(N,M)
