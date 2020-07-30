#14888 연산자 끼워넣기
#20200730

def math_insert(n,num,op):
    my_max = 0
    my_min = 0

    



n = int(input())
num = list(map(int,input().split()))# 숫자의 순서는 바뀌지 않음.
op = list(map(int,input().split())) #    + - *  // 의 개수

math_insert(n,num,op)  #연산자 개수는 숫자 개수보다 하나 적음.
