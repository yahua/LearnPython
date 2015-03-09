classmates = ['Michael', 'Bob', 'Tracy']

def printClassmates():
	print classmates

print classmates
print len(classmates)
print classmates[0]
print classmates[-1]
# add
classmates.append('Adam')
printClassmates()

classmates.insert(1, 'Jack')
printClassmates()

classmates.pop()
printClassmates()

print 'the type classmates is',type(classmates)

print classmates[0:2]
print classmates[:2]
print classmates[-2:]
L = range(100)
print L
print L[:10:2]
print L[::5]
print 'abcderg'[::-1]

###############  tuple  can not change list

classmates = (1, 2)
printClassmates()

singleTuple = (1,)    #single elt should add ,    not (1)
print singleTuple