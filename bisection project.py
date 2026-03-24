"""
This is a root finder using a bisection method. This is the first version. More improvements later...

Features:
1. Utilizes bisection method to search for to for a root in your HARD-CODED POLYNOMIAL

Limitations:
1. Hard-coded polynomials. x values are only consistent to one value from the f function.
2. Only finds a single root. You have to be precise enough to correctly set boundaries.

Soon to improve:
1. More variety for typing your polynomial to evaluate. No hard-code
2. Alternative method to be able to solve for multiple roots in a boundary.
3. Graphical-User Interface. I would potentially make this an application.
4. Polynomial Graph Plotting using MathPlotLib

"""
def f(x):
    #For now, this is a hard-coded function where x values are consistent
    return x-2

def bisection(f, a, b, counter=0):

    #To get the midpoint of the intervals we just set.
    midpoint=(a+b)/2

    if f(a)*f(b)>0:
    #Program will stop when their product is positive (There were no roots between the intervals a and b)
        return "No roots found!"

    elif f(a)*f(b)<0:
        if abs(b-a)<=0.001:
            #If the gap between the boundaries is insignificantly small, it only return the mean instead
            return f"The root for this function is approximately {midpoint:0.2f} after {counter} times!"
        
        elif f(midpoint)==0:
            #Checks if the midpoint is exactly the root
            return f"The root for this function is {midpoint} after {counter} times!"
        
        elif f(midpoint)>0:
            #Recursively calls for a new boundary, when the right half has consistent positive signs (no roots), disregarding that half
            return bisection(f, a, midpoint, counter+1)
        
        else:
            #Recursively calls for a new boundary, when the right half has consistent negative signs (no roots), disregarding that half
            return bisection(f, midpoint, b, counter+1)
        
    else:
        #Case triggers when one the product of the boundaries is zero. This means one the set boundaries is already the root.
        print("One of your boundaries is already the root!\n")
        if f(a)==0:
            return f"The root for this function is {float(a)}"
        elif f(b)==0:
            return f"The root for this function is {float(b)}"
        
print(bisection(f, -1, 2))