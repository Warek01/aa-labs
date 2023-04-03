from Graph import Graph
import matplotlib.pyplot as plt
from datetime import datetime


def print_g(bfs=False):
	print('Insert graph size')
	CONN_COUNT = int(input('Connections count = '))
	NODES_COUNT = int(input('Nodes count = '))
	WAIT_TIME = float(input('Wait time = '))

	g = Graph()
	g.populate(CONN_COUNT, NODES_COUNT)

	if bfs:
		g.bfs(0, True, WAIT_TIME)
	else:
		g.dfs(0, True, WAIT_TIME)


print('Choose operation:')
print('1 - Draw DFS')
print('2 - Draw BFS')
print('3 - Compare DFS VS BFS')

OP = int(input())

if OP == 1:
	print_g(False)
elif OP == 2:
	print_g(True)
else:
	MIN_NODES = int(input('Start nodes count = '))
	MAX_NODES = int(input('End nodes count = '))
	STEP = int(input('Step size = '))

	x_dataset: list[int] = []
	y_dataset_dfs: list[int] = []
	y_dataset_bfs: list[int] = []

	for max_nodes in range(MIN_NODES, MAX_NODES + STEP, STEP):
		x_dataset += [max_nodes]
		g = Graph()
		g.populate(max_nodes * 10, max_nodes)

		start = datetime.now()
		g.dfs(0, False)
		end = datetime.now()
		y_dataset_dfs += [(end - start).microseconds]

		start = datetime.now()
		g.bfs(0, False)
		end = datetime.now()
		y_dataset_bfs += [(end - start).microseconds]

	plt.figure()
	plt.title('DFS VS BFS', fontsize=24)
	plt.xlabel('Nr. of nodes', fontsize=16)
	plt.ylabel('Running time (μs)', fontsize=16)
	plt.grid(True)
	plt.plot(x_dataset, y_dataset_dfs)
	plt.plot(x_dataset, y_dataset_bfs)
	plt.legend(['DFS', 'BFS'])

	fig = plt.gcf()
	fig.savefig('running_times.png')
	plt.show()
