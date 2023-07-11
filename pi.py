from random import random

number_points = int(input('Number of points: '))

points_square = 0
points_circle = 0

for i in range(number_points):
    point_x = random()
    point_y = random()

    if point_x ** 2 + point_y ** 2 <= 1:
        points_circle += 1
    points_square += 1

pi = 4 * points_circle / points_square
print('Randomized pi:', pi)
