# https://www.codewars.com/kata/53da6d8d112bd1a0dc00008b/train/python
# 회고: l[::-1]

def reverse_list(l):
    res = []
    for i in range(1, len(l)+1):
        res.append(l[-i])
    return res