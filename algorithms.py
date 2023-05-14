from decimal import getcontext, Decimal
from math import *


def Bailey_Borwein_Plouffe(n: Decimal | int) -> Decimal:
	getcontext().prec = n
	return sum(1 / Decimal(16) ** k *
	           (Decimal(4) / (8 * k + 1) -
	            Decimal(2) / (8 * k + 4) -
	            Decimal(1) / (8 * k + 5) -
	            Decimal(1) / (8 * k + 6)) for k in range(n))


def leibniz(n):
	sum = 0
	for k in range(n):
		numerator = (-1) ** k
		denominator = 2 * k + 1
		term = numerator / denominator
		sum += term
	pi = 4 * sum
	return str(pi)[0:n + 1]


pi = Decimal(
	'3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679')


def chudnovsky(n, root_precision = 10):
	def den(k):
		a = Decimal(factorial(6 * k) * (545140134 * k + 13591409))
		b = Decimal(factorial(3 * k) * (factorial(k) ** 3) * ((-262537412640768000) ** k))
		res = a / b
		if k > 0:
			return res + den(k - 1)
		else:
			return res

	def num(root_precision):
		p = getcontext().prec
		getcontext().prec = root_precision
		d = Decimal(10005).sqrt()
		getcontext().prec = p
		return 426880 * Decimal(10005).sqrt()

	return num(root_precision) / den(n)
