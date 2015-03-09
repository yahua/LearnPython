import functools


#############  Test1
def log(text):
	if isinstance(text, str):
		def warpped(func):
			@functools.wraps(func)
			def decorator(*args, **kw):
				print 'begin call'
				print '%s %s():' % (text, func.__name__)
				f = func(*args, **kw)
				print 'end call'
				return f
			return decorator
		return warpped
	else:
		def decorator(*args, **kw):
			print 'begin call'
			print 'call %s():' % (text.__name__)
			f = text(*args, **kw)
			print 'end call'
			return f
		return decorator
	
@log('execute')
def test1Now():
	print '2015-03-09'
	return 'test1'
print test1Now()

@log
def test2Now():
	print '2015-03-09'
	return 'test2'
#ff = log(test2Now)
print test2Now()