class A3(object):
	phonelen = 11
	retireage = 60
	def __init__(self,name,age,phone,addr):
		self.name = name
		self.age = age
		self.phone = phone
		self.addr = addr
		
	def __getattr__(self,attr):
		if attr == 'phone':
			return self._phone[:-3] + '***'
		if attr == 'remian':
			return (self.retireage - self.age)
		else:
			raise AttributeError('Not Exist')
		
	def __setattr__(self,attr,value):
		if attr == 'age':
			if value<10 or value>100:
				raise ValueError('Invalid age')
		if attr == 'phone':
			value = str(value)
			attr = '_phone'
			if len(value) != self.phonelen:
				raise AttributeError('Invalid phone number')
		if attr == 'remian':
			raise TypeError('Cannot set')
		self.__dict__[attr] = value
		

if __name__ == '__main__':
	s = A3('Sue Jones',18,12345678901,'Area3')
	print s.phone
	print s.remian
	
	try:
		s.x
	except Exception as e:
		print e
		
	try:
		s.phone = 123456789
	except Exception as e:
		print e
		
	try:
		s.age = 9
	except Exception as e:
		print e