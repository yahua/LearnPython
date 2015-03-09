# -*- coding:utf-8 -*-

age = int(20)
if age >= 20:
	print 'your age is', age
elif age >= 10:
	print 'your age is', age
else:
    print 'your age is', age

names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print name

sum = 0
for x in range(1,5):
	sum = sum + x
print sum

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print sum