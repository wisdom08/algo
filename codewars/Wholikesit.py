# https://www.codewars.com/kata/5266876b8f4bf2da9b000362/python
# 회고:  f-string 문자열 포맷팅
def likes(names):
    l = len(names)

    if l == 0:
        return 'no one likes this'
    elif l == 1:
        return names[0] + ' likes this'
    elif l == 2:
        return names[0] + ' and ' + names[1] + ' like this'
    elif l == 3:
        return names[0] + ', ' + names[1] + ' and ' + names[2] + ' like this'
    else:
        return names[0] + ', ' + names[1] + ' and ' + str(l-2) + ' others like this'
