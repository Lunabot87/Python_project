class Person:
	pass
class Bird:
	pass
class Student(Person):
	pass
p, s = Person(), Student()

##상속관계 판단 가능
print("p is instance of Person: ", isinstance(p, Person))
print("s is instance of Person: ", isinstance(s, Person))
print("s is instance of Bird: ", isinstance(s, Bird))
##3.x 버전부터는 모든 클래스는 object에서 파생됨
print("p is instance of object: ", isinstance(p, object))
print("p is instance of Bird: ", isinstance(p, Bird))
print("int is instance of object: ", isinstance(int, object))