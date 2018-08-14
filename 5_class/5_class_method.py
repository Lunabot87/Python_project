#반드시 __del__이 정의 되었다고 해서 실행 되는 것은 아님
#레퍼런스 카운터가 1이상 이면 발생하지 않음

class Myclass:
	## 앞뒤로 '__' 가 붙은 것은 특별한 용도로 미리 정의 되어진 것
	def __init__(self, value):						#생성자 메서드
		self.Value = value
		print("Class is created! Value = ",value)

	def __del__(self):								#소멸자 메서드
		print("Class is deleted!")

c = Myclass(10)										#레퍼런스 카운터 증가 (1)
c_copy = c 											#레퍼런스 카운터 증가 (2)
del c 												#레퍼런스 카운터 감소 (1)
del c_copy											#레퍼런스 카운터 감소 (0)

# 레퍼런스 카운터가 0이면 __del__ 발생