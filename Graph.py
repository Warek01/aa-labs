from collections import defaultdict, deque
from random import randint
import networkx as nx
import matplotlib.pyplot as plt


class Graph:
	_graph: defaultdict[int, list[int]]

	def __init__(self):
		self._graph = defaultdict(list[int])

	def add(self, v1: int, v2: int):
		self._graph[v1].append(v2)

	def populate(self, connections: int, max_nodes: int):
		for _ in range(connections):
			v1 = randint(0, max_nodes)
			v2 = randint(0, max_nodes)

			while self._graph[v1].count(v2) > 0 or v1 == v2:
				v2 = randint(0, max_nodes)

			self._graph[v1].append(v2)

	def print(self):
		plt.figure(figsize=(19.2, 10.8))
		G = nx.Graph()

		for node, connections in self._graph.items():
			for conn in connections:
				G.add_edge(node, conn)

		nx.draw(
			G, node_size=1000,
			labels={node: node for node in G.nodes()}
		)

		plt.savefig('Graph.png')
		plt.show()

	def dfs(self, start_node: int, draw: bool, pause_interval: float = 0.5):
		visited = set()
		stack = [start_node]
		G = nx.Graph()

		while stack:
			node = stack.pop()
			if node not in visited:
				visited.add(node)

				for neighbor in reversed(self._graph[node]):
					if neighbor not in visited:
						stack.append(neighbor)

						if draw:
							G.add_edge(node, neighbor)
							nx.draw(G, with_labels=True)

							plt.draw()
							plt.pause(pause_interval)
							plt.clf()

		return visited

	def bfs(self, start_node: int, draw: bool, pause_interval: float = 0.5):
		visited = set()
		queue = deque([start_node])
		G = nx.Graph()

		while queue:
			node = queue.popleft()
			if node not in visited:
				visited.add(node)

				for neighbor in self._graph[node]:
					if neighbor not in visited:
						queue.append(neighbor)

						if draw:
							G.add_edge(node, neighbor)

							nx.draw(G, node_color='r', with_labels=True)

							plt.draw()
							plt.pause(pause_interval)
							plt.clf()

		return visited
