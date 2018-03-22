class A4(object):
	phonelen = 11
	retireage = 59
	
	def __init__(self,name,age,phone,addr):
		self.name = name
		self.age = age
		self.phone = phone
		self.addr = addr
		
	def __getattribute__(self,attr):
		superget = object.__getattribute__
		if attr == 'phone':
			return superget(self,'phone')[:-3] + '***'
		if attr == 'remain':
			return superget(self,'retireage') - superget(self,'age')
		else:
			return superget(self,attr)
		
	def __setattr__(self,attr,value):
		if attr == 'age':
			if value<10 or value>100:
				raise ValueError('Invalid age')
		if attr == 'phone':
			value = str(value)
			if len(value) != self.phonelen:
				raise ValueError('Invalid phone number')
		if attr == 'remian':
			raise TypeError('Cannot set')
		self.__dict__[attr] = value
		
		
		
if __name__ == '__main__':
	s = A4('Sue Jones',18,12345678901,'Area3')
	print s.phone
	print s.remain
	
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