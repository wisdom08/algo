# https://www.acmicpc.net/problem/28702
# 회고: 딕셔너리 활용

x, y, n = map(int, input().split())
for i in range(1, n + 1):
    if i % x == 0 and i % y == 0:
        print("FizzBuzz")
    elif i % x == 0:
        print("Fizz")
    elif i % y == 0:
        print("Buzz")
    else:
        print(i)
