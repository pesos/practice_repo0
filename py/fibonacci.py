def fibonacci(n):
	a = 0
	b = 1
	for i in range(n):
		b = b+a
		a = b-a
	return a

def fibgen(n):
	a = 0
	b = 1
	for i in range(n):
		b = b+a
		a = b-a
		yield a
		

# print(fibonacci(6))

# for i in fibgen(10):
# 	print(i)

