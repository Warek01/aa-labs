from datetime import datetime
from Graph import Graph

TESTS = 10
SIZE = 100
EDGES = 3000
PATH_NODES = 3
d_total_time = 0
fw_total_time = 0

g = Graph(SIZE)

for _ in range(TESTS):
	g = Graph(SIZE)
	g.populate(EDGES)

	start = datetime.now()
	for i in range(PATH_NODES):
		g.dijkstra(0, i)

	end = datetime.now()

	d_total_time += (end - start).microseconds

	start = datetime.now()
	for i in range(PATH_NODES):
		g.floyd_warshall(0, i)

	end = datetime.now()

	fw_total_time += (end - start).microseconds

print(
	f'''Average time for a graph with {SIZE} nodes and {EDGES} edges \
({'Complete' if g.is_complete() else 'Sparse' if g.is_sparse() else 'Dense'} with {g.get_density():.2f} density)
Dijkstra: {d_total_time / TESTS:.2f}μs
Floyd-Warshall: {fw_total_time / TESTS:.2f}μs
Ratio: {d_total_time / fw_total_time:.4f} (D/FW) or {fw_total_time / d_total_time:.4f} (FW/D)
In {TESTS} tests with shortest path between {PATH_NODES} random node pairs.'''
)
