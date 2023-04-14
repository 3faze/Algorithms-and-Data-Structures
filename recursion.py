#recursion 
#with factorials

def fact(n):
	if n >= 1:
		return n * fact(n - 1)
	else:
		return 1
		
print("factorials:", fact(5))

#with fibonacci
def fibonacci(times):
	print("fibonacci(range => " + str(times) + "):\n")
	curr = 0
	n1 = 0
	n2 =1
	for i in range(times):
		print(n1)
		nth = n1 + n2
		n1 = n2
		n2 = nth
		curr += 1

fibonacci(10)