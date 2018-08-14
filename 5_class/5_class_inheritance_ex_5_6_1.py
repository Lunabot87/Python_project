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

		#self.Name = name
		#self.PhoneNumber = phoneNumber 		#두번 정의가 되어있다.
		Person.__init__(self, name, phoneNumber)	#명시적으로 Person 생성자를 호출 self(인스턴트 객체)(Name : {0}, Phone : {1})".format(self.Name, self.PhoneNumber)를 함께 전달해야함
		self.Subject = subject
		self.StudentID = studentID

	def PrintStudentData(self):
		print("Student(Subject : {0}, StudentID : {1})".format(self.Subject, self.StudentID))

p = Person("Derick", "010-8244-1341")
s = Student("Marry", "010-123-4567", "Computer Science", "990999")

print(p.__dict__)			#인스턴트 객체 사전객체(__dict__)로 관리됨
print(s.__dict__)
print(Student.__bases__)		#부모클래스를 확인하는 법
print(issubclass(Student, Person))	#클래스의 상관관계를 확인 하는 함수 issubclass(자식크래스, 부모 클래스)

s.PrintPersonData()			#부모클래스에서 물려받은 함수 사용 student에 저장된 데이터가 출력됨
s.PrintStudentData()