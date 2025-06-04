# https://www.codewars.com/kata/557e8a141ca1f4caa70000a6
# 회고: 삼각수

import math


def is_triangle_number(number: int) -> bool:
    if number < 0:
        return False

    discriminant = 1 + 8 * number

    sqrt_discriminant = int(math.isqrt(discriminant))

    if sqrt_discriminant * sqrt_discriminant == discriminant:
        k = (-1 + sqrt_discriminant) / 2
        return k.is_integer() and k >= 0

    return False
