#14888 연산자 끼워넣기
#20200730

from itertools import permutations


def math_insert(n,num,op):

    my_max = []
    
    OP = []
    for _ in range(op[0]):
        OP.append('+')
    for _ in range(op[1]):
        OP.append('-')
    for _ in range(op[2]):
        OP.append('*')
    for _ in range(op[3]):
        OP.append('/')

    my_op = list(permutations(OP,len(OP))) # my_op 연산자 수열


    for a in range(len(my_op)): #a -> 0 1 2 3 4.....60
       
        my_answer = num[0]  #첫번째숫자 int
        
        for b in range(n-1):  # b -> 0 1 2 3 4 5
            if my_op[a][b] == '+':
                my_answer += num[b+1]
            elif my_op[a][b] == '-':
                my_answer -= num[b+1]
            elif my_op[a][b] == '*':
                my_answer *= num[b+1]
            elif my_op[a][b] == '/' and my_answer<0:
                temp = -num[b+1]
                my_answer = my_answer // temp
                my_answer = -my_answer
            elif my_op[a][b] == '/' and my_answer>0:
                my_answer = my_answer // num[b+1]

        my_max.append(my_answer)
        

    print(max(my_max), min(my_max))
   



n = int(input())
num = list(map(int,input().split()))# 숫자의 순서는 바뀌지 않음.
op = list(map(int,input().split())) #    + - *  // 의 개수

math_insert(n,num,op)  #연산자 개수는 숫자 개수보다 하나 적음.
