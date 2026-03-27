"""
Newton-Rhapson Method is just another numerical method to find a root of a certain function. 
The same as bisection method. But it uses derivatives to approximate roots.

But we do know that some functions have multiple x-intercepts right??
But this method only finds one root per run — whichever one your initial guess is closest to. 

My functions here are only hard-coded and i can't implement complex trancendental equations yet!!!

"""
import math # just in case you want to include trancendental functions

def newton_raphson(f, df, x_old:float, tolerance=0.00001, iteration=0, max_iteration=150):

    #Let's initialize it for test casing
    derivative = df(x_old)

    #We have to check first if the denominator would be zero
    if derivative == 0:
        raise ValueError("Derivative is zero at this guess. Try a different starting point.")
    
    #This is the actual formula for the Newton-Rhapson
    x_new = x_old - f(x_old) / derivative  # x is new, x0 is previous
    
    #Base case, it will only stop if there is a small difference in approximation, depending on our tolerance.
    #The formula should execute first so we can store the new x, before comparing both.
    if abs(x_new - x_old) < tolerance:
        return x_new, iteration #Ai just told me you can return more than 1 values. This will be treated like a tuple. Order matters.
    
    #Worst-case scenario if the loop is consuming too much memory... 
    if iteration >= max_iteration:
        return None, iteration  # None signals failure
    
    #Recursively calls the function, but replacing the old x0 with new 'x' everytime their difference is still greater than our tolerance approximation.
    return newton_raphson(f, df, x_new, tolerance, iteration+1, max_iteration)

def main_testing():

    #HARD CODE FOR NOW, EVEN THE DERIVATIVES!!!
    f  = lambda x: x**6+x**2-12
    df = lambda x: (6*x**5)+2*x
    #Don't be confused, you have to update the printed function in line 50 if you changed the function here...


    while True:
        try:
            print("\n\n\n")
            print("-^%^-"*10)
            print()
            print("f(x)=x^6 + x^2 - 12\n\nJust hard code it if you want to change the function man")
            print("-^%^-"*10)
            print()

            raw = input("Enter a guess number (or 'q' to quit): ")
            if raw.lower() == 'q':
                print("Thank you, Goodbye!")
                break
            guess = float(raw)

            result = newton_raphson(f, df, guess)

            if result[0] is None:
                print(f"\n\nI can't find the root, just use another tool...🥲")
            elif abs(result[0]) <= 0.0001:
                print(f"\n\nThe root is approximately 0, found in {result[1]} iterations! 😠")
            else:
                print(f"\n\nThe root is {result[0]:.4f} found in {result[1]} iterations! 😮")

        except ValueError as e:
            print(f"Error: {e}. I don't know bro🥀")

if __name__=='__main__':
    main_testing()
