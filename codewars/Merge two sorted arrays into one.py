# https://www.codewars.com/kata/5899642f6e1b25935d000161/train/python
# 회고: 합집합 set(arr1) | set(arr2)

def merge_arrays(arr1, arr2):
    return sorted(set(arr1+arr2))
