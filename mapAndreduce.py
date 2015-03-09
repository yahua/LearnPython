def f(x):
	return x*x
def my_map(fuction, l):
	return [fuction(x) for x in l]
l = xrange(1, 11)
print map(f, l)
print my_map(f, l)
print map(str, l)

########################## reduce
def add(x, y):
	return x+y
print reduce(add, [1,3,5,7,9])

def strToInt(s):
	if not isinstance(s, str):
		return 'not str'
	def fn(x, y):
		return x*10 + y
	def charToNum(s):
		return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
	return reduce(fn , map(charToNum, s))
print strToInt('12')	


##################  Test
def test1(l):
	def change(x):
		if len(x)>1:
			return x[0].upper() + x[1:].lower()
		else:
			return x[0].upper()
	return map(change, l)		
print test1(['michael', 'J', 'adaM'])

def test2(l):
	def prod(x, y):
		return x*y
	return reduce(prod, l)
print test2([1, 2, 3, 4])