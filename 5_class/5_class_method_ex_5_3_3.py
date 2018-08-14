class CounterManager:
	# 사용시 이름이 _CounterManager__insCount
	__insCount = 0				#이름 변경을 위해 '__'를 변수명 앞에 사용
	def __init__(self):
		CounterManager.__insCount += 1
	def staticPrintCount():
		print("Instance Count: %d" % CounterManager.__insCount)
	SPrintCount = staticmethod(staticPrintCount)

a, b, c = CounterManager(), CounterManager(), CounterManager()
CounterManager.SPrintCount()

#C++ 처럼 접근 불가로 만드는 것이 아닌 이름을 변경 함으로써 기존 이름으로 접근을 하지 못하게 하는 것

#클래스 구성 보기
#print(dir(CounterManager))