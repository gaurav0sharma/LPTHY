class employee:
	def __init__(self,name,salary):
		self.name = name
		self.salary = salary
	
	def displayDetail(self):
		print(dir(self))
		print(self.name,self.salary)


emp1 = employee("gaurav",'15000')
emp2 = employee('saurav','56000')
emp1.displayDetail()
