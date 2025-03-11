# https://www.acmicpc.net/problem/2750
# 회고: sort() 원본값 수정 / sorted() 원본값 수정X

n = int(input())
ns = [int(input()) for _ in range(n)]

print(*sorted(ns), sep="\n")
