import itertools
import math
import matplotlib.pyplot as plt

def calculate_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def total_route_distance(route):
    distance = 0
    for i in range(len(route) - 1):
        distance += calculate_distance(route[i], route[i + 1])
    return distance

def find_shortest_route(points):
    warehouse = points[0]
    delivery_points = points[1:]
    all_routes = itertools.permutations(delivery_points)
    shortest_distance = float('inf')
    shortest_route = None
    for route in all_routes:
        full_route = [warehouse] + list(route) + [warehouse]
        distance = total_route_distance(full_route)
        if distance < shortest_distance:
            shortest_distance = distance
            shortest_route = full_route
    return shortest_route, shortest_distance

def plot_route(route):
    x_coords = [point[0] for point in route]
    y_coords = [point[1] for point in route]
    plt.figure(figsize=(8, 6))
    plt.plot(x_coords, y_coords, marker='o', linestyle='-', color='b')
    for i, point in enumerate(route):
        label = f"{i}" if i == 0 or i == len(route) - 1 else f"{route[i]}"
        plt.text(point[0] + 0.2, point[1] + 0.2, label, fontsize=9)
    plt.title("Optimal Delivery Route")
    plt.xlabel("X-coordinate")
    plt.ylabel("Y-coordinate")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    points = [(0, 0), (2, 3), (5, 4), (8, 1), (4, 7), (1, 8)]
    shortest_route, shortest_distance = find_shortest_route(points)
    print(f"Shortest Route: {shortest_route}")
    print(f"Shortest Distance: {shortest_distance:.2f}")
    plot_route(shortest_route)
