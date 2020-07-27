#1436 영화감독 숌
#20200723

def movie(n):    # n번째 666 들어가는 수 구하기

    number = 665
    count = 0

    while True:
        number+=1
        if '666'in str(number):  #666이 숫자 안에 있으면
            count+=1            #count 증가
        if count == n:     #count가 입력n과 같으면
            print(number)   #출력
            break


n = int(input())
movie(n)
