#2231 분해합
#20200721

def ssum(n):

    for i in range(n): # 0,1,2...n-1
        my_str = str(i) # i를 문자열로 바꾸어 저장
        sum_my = i # 답

        for k in my_str:  # 문자열 안에 있는거 하나씩
            sum_my += int(k)  #정수형으로 바꾸어 sum_my에 더하기

        if sum_my == n: #만약에 sum_my가 답과 같으면 
            return i  # 리턴

    return 0  # 답이 없으면 0리턴
    



n = int(input())
print(ssum(n))
