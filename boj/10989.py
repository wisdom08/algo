# https://www.acmicpc.net/problem/10989
# 회고: 숫자 범위 제한적(10,000)이고 데이터 개수가 매우 많음(10,000,000)
import sys

n = int(input())

count = [0] * 10001

for i in range(n):
    count[int(sys.stdin.readline())] += 1

for i in range(len(count)):
    if count[i] != 0:
        for _ in range(count[i]):
            print(i)