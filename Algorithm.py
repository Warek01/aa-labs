from typing import Callable, Any


class Algorithm:
	name: str
	function: Callable[[int], Any]
	color: str
	data: list[int]

	def __init__(self, name: str, function: Callable[[int], Any], color: str):
		self.name = name
		self.function = function
		self.color = color
		self.data = []
