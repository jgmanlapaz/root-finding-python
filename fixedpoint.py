# Python Code for Fixed Point Iteration
def g(x):
	return (5.00*x*x - 1.01*x - 1.88)/(x*x)

def fixed_pt(x_zero, N):
	n = 1
	while n < N:
		x_one = g(x_zero)
		if abs(x_one - x_zero) < 0:
			break
		x_zero = x_one
		n += 1
	return x_one

print(fixed_pt(5, 10))