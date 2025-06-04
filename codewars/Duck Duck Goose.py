# https://www.codewars.com/kata/582e0e592029ea10530009ce
# 회고: 원형 배열

class Player:
    def __init__(self, name):
        self.name = name


def duck_duck_goose(players, goose):
    chosen_index = (goose - 1) % len(players)
    return players[chosen_index].name
