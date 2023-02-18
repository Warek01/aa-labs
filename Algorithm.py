from typing import Callable


class Algorithm:
	name: str
	function: Callable[[list[int]], list[int]]
	color: str
	data: list[int]

	def __init__(self, name: str, function: Callable[[list[int]], list[int]], color: str):
		self.name = name
		self.function = function
		self.color = color
		self.data = []
