#14889 스타트와 링크
#20200804
import itertools 

def solution(n,T):

    member = list(itertools.combinations(range(1,n+1),n//2))
    score = []

    for i in range(len(member)):
        my_mem = list(itertools.permutations(member[i],2))  # my_mem -> 팀 안에서 멤버를 2명씩 뽑음
        answer = 0
        for k in range(len(my_mem)):  
            answer += T[my_mem[k][0]-1][my_mem[k][1]-1]
        score.append(answer)

    min_score = []
    for i in range(len(score)//2):

        min_score.append(abs(score[i]-score[len(score)-i-1]))
        '''
        if score[i]>score[len(score)-i-1]:
            min_score.append(score[i]-score[len(score)-i-1])
        else:
            min_score.append(score[len(score)-i-1]-score[i])
        '''

    print(min(min_score))

    



n = int(input())  #n명
T = []
for i in range(n):
    T.append(list(map(int,input().split())))

solution(n,T)
