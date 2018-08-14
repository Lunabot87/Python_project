class Animal:
	def __init__(self):
		print("Animal__init__()")
class Tiger(Animal):
	def __init__(self):
		#Animal.__init__(self)
		super().__init__()
		print("Tiger__init__()")
class Lion(Animal):
	def __init__(self):
		#Animal.__init__(self)
		super().__init__()
		print("Lion__init__()")
class Liger(Tiger, Lion):
	def __init__(self):
		#Tiger.__init__(self)
		#Lion.__init__(self)
		super().__init__()		#중복 생성자 호출을 방지하는 내장함수, 이때 생성자 호출 순서는 mro의 역순
		print("Liger__init__()")

l = Liger()