#coding:gbk
# 删除素数
def primeNumber(x):
	abs_X = abs(x)
	if abs_X>2:
		for i in xrange(2,abs_X-1):
			if abs_X%i == 0:
				return True
	return False	

print filter(primeNumber, xrange(1, 101))	