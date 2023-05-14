import matplotlib.pyplot as plt
from datetime import datetime

from algorithms import *
from Algorithm import *

START = 100
END = 200
STEP = 1

ALGORITHMS: list[Algorithm] = [
	Algorithm('Bailey Borwein Plouffe', Bailey_Borwein_Plouffe, 'b'),
	Algorithm('Leibniz', leibniz, 'r'),
	Algorithm('Chudnovsky', chudnovsky, 'g'),
]

for i in range(START, END + STEP, STEP):
	for algorithm in ALGORITHMS:
		start = datetime.now()
		algorithm.function(i)
		algorithm.data.append((datetime.now() - start).microseconds)

STEPS = [i for i in range(START, END + STEP, STEP)]

for algorithm in ALGORITHMS:
	plt.plot(STEPS, algorithm.data, algorithm.color)

plt.legend([algorithm.name for algorithm in ALGORITHMS])
plt.grid(True)
plt.title('N-th digit of PI')
plt.xlabel('Nr. of digits')
plt.ylabel('Computing time (μs)')
plt.show()
