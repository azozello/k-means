import math as m
import copy
import random
import matplotlib.pyplot as plt
import core.engine.classes as c


def start(points_number, central_number, constant=0):
    epoch = 0
    plane = init(points_number, central_number)

    if constant < central_number:
        for i in range(constant):
            plane.old[i].move = False

    find_centrals(plane.points, plane.old)
    draw_centrals(plane.old)

    while True:
        epoch = epoch + 1
        plane.new = copy.deepcopy(plane.old)
        update_centrals(plane.new)
        clean_points(plane.new)
        find_centrals(plane.points, plane.new)
        print('Epoch: ', epoch)
        draw_centrals(plane.new)
        if centrals_equals_position(plane.old, plane.new):
            break
        else:
            plane.old = copy.deepcopy(plane.new)


def update_centrals(centrals):
    for i in range(len(centrals)):
        if centrals[i].move:
            move_central(centrals[i])


def move_central(central):
    sum_x = 0.0
    sum_y = 0.0
    for i in range(len(central.points)):
        sum_x = sum_x + central.points[i].x
        sum_y = sum_y + central.points[i].y
    central.x = sum_x / len(central.points)
    central.y = sum_y / len(central.points)


def find_centrals(points, centrals):
    for i in range(len(points)):
        centrals[get_nearest_central(points[i], centrals)].points.append(points[i])


def get_nearest_central(point, centrals):
    nearest_central = 0
    for i in range(len(centrals)):
        if get_distance(point, centrals[i]) < get_distance(point, centrals[nearest_central]):
            nearest_central = i
    return nearest_central


def clean_points(centrals):
    for i in range(len(centrals)):
        centrals[i].points = []


def init(points_number, central_number):
    plane = c.Plane([], [], [])

    plane.points = get_random_points(points_number)
    plane.old = get_random_centrals(central_number, points_number)

    return plane


def get_distance(point_1, point_2):
    return m.sqrt(m.pow(point_2.x - point_1.x, 2)
                  + m.pow(point_2.y - point_1.y, 2))


def centrals_equals_position(centrals_1, centrals_2):
    if len(centrals_1) != len(centrals_2):
        return False
    else:
        for i in range(len(centrals_1)):
            if (centrals_1[i].x != centrals_2[i].x) or (centrals_1[i].y != centrals_2[i].y):
                return False
    return True


def get_random_centrals(n, max_coordinate):
    random_centrals = []
    for i in range(n):
        random_centrals.append(c.Centroid([], random.uniform(0, m.sqrt(max_coordinate)), random.uniform(0, m.sqrt(max_coordinate))))
    return random_centrals


def get_random_points(n):
    return [c.Point(random.uniform(0, m.sqrt(n)), random.uniform(0, m.sqrt(n))) for i in range(n)]


def draw_centrals(centrals):
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
    for i in range(len(centrals)):
        if centrals[i].move:
            plt.plot(centrals[i].x, centrals[i].y, (colors[i] + '+'))
        else:
            plt.plot(centrals[i].x, centrals[i].y, 'k+')

        for j in range(len(centrals[i].points)):
            if centrals[i].move:
                plt.plot(centrals[i].points[j].x, centrals[i].points[j].y, (colors[i] + 'o'))
            else:
                plt.plot(centrals[i].points[j].x, centrals[i].points[j].y, 'ko')

    plt.show()
    plt.clf()
