# https://www.codewars.com/kata/514b92a657cdc65150000006/train/python
# 회고: 주어진 숫자보다 작다는 거 놓침. 조건을 잘 확인하자

def solution(number):
    if number < 0:
        return 0

    res = set()

    for i in range(3, number):
        if i % 3 == 0 or i % 5 == 0:
            res.add(i)

    return sum(res)

# def solution(number):
#     return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)
