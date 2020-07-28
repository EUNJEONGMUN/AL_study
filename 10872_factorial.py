#10872 팩토리얼
#20200728

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n*factorial(n-1)




n = int(input())
print(factorial(n))
