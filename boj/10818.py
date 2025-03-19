# https://www.acmicpc.net/problem/10818
# 회고: min(), max() 함수를 각각 호출하는 게 직관적이긴 하지만 한 번의 반복문으로도 찾을 수 있음.
# 입력 크기가 커지면 성능을 고려해야 하긴 하는데 min(), max() 함수는 내부적으로 최적화가 되어 있어서 일반적으로 해당 함수를 쓰는 게 직관적이고 충분히 빠르다고 한다.

n = int(input())
ns = list(map(int, input().split()))

# print(min(ns), max(ns))

min_value, max_value = ns[0], ns[0]

for n in ns:
    if n < min_value:
        min_value = n
    if n > max_value:
        max_value = n

print(min_value, max_value)