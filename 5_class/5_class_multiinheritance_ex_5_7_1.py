class Tiger:
	def Jump(self):
		print("호랑이처럼 멀리 점프하기")
	def Cry(self):
		print("호랑이 : 어흥~")

class Lion:
	def Bite(self):
		print("사자처럼 한입에 꿀꺽하기")
	def Cry(self):
		print("사자 : 으르렁~")

class Liger(Tiger, Lion):
	def Play(self):
		print("라이거만의 사육사와 재미있게 놀기")

l = Liger()
l.Jump()
l.Bite()
l.Play()	#각 클래스 메서드의 함수가 작동

l.Cry()		#우선 선언도니 Tiger의 메서드가 작동
print(Liger.__mro__)	#상속구조에서 메서드의 이름을 찾는 순서 함수