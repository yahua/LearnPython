dic = {'Michael': 95, 'Bob': 99, 'Tracy': 77}
print dic

print dic['Michael']
dic['Adam'] = 66
print dic
dic['Adam'] = 88
print dic
dic.pop('Adam')
print dic

#########################  set
s = set([1, 2, 3])
print s
s = set([1, 1, 2, 3])
print s
s.add(4)
print s
s1 = set([1, 2, 4, 5])
print s & s1
print s | s1