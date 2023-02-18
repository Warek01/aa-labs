from math import floor
from copy import deepcopy


def quicksort(arr: list[int]) -> list[int]:
	sorted = deepcopy(arr)

	def partition(arr: list, left: int, right: int, pivot: int) -> int:
		while left <= right:
			while arr[left] < pivot:
				left += 1

			while arr[right] > pivot:
				right -= 1

			if left <= right:
				temp = arr[left]
				arr[left] = arr[right]
				arr[right] = temp
				left += 1
				right -= 1
		return left

	def sort(arr: list, left: int, right: int) -> None:
		if left >= right:
			return
		pivot = arr[floor((left + right) / 2)]
		index = partition(arr, left, right, pivot)
		sort(arr, left, index - 1)
		sort(arr, index, right)

	sort(sorted, 0, len(sorted) - 1)
	return sorted


def mergesort(arr: list[int]) -> list[int]:
	sorted = deepcopy(arr)

	def sort(arr: list) -> None:
		if len(arr) <= 1:
			return

		middle = len(arr) // 2

		L = arr[middle:]
		R = arr[:middle]

		sort(L)
		sort(R)

		i = j = k = 0

		while i < len(L) and j < len(R):
			if L[i] <= R[j]:
				arr[k] = L[i]
				i += 1
			else:
				arr[k] = R[j]
				j += 1
			k += 1

		while i < len(L):
			arr[k] = L[i]
			i += 1
			k += 1

		while j < len(R):
			arr[k] = R[j]
			j += 1
			k += 1

	sort(sorted)
	return sorted


def heapsort(arr: list[int]) -> list[int]:
	sorted = deepcopy(arr)

	def heapify(arr: list[int], n: int, i: int):
		largest = i
		l = 2 * i + 1
		r = 2 * i + 2

		if l < n and arr[i] < arr[l]:
			largest = l

		if r < n and arr[largest] < arr[r]:
			largest = r

		if largest != i:
			(arr[i], arr[largest]) = (arr[largest], arr[i])

			heapify(arr, n, largest)

	def sort(arr: list[int]):
		n = len(arr)

		for i in range(n // 2 - 1, -1, -1):
			heapify(arr, n, i)

		for i in range(n - 1, 0, -1):
			(arr[i], arr[0]) = (arr[0], arr[i])
			heapify(arr, i, 0)

	sort(sorted)
	return sorted


def selectionsort(arr: list[int]) -> list[int]:
	sorted = deepcopy(arr)
	for i in range(len(sorted)):
		min_index: int = i

		for j in range(i + 1, len(sorted)):
			if sorted[j] < sorted[min_index]:
				min_index = j
		(sorted[i], sorted[min_index]) = (sorted[min_index], sorted[i])

	return sorted
