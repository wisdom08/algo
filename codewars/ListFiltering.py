# https://www.codewars.com/kata/53dbd5315a3c69eed20002dd/train/python
# 회고: isinstance, type

def filter_list(l):
    res = []
    for x in l:
        if type(x) == int:
            res.append(x)
    return res
