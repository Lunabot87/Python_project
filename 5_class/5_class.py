class Person:
	Name = "Default Name"
	def Print(self):
		print("My name is {0}".format(self.Name))

p1 = Person()
p2 = Person()
p1.Print()

#p1.Name = "김현준!"
#p1.Print()

Person.title = "New title"
p1.age = "25"
print("p1's title: ", p1.title)
print("p1's age: ", p1.age)

#인스턴트 객체의 내장 속성'__class__'
p1.Print()
p2.Print()
p1.__class__.Name = "클래스 데이터를 변경합니다."
p1.Print()
p2.Print()
p1.Name = "김현준!!"
p1.Print()
p2.Print()