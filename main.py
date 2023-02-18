import matplotlib.pyplot as plt
from random import randint
from datetime import datetime

from sort import quicksort, mergesort, heapsort, selectionsort
from Algorithm import Algorithm

START = 1_000
END = 5_000
STEP = 1_000

ALGORITHMS: list[Algorithm] = [
	Algorithm('Quick Sort', quicksort, 'b'),
	Algorithm('Merge Sort', mergesort, 'r'),
	Algorithm('Heap Sort', heapsort, 'g'),
	Algorithm('Selection Sort', selectionsort, 'y'),
]

for i in range(START, END + STEP, STEP):
	arr = [randint(-1_000_000, 1_000_000) for _ in range(i)]
	for algorithm in ALGORITHMS:
		start = datetime.now()
		algorithm.function(arr)
		algorithm.data.append((datetime.now() - start).microseconds)

STEPS = [i for i in range(START, END + STEP, STEP)]

for algorithm in ALGORITHMS:
	plt.plot(STEPS, algorithm.data, algorithm.color)

plt.legend([algorithm.name for algorithm in ALGORITHMS])
plt.xlabel('Array size')
plt.ylabel('Sorting time (μs)')

plt.show()
