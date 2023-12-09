# https://adventofcode.com/2023/day/2
import re

file = open("input.txt")
input = file.readlines()
file.close


class SingleGame:
    red = 0
    green = 0
    blue = 0

    def __init__(self, single_game):
        # finding most red balls found
        red_balls = re.findall(r"(\d+) red", single_game)
        red_balls = [int(x) for x in red_balls]  # convert to integer list
        red_balls.sort(reverse=True)  # sort so biggest number at index = 0
        if len(red_balls) > 0:
            # if the current amount of red balls is smaller than already found
            if self.red < red_balls[0]:
                self.red = red_balls[0]

        # finding most green balls found
        red_balls = re.findall(r"(\d+) green", single_game)
        red_balls = [int(x) for x in red_balls]  # convert to integer list
        red_balls.sort(reverse=True)  # sort so biggest number at index = 0
        if len(red_balls) > 0:
            # if the current amount of red balls is smaller than already found
            if self.green < red_balls[0]:
                self.green = red_balls[0]

        # finding most blue balls found
        red_balls = re.findall(r"(\d+) blue", single_game)
        red_balls = [int(x) for x in red_balls]  # convert to integer list
        red_balls.sort(reverse=True)  # sort so biggest number at index = 0
        if len(red_balls) > 0:
            # if the current amount of red balls is smaller than already found
            if self.blue < red_balls[0]:
                self.blue = red_balls[0]

    def getPowerOfBalls(self) -> None:
        # returns the minimum amount of balls needed multiplied together
        # -> findBallsAmount must
        return self.blue * self.red * self.green


sum_of_powers = 0

for i in range(len(input)):
    game_class = SingleGame(input[i])
    sum_of_powers += SingleGame.getPowerOfBalls(game_class)


print("Sum of possible ids: ", sum_of_powers)
