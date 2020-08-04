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

    my_op = permutations(OP,len(OP)) # 연산자 수열

    MMYY_OOPP = []
    

    for i in my_op:
        MMYY_OOPP.append(''.join(map(str,i)))


    for a in range(len(MMYY_OOPP)): #a -> 0 1 2 3 4.....60
        answer = 0
        my_answer = num[0]  #첫번째숫자 문자열
        for b in range(n-1):  # b -> 0 1 2 3 4
            if MMYY_OOPP[a][b] == '/' and int(num[b+1])<0:
                temp = int(num[b+1])
                my_answer += '//'+str(-temp)

                answer = eval(my_answer)
                my_answer = str(-answer)
                continue
            elif MMYY_OOPP[a][b] == '/' and int(num[b+1])>0:
                my_answer += '//'+num[b+1]
                
            else:
                my_answer += MMYY_OOPP[a][b]+num[b+1]

            answer = eval(my_answer)
            my_answer = str(answer)

        my_max.append(int(my_answer))
        

    print(max(my_max), min(my_max))
   



n = int(input())
num = list(map(str,input().split()))# 숫자의 순서는 바뀌지 않음.
op = list(map(int,input().split())) #    + - *  // 의 개수

math_insert(n,num,op)  #연산자 개수는 숫자 개수보다 하나 적음.
