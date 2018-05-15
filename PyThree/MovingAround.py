

from enum import Enum
import random
import operator


class Directions(Enum):
    NORTH = (1, 0)
    SOUTH = (-1, 0)
    WEST = (0, -1)
    EAST = (0, 1)


def do_walk(starting_point, new_direction):

    return tuple(map(operator.add, starting_point, new_direction.value))


def random_walk(position, number_of_steps):

    print("WALK ----------------------------------------------- ")
    for counter in range(number_of_steps):
        rand_direction = random.choice([Directions.NORTH, Directions.SOUTH, Directions.EAST, Directions.WEST])
        print(rand_direction)
        position = do_walk(position, rand_direction)

    print("END WALK ----------------------------------------------- {}".format(position))
    return position


def calculate_distance(end_point):
    return abs(end_point[0]) + abs(end_point[1])


def calculate_distance_between(start_point, end_point):

    ip = calculate_distance(start_point)
    ep = calculate_distance(end_point)

    #this is not correct - FIXME
    return abs(abs(ep) - abs(ip))


starting_point = (0, 0)
walk = random_walk(starting_point, 5)
second_walk = random_walk(walk, 5)

print(calculate_distance(walk))
print(calculate_distance_between(starting_point, walk))
print(calculate_distance_between(walk, second_walk))
