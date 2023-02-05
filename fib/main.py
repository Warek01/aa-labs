from datetime import datetime
import matplotlib.pyplot as plt
import fib

funcs = [
	('Cheating', fib.cheating),
	('Recursive', fib.recursive),
	('Iterative', fib.iterative),
	('Golden ratio', fib.gratio),
	('Eigenvalue', fib.matrix),
	('Eigenvalue fast exponentiation', fib.exponentiation),
	('Eigenvalue optimized', fib.implicit_matrix)
]

data = {
	'Cheating': [],
	'Recursive': [],
	'Iterative': [],
	'Golden ratio': [],
	'Eigenvalue': [],
	'Eigenvalue fast exponentiation': [],
	'Eigenvalue optimized': []
}

A = 0
B = 20

for n in range(A, B + 1):
	for (name, f) in funcs:
		start = datetime.now()
		f(n)
		elapsed = datetime.now() - start
		data[name] += [elapsed.microseconds]

plt.plot(
	[i for i in range(A, B + 1)], data['Cheating'], 'r',
	[i for i in range(A, B + 1)], data['Recursive'], 'b',
	[i for i in range(A, B + 1)], data['Iterative'], 'g',
	[i for i in range(A, B + 1)], data['Golden ratio'], 'y',
	[i for i in range(A, B + 1)], data['Eigenvalue'], 'k',
	[i for i in range(A, B + 1)], data['Eigenvalue fast exponentiation'], 'm',
	[i for i in range(A, B + 1)], data['Eigenvalue optimized'], 'c'
)
plt.xlabel('N')
plt.ylabel('μs')
plt.legend([name for (name, f) in funcs])
plt.show()
