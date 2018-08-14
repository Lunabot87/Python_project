str = "NOT Class Member"
class GString:
	str = ""
	def Set(self, msg):
		self.str = msg
	def Print(self):				#self 는 인스턴트 객체
		#print(str)					#애러 발생
		print(format(self.str))		#이런식으로 써야 애러가 발생하지 않음

g = GString()
g.Set("First Message")
g.Print()