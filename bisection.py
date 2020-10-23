def bisection_method(f, a, b, error, max_iterations):
    #Checking if root exists via IVT Theorem
    if f(a) * f(b) >= 0:
        print("There is no root in the specified interval because f(a) * f(b) > 0! Please input another interval and run the function again")
        return None
    
    #Setting up counters 
    iterations = 1
    midpoint = 0
    
    while iterations <= max_iterations:
        
        #Taking midpoint and applying bisection method
        midpoint = (a+b)/2
        f_midpoint = f(midpoint)
        
        if f_midpoint == 0 or abs(a-b) <= error:
            return print(f"The root is {midpoint} and the number of iterations to solve is {iterations}")
        
        elif f(a) * f_midpoint < 0:
            b = midpoint
            
        elif f(a) * f_midpoint > 0:
            a = midpoint
        
        iterations += 1
    
    #For non-convergence
    return print(f'Bisection method has failed to converge. Final iteration values yielded an approximated root of {midpoint} with function value{f(midpoint)}')
    
f = lambda x: x ** 3 - 5*x ** 2 + 1.01*x + 1.88
bisection_method(f, 0, 1, 10 ** -7, 30)       