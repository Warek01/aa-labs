from profiler import *
from Graph import *
import random


def generate_random_graph(N, p=0.5, min_weight=1, max_weight=15):
	graph = Graph(N)
	for i in range(N):
		for j in range(i + 1, N):  # avoid self-loop and duplicate edges
			if random.random() < p:  # if random number is less than p, create edge
				weight = random.randint(min_weight, max_weight)
				graph.add_edge(i, j, weight)
	return graph


inp = []

for n in range(10, 300, 10):
	print("---")
	print(n)
	graph = generate_random_graph(n)
	kruskal(graph, 0)
	prim(graph, 0)
	inp.append(n)

plot_result(inp)
