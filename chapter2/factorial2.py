#반복구조의 팩토리얼 알고리즘
def factorial(n):
    result = 1
    for k in range(n,0,-1):
        result = result*k
    return result