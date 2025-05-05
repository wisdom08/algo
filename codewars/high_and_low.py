# https://www.codewars.com/kata/554b4ac871d6813a03000035/train/python
# 회고: map(int, str.split())

def high_and_low(numbers):
    numbers = numbers.split(' ')
    min = int(numbers[0])
    max = int(numbers[0])
    
    for n in numbers:
        n = int(n)
        if min > n:
            min = n
        elif max < n:
            max = n
    
    return f'{max} {min}'

def high_and_low2(numbers):
    ns = list(map(int, numbers.split(" ")))
    return f"{max(ns)} {min(ns)}"
    