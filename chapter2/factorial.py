#순환적인 팩토리얼 알고리즘
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(7))