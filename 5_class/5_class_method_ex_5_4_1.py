class GString:
	def __init__(self, init=None):
		self.content = init

	def __sub__(self, str):
		for i in str:
			self.content = self.content.replace(i, '')
		return GString(self.content)

	def Remove(self, str):
		return self.__sub__(str)

	def __add__(self, str):
		self.content = self.content + str
		return GString(self.content)

	def add(self, str):
		return self.__add__(str)

	def Print(self):
		print(self.content)

g = GString("ABCDEFGabcdefg")
g - "ABC"
g + "rrr"
# == g.add("rrr")
g.Print()