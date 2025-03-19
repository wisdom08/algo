# https://www.acmicpc.net/problem/2501
# 회고: 문제를 끝까지 제대로 안 읽어서 len(ns) < k 조건을 놓침

n, k = map(int, input().split())
ns = [i for i in range(1, n+1) if n % i == 0]

if len(ns) < k:
    print(0)
else:
    print(ns[k-1])
