class SuperClass:
	x = 10
	def printX(self):
		print(self.x)
class SubClass(SuperClass):
	y = 20
	def printX(self):
		SuperClass.printX(self)			#재생성은 함수를 가져오는 것이 아닌 그 함수가 실행되는 것을 가져오는 것
	def printY(self):
		print(self.y)

s = SubClass()
s.a = 30
s.x = 50
print("SuperClass : ", SuperClass.__dict__)
print("SubClass : ", SubClass.__dict__)
print("s : ", s.__dict__)