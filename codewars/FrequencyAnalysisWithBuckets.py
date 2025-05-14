# https://www.codewars.com/kata/5ac95cb05624bac42e000005
# 회고: bucket

from collections import Counter

def frequency_buckets(arr):
    if not arr:
        return []

    freq = Counter(arr)  # 
    max_freq = max(freq.values())  

    buckets = [None] * (max_freq + 1)

    for num, count in freq.items():
        if buckets[count] is None:
            buckets[count] = [num]
        else:
            buckets[count].append(num)

    return buckets
