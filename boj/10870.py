# https://www.acmicpc.net/problem/10870
# 회고: 반복문, dp로 푸는 방식 학습 해야 함

n = int(input())


def fibo(n):
    if n == 0 or n == 1:
        return n

    return fibo(n - 2) + fibo(n - 1)

print(fibo(n))
