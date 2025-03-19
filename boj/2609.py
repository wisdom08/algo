# https://www.acmicpc.net/problem/2609
# 회고: 유클리드 호제법 찾아 보기
import math

a, b = map(int, input().split())

gcd = math.gcd(a, b)
lcm = (a * b) // gcd

print(gcd, lcm)