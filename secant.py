def secant(f, x_b, x_n, error, max_iterations):
    
    #Checking if root in interval via IVT Theorem
    if f(x_b) * f(x_n) >= 0:
        print("There is no root in the specified interval because f(x_n * f(x_b) > 0! Please input another interval and run the function again")
        return None
    
    #Counters
    iterations = 1
    x_new = 0
    
    while iterations <= max_iterations:
        #Solving for intermediate value using Secant method formula
        x_new = x_n - f(x_n) * (x_n - x_b) / (f(x_n) - f(x_b))
            
        if f(x_new) == 0 or abs(x_new - x_n) < error:
            return print(f"The root is {x_new} and the number of iterations to solve is {iterations}")
        
        #reassigning values for iteration
        x_b = x_n
        x_n = x_new
        iterations += 1
    
    #For non-convergence
    return print(f'Secant method has failed to converge. Final iteration values yielded an approximated root of {x_new} with function value{f(x_new)}')

f = lambda x: x ** 3 - 5*x ** 2 + 1.01*x + 1.88
secant(f, 2.5, 5, 10 ** -7, 50)