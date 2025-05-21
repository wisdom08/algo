# https://www.codewars.com/kata/55fab1ffda3e2e44f00000c6/train/python
# 회고: s // 0.036

import math


def cockroach_speed(speed_kmh):
    speed_cms = speed_kmh * (100000 / 3600)

    return math.floor(speed_cms)
