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
B = 30

for n in range(A, B + 1):
	for (name, f) in funcs:
		start = datetime.now()
		f(n)
		elapsed = datetime.now() - start
		data[name] += [elapsed.microseconds]

plt.plot(
	data['Cheating'], 'r',
	data['Recursive'], 'b',
	data['Iterative'], 'g',
	data['Golden ratio'], 'y',
	data['Eigenvalue'], 'k',
	data['Eigenvalue fast exponentiation'], 'm',
	data['Eigenvalue optimized'], 'c'
)
plt.xlabel('N')
plt.ylabel('μs')
plt.legend([name for (name, f) in funcs])
plt.show()
