import numpy as np
import heapq

class TSP:
    def __init__(self, num_cities, distances):
        self.num_cities = num_cities
        self.distances = distances

    def greedy_best_first_search(self):
        visited = [0]  
        total_distance = 0

        while len(visited) < self.num_cities:
            current_city = visited[-1]
            min_distance = float('inf')
            next_city = None

            for city in range(self.num_cities):
                if city not in visited:
                    if self.distances[current_city][city] < min_distance:
                        min_distance = self.distances[current_city][city]
                        next_city = city

            visited.append(next_city)
            total_distance += min_distance

        total_distance += self.distances[visited[-1]][visited[0]]
        visited.append(visited[0])

        return visited, total_distance

    def a_star(self):
        start_node = (0, [0], 0)  
        pq = [start_node]  
        heapq.heapify(pq)

        while pq:
            total_distance, visited, current_city = heapq.heappop(pq)

            if len(visited) == self.num_cities:
                total_distance += self.distances[visited[-1]][visited[0]]
                visited.append(visited[0])
                return visited, total_distance

            for next_city in range(self.num_cities):
                if next_city not in visited:
                    next_visited = visited + [next_city]
                    next_distance = total_distance + self.distances[current_city][next_city] + self.distances[next_city][0]
                    heapq.heappush(pq, (next_distance, next_visited, next_city))

num_cities = 4
distances = np.array([
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
])

tsp = TSP(num_cities, distances)

# Greedy Best-First Search
route_greedy, distance_greedy = tsp.greedy_best_first_search()
print("Greedy Best-First Search:")
print("Route:", route_greedy)
print("Total Distance:", distance_greedy)

# A* Algorithm
route_a_star, distance_a_star = tsp.a_star()
print("\nA* Algorithm:")
print("Route:", route_a_star)
print("Total Distance:", distance_a_star)
