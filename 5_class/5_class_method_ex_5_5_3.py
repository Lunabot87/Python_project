class Sequencer:
	def __init__(self, maxValue):
		self.maxValue = maxValue
	def __len__(self):					#len 내장 함수
		return self.maxValue
	def __getitem__(self, index):
		if 0 < index <= self.maxValue:
			return index * 10
		else:
			raise IndentationError("Index out of range")	#7장에서 다룸

	def __contains__(self, item):
		return 0 < item <= self.maxValue

s = Sequencer(5)
print(s[1])
print(s[3])
print(len(s))
print(3 in s)