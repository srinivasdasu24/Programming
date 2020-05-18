#The function returned during the outer() invocation is a closure.

def outer(par):
	loc = par
	def inner():
		return loc
	return inner

var = 1
fun = outer(var)
print(fun())




#another example

def makeclosure(par):
	loc = par
	def power(p):
		return p ** loc
	return power

fsqr = makeclosure(2)
fcub = makeclosure(3)
for i in range(5):
	print(i, fsqr(i), fcub(i))