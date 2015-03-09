print dir('abc')
print len('abc')
print 'abc'.__len__()


class MyObject(object):
	"""docstring for MyObject"""
	def __init__(self):
		super(MyObject, self).__init__()
		self.x = 9
		self.__y = 10
	def __len__(self):
		return 100
	def power(self):
		return self.x * self.x
obj = MyObject()
print len(obj)	
print hasattr(obj, 'x')	
print hasattr(obj, 'power')
print getattr(obj, 'x')
print getattr(obj, 'power')
print hasattr(obj, '__y')	