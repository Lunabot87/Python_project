class Person:
	" 부모클래스 "
	def __init__ (self, name, phoneNumber):				#메서드 생산자 생성
		self.Name = name
		self.PhoneNumber = phoneNumber

	def PrintInfo(self):
		print("Info(Name : {0}, Phone : {1})".format(self.Name, self.PhoneNumber))

	def PrintPersonData(self):
		print("Person(Name : {0}, Phone : {1})".format(self.Name, self.PhoneNumber))

class Student(Person):
	" 자식클래스 "
	def __init__(self, name, phoneNumber, subject, studentID):
		Person.__init__(self, name, phoneNumber)
		self.Subject = subject
		self.StudentID = studentID

	def PrintStudentData(self):
		print("Student(Subject : {0}, StudentID : {1})".format(self.Subject, self.StudentID))

	def PrintInfo(self):			#Person의 PrintInfo() 재정의 (Method Overriding)
		#print("Info(Name : {0}, Phone : {1})".format(self.Name, self.PhoneNumber))		#위의 정의되어진 것을 다시 재정의 한것과 같으므로 명시적 정의를 하는 방법으로 최소한이 작업으로 할 수 있다.
		Person.PrintInfo(self)
		print("Info(Subject : {0}, StudentID : {1})".format(self.Subject, self.StudentID))

p = Person("Derick", "010-8244-1341")
s = Student("Marry", "010-123-4567", "Computer Science", "990999")

p.PrintInfo()
s.PrintInfo()