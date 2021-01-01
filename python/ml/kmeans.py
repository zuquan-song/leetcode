from collections import defaultdict
from random import uniform
from math import sqrt

def point_avg(points):
    dimensions = len(points[0])
    new_center = []

    for dimension in range(dimensions):
        dim_sum = 0
        for p in points:
            dim_sum += p[dimension]
        new_center.append(dim_sum / float(len(points)))

    return new_center

def update_centers(data_set, assignments):
    new_means = defaultdict(list)
    centers = []
    for assignments, point in zip(assignments, data_set):
        new_means[assignments].append(point)

    for points in new_means.values():
        centers.append(point_avg(points))

    return centers

def distance(a, b):
    dimensions = len(a)
    _sum = 0
    for dimension in range(dimensions):
        difference_sq = (a[dimension] - b[dimension]) ** 2
        _sum += difference_sq
    return sqrt(_sum)

def assign_points(data_points, centers):
    assignments = []
    for point in data_points:
        shortest = float('inf')
        shortest_index = 0
        for i in range(len(centers)):
            val = distance(point, centers[i])
            if val < shortest:
                shortest = val
                shortest_index = i
        assignments.append(shortest_index)
    return assignments

def generate_k(data_set, k):
    centers = []
    dimensions = len(data_set[0])
    min_max = defaultdict(int)

    for i in range(dimensions):
        min_val, max_val = float('inf'), float('-inf')
        for point in data_set:
            min_val = min(min_val, point[i])
            max_val = max(max_val, point[i])
        min_max[i] = (min_val, max_val)

    for _k in range(k):
        rand_point = []
        for i in range(dimensions):
            min_val, max_val = min_max[i]
            rand_point.append(uniform(min_val, max_val))
        centers.append(rand_point)
    return centers

def k_means(dataset, k):
    k_points = generate_k(dataset, k)
    assignments = assign_points(dataset, k_points)
    old_assignments = None
    while assignments != old_assignments:
        new_centers = update_centers(dataset, assignments)
        old_assignments = assignments
        assignments = assign_points(dataset, new_centers)
    return zip(assignments, dataset)


points = [
    [1, 2],
    [2, 1],
    [3, 1],
    [5, 4],
    [5, 5],
    [6, 5],
    [10, 8],
    [7, 9],
    [11, 5],
    [14, 9],
    [14, 14],
    ]
for assign, data in k_means(points, 3):
    print(assign, data)