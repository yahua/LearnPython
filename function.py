a = -100
print abs(a)
jdz = abs
print jdz(a)

def my_abs(x):
	if not isinstance(x, (int, float)):
		raise TypeError('bad operand type')
	if x >= 0:
		return x
	else:
		return -x
print 'print my_abs:',my_abs(a)
print my_abs('a')