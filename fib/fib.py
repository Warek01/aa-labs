import numpy as np


def cheating(n: int) -> int:
	fib = [
		0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597,
		2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418,
		317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465,
		14930352, 24157817, 39088169, 63245986, 102334155, 165580141, 267914296,
		433494437, 701408733, 1134903170, 1836311903, 2971215073, 4807526976,
		7778742049, 12586269025, 20365011074, 32951280099, 53316291173,
		86267571272, 139583862445, 225851433717, 365435296162, 591286729879,
		956722026041, 1548008755920, 2504730781961, 4052739537881, 6557470319842,
		10610209857723, 17167680177565, 27777890035288, 44945570212853,
		72723460248141, 117669030460994, 190392490709135, 308061521170129,
		498454011879264, 806515533049393, 1304969544928657, 2111485077978050,
		3416454622906707, 5527939700884757, 8944394323791464, 14472334024676221,
		23416728348467685, 37889062373143906, 61305790721611591, 99194853094755497,
		160500643816367088, 259695496911122585, 420196140727489673,
		679891637638612258, 1100087778366101931, 1779979416004714189,
		2880067194370816120, 4660046610375530309, 7540113804746346429
	]

	return fib[n]


def recursive(n: int) -> int:
	if n == 0:
		return 0

	if n == 1 or n == 2:
		return 1

	return recursive(n - 1) + recursive(n - 2)


def iterative(n: int) -> int:
	a, b = 0, 1
	for _ in range(n - 1):
		b = a + b
		a = b - a

	return b


def matrix(n: int) -> int:
	f1 = np.array([[1, 1], [1, 0]])
	eigenvalues, eigenvectors = np.linalg.eig(f1)
	fn = eigenvectors @ np.diag(eigenvalues ** n) @ eigenvectors.T
	return int(np.rint(fn[0, 1]))


def exponentiation(n: int):
	def matrix_multiply(A, B):
		a, b, c, d = A
		x, y, z, w = B

		return (
			a * x + b * z,
			a * y + b * w,
			c * x + d * z,
			c * y + d * w,
		)

	def matrix_power(A, m):
		if m == 0:
			return [1, 0, 0, 1]
		elif m == 1:
			return A
		else:
			B = A
			n = 2
			while n <= m:
				# repeated square B until n = 2^q > m
				B = matrix_multiply(B, B)
				n = n * 2
			# add on the remainder
			R = matrix_power(A, m - n // 2)
			return matrix_multiply(B, R)

	F1 = [1, 1,
	      1, 0]

	return matrix_power(F1, n)[1]


def implicit_matrix(n: int) -> int:
	def multiply(a: int, b: int, x: int, y: int):
		return x * (a + b) + a * y, a * x + b * y

	def square(a: int, b: int):
		a2 = a * a
		b2 = b * b
		ab = a * b
		return a2 + (ab << 1), a2 + b2

	def power(a: int, b: int, m: int):
		if m == 0:
			return 0, 1
		elif m == 1:
			return a, b
		else:
			x, y = a, b
			n = 2
			while n <= m:
				# repeated square until n = 2^q > m
				x, y = square(x, y)
				n = n * 2
		# add on the remainder
		a, b = power(a, b, m - n // 2)
		return multiply(x, y, a, b)

	a, b = power(1, 0, n)
	return a


def gratio(n):
	if n < 6:
		return gratio.f[n]

	t = 5
	fn = 5

	while t < n:
		fn = round(fn * gratio.PHI)
		t += 1

	return fn


gratio.PHI = 1.6180339
gratio.f = [0, 1, 1, 2, 3, 5]
