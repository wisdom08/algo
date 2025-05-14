# https://www.codewars.com/kata/5a262cfb8f27f217f700000b
# 회고: s = set(a)&set(b)

def solve(a, b):
    return ''.join([ch for ch in a if ch not in b] + [ch for ch in b if ch not in a])
