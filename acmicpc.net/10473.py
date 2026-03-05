from heapq import heapify, heappush, heappop

def distance_walk(x1: float, y1: float, x2: float, y2: float) -> float:
	return (abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2 ) ** .5 / 5


def distance_cannon(x1: float, y1: float, x2: float, y2: float) -> float:
	distance = (abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2 ) ** .5 
	if distance <= 50: 
		return distance / 25
	else:
		return (distance - 50) / 5 + 2

coords = {}
coords[-1] = tuple(map(float, input().split()))
coords[101] = tuple(map(float, input().split()))
n = int(input())

for i in range(n):
	coords[i] = tuple(map(float, input().split()))
distances = {point: {} for point in coords}

for point in coords:
	distances[point] = distance_walk(*coords[-1], *coords[point])

print(distances)

q = [(v, k) for k, v in distances.items()]
heapify(q)
print(q)
visited = {-1}
distances.pop(-1)

while q:
	curr_distance, point = heappop(q)
	for destination in distances:
		if point not in visited: 
			visited.add(destination)
			new_distance = distance_cannon(*coords[point], *coords[destination]) + curr_distance 
			print(f"calculated new distance: {new_distance} for from: {point} and to {destination}")
			if new_distance < distances[destination]:
				distances[destination] = new_distance
			heappush(q, (distances[destination], destination))
print(distances)
			
