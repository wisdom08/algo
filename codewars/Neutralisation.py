def neutralise(s1, s2):
    result = ""

    for char1, char2 in zip(s1, s2):
        if char1 == '+' and char2 == '+':
            result += '+'
        elif char1 == '-' and char2 == '-':
            result += '-'
        else:
            result += '0'

    return result
