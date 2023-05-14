import random
import sys
import networkx as nx
import matplotlib.pyplot as plt

INF = sys.maxsize
MIN = 1
MAX = 100


class Graph:
	_g: list[list[int]] = []
	size: int = 0
	edges_count: int = 0

	def __init__(self, size: int):
		self.size = size

		for i in range(size):
			ls = []
			for j in range(size):
				ls += [INF]
			self._g += [ls]

	def add(self, v1: int, v2: int, value: int):
		if v1 == v2:
			return

		self._g[v1][v2] = value
		self._g[v2][v1] = value

	def get(self, v1: int, v2: int):
		return self._g[v1][v2]

	def is_connected(self, v1: int, v2: int):
		return self.get(v1, v2) != INF

	def populate_complete(self, min: int = MIN, max: int = MAX):
		self.edges_count = self.get_max_edges()

		for i in range(self.size - 1):
			for j in range(self.size - 1):
				self.add(i, j, random.randint(min, max))

	def populate(self, connections_count: int, min: int = MIN, max: int = MAX):
		self.edges_count = connections_count

		if connections_count > self.get_max_edges():
			raise Exception(f"Too many connections\nGot {connections_count}\nMax: {self.get_max_edges()}\nSize: {self.size}")

		for i in range(connections_count):
			v1 = random.randint(0, self.size - 1)
			v2 = random.randint(0, self.size - 1)

			while v1 == v2:
				v1 = random.randint(0, self.size - 1)
				v2 = random.randint(0, self.size - 1)

			self.add(v1, v2, random.randint(min, max))

	def print(self):
		for i in range(self.size):
			string = ''

			for j in range(self.size):
				string += self.get(i, j).__str__() + ' '

			print(string)

	def show(self):
		plt.figure(figsize=(8, 6))
		G = nx.Graph()

		for i in range(self.size):
			for j in range(self.size):
				if i != j and self.is_connected(i, j):
					G.add_edge(i, j)

		nx.draw(
			G, node_size=1000,
			labels={node: node for node in G.nodes()}
		)

		plt.savefig('Graph.png')
		plt.show()

	def get_max_edges(self) -> int:
		return int((self.size * (self.size - 1)) / 2)

	def dijkstra(self, v1: int, v2: int) -> list[int]:
		dist = [INF] * self.size
		visited = [False] * self.size
		dist[v1] = 0

		for i in range(self.size):
			u = self._min_distance(dist, visited)
			visited[u] = True

			for v in range(self.size):
				if not visited[v] and self._g[u][v] != INF and \
					dist[u] + self._g[u][v] < dist[v]:
					dist[v] = dist[u] + self._g[u][v]

		path = [v2]
		while path[-1] != v1:
			for v in range(self.size):
				if self._g[path[-1]][v] != INF and \
					dist[v] + self._g[path[-1]][v] == dist[path[-1]]:
					path.append(v)
					break

		return path[::-1]

	def _min_distance(self, dist: list[int], visited: list[bool]) -> int:
		min_dist = INF
		min_vertex = -1

		for v in range(self.size):
			if not visited[v] and dist[v] <= min_dist:
				min_dist = dist[v]
				min_vertex = v

		return min_vertex

	def floyd_warshall(self, v1: int, v2: int) -> list[int]:
		dist = [[INF if self._g[i][j] == INF else self._g[i][j] for j in range(self.size)] for i in range(self.size)]
		next = [[j if self._g[i][j] != INF else None for j in range(self.size)] for i in range(self.size)]

		for k in range(self.size):
			for i in range(self.size):
				for j in range(self.size):
					if dist[i][k] == INF or dist[k][j] == INF:
						continue

					new_dist = dist[i][k] + dist[k][j]
					if new_dist < dist[i][j]:
						dist[i][j] = new_dist
						next[i][j] = next[i][k]

		if next[v1][v2] is None:
			return []

		path = [v1]
		while path[-1] != v2:
			path.append(next[path[-1]][v2])

		return path

	def get_density(self) -> float:
		return self.edges_count / self.get_max_edges()

	def is_sparse(self):
		return self.get_density() < 0.5

	def is_dense(self):
		return self.get_density() >= 0.5

	def is_complete(self):
		return self.get_density() == 1
