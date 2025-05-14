# https://www.codewars.com/kata/576bb71bbbcf0951d5000044
# 회고:  if not arr: return []

def count_positives_sum_negatives(arr):
    count_of_positive = 0
    sum_of_negative = 0
    if len(arr) == 0:
        return []

    for i in arr:
        if i == 0:
            continue
        if i > 0:
            count_of_positive += 1
        else:
            sum_of_negative += i

    return [count_of_positive, sum_of_negative]
