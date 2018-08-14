class Myclass:
	## 앞뒤로 '__' 가 붙은 것은 특별한 용도로 미리 정의 되어진 것
	def __init__(self, value):						#생성자 메서드
		self.Value = value
		print("Class is created! Value = ",value)

	def __del__(self):								#소멸자 메서드
		print("Class is deleted!")

def foo():
	d = Myclass(10)

foo()