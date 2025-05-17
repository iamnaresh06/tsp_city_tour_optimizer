from distance import haversine_distance
import random
import math

def calculate_total_distance(path, cities):
    return sum(
        haversine_distance(*cities[path[i]][1:], *cities[path[i + 1]][1:])
        for i in range(len(path) - 1)
    )

def greedy_algorithm(cities, start_index=0):
    n = len(cities)
    visited = [False] * n
    path = [start_index]
    visited[start_index] = True

    for _ in range(n - 1):
        last = path[-1]
        nearest = min(
            (i for i in range(n) if not visited[i]),
            key=lambda i: haversine_distance(*cities[last][1:], *cities[i][1:])
        )
        path.append(nearest)
        visited[nearest] = True

    return path

def two_opt(cities, path):
    def distance(p):
        return calculate_total_distance(p, cities)

    best = path
    improved = True
    while improved:
        improved = False
        for i in range(1, len(best) - 2):
            for j in range(i + 1, len(best)):
                if j - i == 1: continue
                new_path = best[:i] + best[i:j][::-1] + best[j:]
                if distance(new_path) < distance(best):
                    best = new_path
                    improved = True
        path = best
    return best

def simulated_annealing(cities, start_index=0):
    n = len(cities)
    current = list(range(n))
    random.shuffle(current)
    if start_index in current:
        current.remove(start_index)
    current = [start_index] + current

    best = current[:]
    best_distance = calculate_total_distance(best, cities)
    T = 10000.0
    T_min = 1.0
    alpha = 0.995

    while T > T_min:
        i, j = sorted(random.sample(range(1, n), 2))
        new = current[:]
        new[i:j] = reversed(new[i:j])
        new_distance = calculate_total_distance(new, cities)

        if new_distance < best_distance or math.exp((best_distance - new_distance) / T) > random.random():
            current = new
            if new_distance < best_distance:
                best = new
                best_distance = new_distance

        T *= alpha

    return best