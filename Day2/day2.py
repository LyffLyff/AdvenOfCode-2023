# https://adventofcode.com/2023/day/2
import re

file = open("input.txt")
input = file.readlines()
file.close


class SingleGame:
    red = 0
    green = 0
    blue = 0

    def findBallsAmount(self, single_game) -> None:
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


sum_of_possible_ids = 0

for i in range(len(input)):
    game_class = SingleGame()
    SingleGame.findBallsAmount(game_class, input[i])
    if game_class.red <= 12 and game_class.blue <= 14 and game_class.green <= 13:
        # game id = index + 1
        sum_of_possible_ids += i + 1


print("Sum of possible ids: ", sum_of_possible_ids)
