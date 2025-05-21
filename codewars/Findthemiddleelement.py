# https://www.codewars.com/kata/545a4c5a61aa4c6916000755/train/python
# 회고: index, sorted

def gimme(input_array):
    man_and_min = [max(input_array), min(input_array)]
    index = 0
    for i in input_array:
        if i not in man_and_min:
            return index

        index += 1
