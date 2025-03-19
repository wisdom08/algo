# https://www.acmicpc.net/problem/1292
# 회고: 리스트 슬라이싱으로 한 줄로도 풀 수 있음
# 문제 조건에 따라서 최대 1000번째 숫자까지 만들면 되는데 가우스 덧셈 공식으로 1부터 46까지 반복하면 된다는 걸 도출할 수 있음

a, b = map(int, input().split())

ns = []
for i in range(1, a + b + 1):
    for j in range(i):
        ns.append(i)

# total = 0
# for i in range(a, b+1):
#     total += ns[i-1]
# print(total)

print(sum(ns[a - 1:b]))
