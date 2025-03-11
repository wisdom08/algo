# https://www.acmicpc.net/problem/2587
# 회고: ns 입력 받을 때 sorted() 처리를 할 수도 있음

ns = [int(input()) for _ in range(5)]

print(sum(ns)//5)
print(sorted(ns)[2])