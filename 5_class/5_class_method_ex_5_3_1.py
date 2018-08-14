class CounterManager:
	insCount = 0
	def __init__(self):
		CounterManager.insCount += 1
	def PrintInstaceCount():
		print("Instance Count: ", CounterManager.insCount)
###
	#static method
	def staticPrintCount():
		print("Instance Count: ", CounterManager.insCount)
	#정적 메소드 등록
	SPrintCount = staticmethod(staticPrintCount)

	#class method 정의 첫 인자는 암묵적으로 class를 받음
	def classPrintCount(cls):
		print("Instance Count: ", cls.insCount)
	#클래스 메소드 등록
	CPrintCount = classmethod(classPrintCount)
###

a, b, c = CounterManager(), CounterManager(), CounterManager()

#예외 처리 7장에서 해결하는 방법을 배움
#CounterManager.PrintInstaceCount()
#b.PrintInstaceCount()

#정적 메서드로 인스턴스 객체 개수 출력
CounterManager.SPrintCount()
b.SPrintCount()

#클래스 메서드로 인스턴스 객체 개수 출력
CounterManager.CPrintCount()
b.CPrintCount()