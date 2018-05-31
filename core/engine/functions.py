import math as m
import copy
import random
import matplotlib.pyplot as plt
import core.engine.classes as c


def start(points_number, central_number):
    epoch = 0
    plane = init(points_number, central_number)
    find_centrals(plane.points, plane.old_centrals)
    draw_centrals(plane.old_centrals)

    while True:
        epoch = epoch + 1
        plane.new_centrals = copy.deepcopy(plane.old_centrals)
        update_centrals(plane.new_centrals)
        clean_points(plane.new_centrals)
        find_centrals(plane.points, plane.new_centrals)
        print('Epoch: ', epoch)
        draw_centrals(plane.new_centrals)
        if centrals_equals_position(plane.old_centrals, plane.new_centrals):
            break
        else:
            plane.old_centrals = copy.deepcopy(plane.new_centrals)


def update_centrals(centrals):
    for i in range(len(centrals)):
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
    plane = c.Plane

    plane.points = get_random_points(points_number)
    plane.old_centrals = get_random_centrals(central_number, points_number)

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
        random_centrals.append(c.Central(random.uniform(0, m.sqrt(max_coordinate)), random.uniform(0, m.sqrt(max_coordinate)), []))
    return random_centrals


def get_random_points(n):
    random_points = []
    for index in range(n):
        new_point = c.Point(random.uniform(0, m.sqrt(n)), random.uniform(0, m.sqrt(n)))
        random_points.append(new_point)
    return random_points


def draw_centrals(centrals):
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
    for i in range(len(centrals)):
        plt.plot(centrals[i].x, centrals[i].y, (colors[i] + '+'))
        for j in range(len(centrals[i].points)):
            plt.plot(centrals[i].points[j].x, centrals[i].points[j].y, (colors[i] + 'o'))
    plt.show()
    plt.clf()
