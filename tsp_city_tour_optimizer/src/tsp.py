import argparse
import csv
import json
import os
import matplotlib.pyplot as plt
from tsp_solver import greedy_algorithm, two_opt, simulated_annealing, calculate_total_distance

def load_cities(csv_path, selected_cities=None):
    with open(csv_path, newline='') as f:
        reader = csv.reader(f)
        next(reader)
        cities = [(row[0], float(row[1]), float(row[2])) for row in reader]
        if selected_cities:
            cities = [city for city in cities if city[0] in selected_cities]
        return cities

def export_geojson(path_indices, cities, filename):
    features = [{
        "type": "Feature",
        "geometry": {
            "type": "LineString",
            "coordinates": [[cities[i][2], cities[i][1]] for i in path_indices]
        },
        "properties": {
            "name": "Optimized Route"
        }
    }]
    geojson = {
        "type": "FeatureCollection",
        "features": features
    }
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w') as f:
        json.dump(geojson, f)
    print(f"Route written to {filename}")

def plot_route(tour):
    lons = [city[2] for city in tour]
    lats = [city[1] for city in tour]
    names = [city[0] for city in tour]

    plt.figure(figsize=(12, 7))
    plt.plot(lons, lats, 'bo-')

    for i, (lon, lat) in enumerate(zip(lons, lats)):
        plt.text(lon, lat, f"{i+1}) {names[i]}", fontsize=8, ha='right')

    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.title('City Tour Route')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('output/route_plot.png')  # Optional: save image
    plt.show()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--csv', required=True, help='Path to CSV file containing places')
    parser.add_argument('--start', required=True, help='Starting city')
    parser.add_argument('--cities', nargs='*', help='List of cities to include in the tour')
    parser.add_argument('--algo', choices=['greedy', 'two-opt', 'simulated-annealing'], default='greedy')
    parser.add_argument('--should-return', action='store_true', help='Return to start city at the end')
    args = parser.parse_args()

    cities = load_cities(args.csv, args.cities)

    city_indices = {name: idx for idx, (name, _, _) in enumerate(cities)}
    if args.start not in city_indices:
        raise ValueError(f"Start city '{args.start}' not found in the selected cities")

    start_index = city_indices[args.start]

    if args.algo == 'greedy':
        tour_indices = greedy_algorithm(cities, start_index)
    elif args.algo == 'two-opt':
        tour_indices = two_opt(cities, start_index)
    elif args.algo == 'simulated-annealing':
        tour_indices = simulated_annealing(cities, start_index)

    tour = [cities[i] for i in tour_indices]
    if args.should_return:
        tour.append(cities[start_index])
        tour_indices.append(start_index)

    for i, city in enumerate(tour):
        print(f"{i+1}) {city[0]}")

    print(f"Total distance: {calculate_total_distance(tour_indices, cities):.2f} km")

    export_geojson(tour_indices, cities, 'output/route.geojson')
    plot_route(tour)

if __name__ == '__main__':
    main()
