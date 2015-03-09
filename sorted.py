#coding:gbk

l = [36, 33, 56, 9]
# 默认从小到大
print sorted(l) 

# 倒序
def reversed_cmp(x, y):
	if x>y:
		return -1
	elif x<y:
		return 1
	else:
		return 0
print sorted(l, reversed_cmp)		