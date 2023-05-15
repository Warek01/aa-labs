import numpy as np
import matplotlib.pyplot as plt
import timeit

OKGREEN = '\033[92m'
WARNING = '\033[93m'
BOLD = '\033[1m'
ENDC = '\033[0m'

running_time = dict()


def exec_time(name, print_data=False):
	def real_decorator(func):
		def wrapper(graph, start_vertex):
			t_start = timeit.default_timer()
			result = func(graph, start_vertex)
			t_end = timeit.default_timer()

			elapsed_time = round((t_end - t_start) * 10 ** 6, 4)

			result = f'and result {BOLD}{result}{ENDC}' if print_data else ''
			input_str = f'with input {WARNING}{graph}{ENDC}' if print_data else ''

			print(
				f'Elapsed time {input_str} {result}: {OKGREEN}{elapsed_time}{ENDC} µs.')

			# save results for graphing
			if name in running_time.keys():
				running_time[name].append(elapsed_time)
			else:
				running_time[name] = list()
				running_time[name].append(elapsed_time)

			return result

		return wrapper

	return real_decorator


def plot_result(_input: list):
	names = np.array(list(running_time.keys()))
	times = np.array(list(running_time.values()))
	algorithm_num = 0

	plt.title('Running times per algorithm')
	plt.xlabel('Values')
	plt.ylabel('Time (µs)')

	for _ in times:
		x_axis = np.array(_input)
		y_axis = times[algorithm_num]

		plt.plot(x_axis, y_axis, label=names[algorithm_num])

		algorithm_num += 1

	plt.legend()
	plt.grid()
	plt.show()
