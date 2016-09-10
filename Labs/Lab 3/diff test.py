def f(x):
	return x**2

def fprime(x,x0):
	return (f(x) - f(x0))/(x-x0)

x0 = 3
a = []

for n in range(1,100):
	x = x0 + 1/n
	a.append(fprime(x,x0))

print(a[1])

print(a[-1])