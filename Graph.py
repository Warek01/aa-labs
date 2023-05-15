import heapq
from collections import *
from profiler import *


class Graph:
	def __init__(self, vertices: int):
		self.vertices = vertices
		self.adj_list = {vertex: [] for vertex in range(self.vertices)}

	def add_edge(self, u, v, weight):
		self.adj_list[u].append((v, weight))
		self.adj_list[v].append((u, weight))


def find(parent, i):
	if parent[i] == i:
		return i
	return find(parent, parent[i])


@exec_time("kruskal")
def kruskal(graph, start):
	result = []  # This will store the resultant MST
	edges = []

	# Create a list of all edges in the graph
	for node in graph.adj_list:
		for neighbor, weight in graph.adj_list[node]:
			edges.append((weight, node, neighbor))

	# Sort all the edges in non-decreasing order of their weight
	edges.sort()

	parent = [i for i in range(graph.vertices)]

	for edge in edges:
		weight, u, v = edge
		parent_u = find(parent, u)
		parent_v = find(parent, v)
		if parent_u != parent_v:
			result.append((u, v, weight))
			parent[parent_u] = parent_v

	return result


@exec_time("prim")
def prim(graph, start_vertex):
	mst = defaultdict(set)
	visited = {start_vertex}
	edges = [
		(cost, start_vertex, to)
		for to, cost in graph.adj_list[start_vertex]
	]
	heapq.heapify(edges)

	while edges:
		cost, frm, to = heapq.heappop(edges)
		if to not in visited:
			visited.add(to)
			mst[frm].add(to)
			for to_next, cost2 in graph.adj_list[to]:
				if to_next not in visited:
					heapq.heappush(edges, (cost2, to, to_next))

	return mst
