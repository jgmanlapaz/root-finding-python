# Python Code for Newton-Raphson Method
import math
def f(x):
	return 2*x - math.cos(x)

def f_prime(x):
	return 2 + math.sin(x)

def newton(x_in, N):
	n = 1
	x = 0

	while n < N:
		x = x_in - f(x_in)/f_prime(x_in)
		if f(x) == 0 or abs(x - x_in) < 0:
			break 
		x_in = x
		n += 1
	return x

print(newton(1, 6))