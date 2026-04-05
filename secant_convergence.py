"""
Secant Convergence Method is pretty much the same method as newton rhapson where you need to use a derivative of a function. Newton-Rhapson is faster
than Secant Convergence, but it lacks the versatility when you can't even derive functions like humans do. Theformula is pretty much the same
the only difference; Secant convergence method uses the fundamental formula for derivatives: 

lim h->0 = df= f(x+h)-f(x) / h

Speed ranking of root finding methods:
1. Newton-Rhapson (not versatile)
2. Secant Convergence (more versatile but a bit slower)
3. Bisection (slowest but the most versatile)


*This was lowkey the fastest to implement since I already got the gist of recursion when implementing bisection and newton-rhapson before.


Limited features:
1. Hard Coded functions, enough said
2. Only finds a single root, it depends on the user's initial x values.
"""
import math 

def secant_convergence(f, a, b, tol=0.0001, counter=0, max_iteration=200):
    try: 

        #Formula, derived from the fundamental formula of derivative (Just the same as newthon rhapson)
        c= b - f(b) / ( (f(b)-f(a)) / (b-a))

        #If the changes between the previous and the new value is insignificantly small enough.
        if abs(c-b)<=tol:
            return c, counter
        
        #When recursion calls too much. To avoid infinite recursion (Second Base Case)
        elif counter>=max_iteration:
            return c, counter
        
    except ZeroDivisionError as e:
        #In case the denominators of the formula are equal to zero. Easy life with exception, I don't need to overthink all edge cases.
        b+=0.000000001 # If one of the conditions where b=a (guranteed zero), this insignificantly adds a small value to b just to remove equality.
        return secant_convergence(f, a, b, tol, counter+1, max_iteration) #Repeat the recursion call with the revised b value

    #YESSS THIS IS THE MAIN RECURSION CALL! We want to store our tolerance, action counts, and iterations
    return secant_convergence(f, b, c, tol, counter+1, max_iteration)
    

#JUST HARD CODE YOUR FUNCTION AGAIN BRUV!!
result = secant_convergence(f=lambda x: math.sin(x), a=2, b=4)

print(f"One of your root/s is {result[0]:0.4f} and that took me {result[1]} times! 🥀")


